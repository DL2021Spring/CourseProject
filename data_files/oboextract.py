






import sys
import re
from string import lowercase

options = None

def case_normalize_initial(s):
    
    
    if re.match(r'^[A-Z][a-z]{2,}', s):
        
        return s[0].lower()+s[1:]
    else:
        return s

def case_normalize_all_words(s):
    return " ".join([case_normalize_initial(w) for w in s.split(" ")])

class Term:
    def __init__(self, tid, name, synonyms=None, defs=None, 
                 is_a=None, part_of=None):
        self.tid      = tid
        self.name     = name
        self.synonyms = synonyms if synonyms is not None else []
        self.defs     = defs     if defs     is not None else []
        self.is_a     = is_a     if is_a     is not None else []
        self.part_of  = part_of  if part_of  is not None else []

        self.parents  = []
        self.children = []

        
        self.objects    = []
        self.components = []

        self.cleanup()

    def obo_idspace(self):
        
        if ":" in self.tid:
            
            
            
            s = self.tid[:self.tid.index(":")]
            if len([c for c in s if c in lowercase]) == len(s):
                return s.upper()
            else:
                return s
        else:
            
            m = re.match(r'^(.[A-Za-z_]+)', self.tid)
            
            return m.group(1)

    def resolve_references(self, term_by_id, term_by_name=None):
        
        for ptid, pname in self.is_a:
            if ptid not in term_by_id:
                print >> sys.stderr, "Warning: is_a term '%s' not found, ignoring" % ptid
                continue
            parent = term_by_id[ptid]
            
            
            if pname is not None and term_by_name is not None and term_by_name[pname] is not None:
                assert parent == term_by_name[pname]
            if self in parent.children:
                print >> sys.stderr, "Warning: dup is-a parent %s for %s, ignoring" % (ptid, str(self))
            else:
                self.parents.append(parent)
                parent.children.append(self)

        
        for prel, ptid, pname in self.part_of:
            if ptid not in term_by_id:
                print >> sys.stderr, "Error: part_of term '%s' not found, ignoring" % ptid
                continue
            pobject = term_by_id[ptid]
            
            if pname is not None and term_by_name is not None and term_by_name[pname] is not None:
                assert pobject == term_by_name[pname]
            if self in pobject.components:
                print >> sys.stderr, "Warning: dup part-of parent %s for %s, ignoring" % (ptid, str(self))
            else:
                self.objects.append((prel, pobject))
                pobject.components.append((prel, self))

    def _case_normalize(self, cn_func):
        self.name = cn_func(self.name)
        for i in range(len(self.synonyms)):
            self.synonyms[i] = (cn_func(self.synonyms[i][0]), self.synonyms[i][1])
        for i in range(len(self.is_a)):
            if self.is_a[i][1] is not None:
                self.is_a[i] = (self.is_a[i][0], cn_func(self.is_a[i][1]))

    def case_normalize_initial(self):
        
        global case_normalize_initial
        self._case_normalize(case_normalize_initial)

    def case_normalize_all_words(self):
        
        global case_normalize_all_words
        self._case_normalize(case_normalize_all_words)

    def cleanup(self):
        
        for i, s in enumerate(self.synonyms):
            if s[-1] == ".":
                
                if re.search(r'\b[a-z]{2,}\.$', s):
                    c = s[:-1]
                    print >> sys.stderr, "Note: cleanup: '%s' -> '%s'" % (s, c)
                    self.synonyms[i] = c

    def __str__(self):
        return "%s (%s)" % (self.name, self.tid)

def parse_obo(f, limit_prefixes=None, include_nameless=False):
    all_terms = []
    term_by_id = {}

    
    skip_block = True
    tid, prefix, name, synonyms, definitions, is_a, part_of, obsolete = None, None, None, [], [], [], [], False
    for ln, l in enumerate(f):
        
        if l.strip() == "[Term]":
            assert tid is None
            assert name is None
            assert is_a == []
            skip_block = False
        if l.strip() == "[Typedef]":
            skip_block = True
        elif re.match(r'^id:.*', l) and not skip_block:
            assert tid is None, str(ln)+' '+tid
            
            l = re.sub(r'\s*\!.*', '', l)

            
            
            
            
            
            
            m = re.match(r'^id: (([A-Za-z](?:\S*(?=:)|[A-Za-z_]*)):?\S+)\s*$', l)
            if m is None:
                print >> sys.stderr, "line %d: failed to match id, ignoring: %s" % (ln, l.rstrip())
                tid, prefix, name, synonyms, is_a, part_of, obsolete = None, None, None, [], [], [], False
                skip_block = True
            else:
                tid, prefix = m.groups()
        elif re.match(r'^name:.*', l) and not skip_block:
            assert tid is not None
            assert name is None
            m = re.match(r'^name: (.*?)\s*$', l)
            assert m is not None
            name = m.group(1)
        elif re.match(r'^is_a:.*', l) and not skip_block:
            assert tid is not None
            
            
            
            
            
            m = re.match(r'^is_a: (\S+) *(?:\{[^{}]*\} *)?(?:\!.*?)?\! *(.*?)\s*$', l)
            if m:
                is_a.append(m.groups())
            else:
                m = re.match(r'^is_a: (\S+)\s*$', l)
                if m is not None:
                    is_a.append((m.group(1), None))
                else:
                    print >> sys.stderr, "Error: failed to parse '%s'; ignoring is_a" % l
        elif re.match(r'^relationship:\s*\S*part_of', l) and not skip_block:
            assert tid is not None
            assert name is not None
            
            
            m = re.match(r'^relationship: +(?:OBO_REL:)?(\S+) +(\S+) *(?:\{[^{}]*\} *)?\! *(.*?)\s*$', l)
            if m:
                part_of.append(m.groups())
            else:
                m = re.match(r'^relationship: +(?:OBO_REL:)?(\S+) +(\S+)\s*$', l)
                if m is not None:
                    part_of.append((m.group(1), m.group(2), None))
                else:
                    print >> sys.stderr, "Error: failed to parse '%s'; ignoring part_of" % l
        elif re.match(r'^synonym:.*', l) and not skip_block:
            assert tid is not None
            assert name is not None
            
            
            m = re.match(r'^synonym: "(.*)" ([A-Za-z_ ]*?) *\[.*\]\s*$', l)
            assert m is not None, "Error: failed to parse '%s'" % l
            synstr, syntype = m.groups()
            if synstr == "":
                print >> sys.stderr, "Note: ignoring empty synonym on line %d: %s" % (ln, l.strip())
            else:
                synonyms.append((synstr,syntype))
        elif re.match(r'^def:.*', l) and not skip_block:
            assert tid is not None
            assert name is not None
            m = re.match(r'^def: "(.*)" *\[.*\]\s*$', l)
            assert m is not None, "Error: failed to parse '%s'" % l
            definition = m.group(1)
            if definition == "":
                print >> sys.stderr, "Note: ignoring empty def on line %d: %s" % (ln, l.strip())
            else:
                definitions.append(definition)
        elif re.match(r'^is_obsolete:', l):
            m = re.match(r'^is_obsolete:\s*true', l)
            if m:
                obsolete = True
        elif re.match(r'^\s*$', l):
            
            
            if (tid is None and prefix is None and name is None and
                synonyms == [] and definitions == [] and 
                is_a == [] and part_of == []):
                
                continue

            
            if (obsolete or
                (limit_prefixes is not None and prefix not in limit_prefixes)):
                
                tid, prefix, name, synonyms, definitions, is_a, part_of, obsolete = None, None, None, [], [], [], [], False
            elif not skip_block:
                assert tid is not None, "line %d: no ID for '%s'!" % (ln, name)
                if name is None and not include_nameless:
                    print >> sys.stderr, "Note: ignoring term without name (%s) on line %d" % (tid, ln)
                else:
                    if tid not in term_by_id:
                        t = Term(tid, name, synonyms, definitions, 
                                 is_a, part_of)
                        all_terms.append(t)
                        term_by_id[tid] = t
                    else:
                        print >> sys.stderr, "Error: duplicate ID '%s'; discarding all but first definition" % tid
                tid, prefix, name, synonyms, definitions, is_a, part_of, obsolete = None, None, None, [], [], [], [], False
            else:
                pass
        else:
            
            pass

    assert tid is None
    assert name is None
    assert is_a == []
    
    return all_terms, term_by_id

def argparser():
    import argparse

    ap=argparse.ArgumentParser(description="Extract terms from OBO ontology.")
    ap.add_argument("-l", "--limit", default=None, metavar="PREFIX", help="Limit processing to given ontology prefix or prefixes (multiple separated by \"|\").")
    ap.add_argument("-d", "--depth", default=None, metavar="INT", help="Limit extraction to given depth from initial nodes.")
    ap.add_argument("-nc", "--no-case-normalization", default=False, action="store_true", help="Skip heuristic case normalization of ontology terms.")
    ap.add_argument("-nm", "--no-multiple-inheritance", default=False, action="store_true", help="Exclude subtrees involving multiple inheritance.")
    ap.add_argument("-ns", "--no-synonyms", default=False, action="store_true", help="Do not extract synonyms.")
    ap.add_argument("-nd", "--no-definitions", default=False, action="store_true", help="Do not extract definitions.")
    ap.add_argument("-e", "--exclude", default=[], metavar="TERM", nargs="+", help="Exclude subtrees rooted at given TERMs.")
    ap.add_argument("-s", "--separate-children", default=[], default=False, action="store_true", help="Separate subontologies found as children of the given term.")
    ap.add_argument("file", metavar="OBO-FILE", help="Source ontology.")
    ap.add_argument("-p", "--separate-parents", default=[], default=False, action="store_true", help="Separate subontologies of parents of the given terms.")
    ap.add_argument("terms", default=[], metavar="TERM", nargs="*", help="Root terms from which to extract.")
    return ap

multiple_parent_skip_count = 0

def get_subtree_terms(root, collection=None, depth=0):
    global options
    global multiple_parent_skip_count

    if collection is None:
        collection = []

    if root.traversed or root.excluded:
        return False

    if options.depth is not None and depth > options.depth:
        return False

    if options.no_multiple_inheritance and len(root.parents) > 1:
        
        if multiple_parent_skip_count < 10:
            print >> sys.stderr, "Note: not traversing subtree at %s %s: %d parents" % (root.tid, root.name, len(root.parents))
        elif multiple_parent_skip_count == 10:
            print >> sys.stderr, "(further 'not traversing subtree; multiple parents' notes suppressed)"
        multiple_parent_skip_count += 1
        return False

    root.traversed = True


    collection.append(root)



    for child in root.children:
        get_subtree_terms(child, collection, depth+1)
    return collection

def exclude_subtree(root):
    if root.traversed:
        return False
    root.traversed = True
    root.excluded = True
    for child in root.children:
        exclude_subtree(child)

def main(argv=None):
    global options

    arg = argparser().parse_args(argv[1:])
    options = arg

    if arg.depth is not None:
        arg.depth = int(arg.depth)
        assert arg.depth > 0, "Depth limit cannot be less than or equal to zero"

    limit_prefix = arg.limit
    if limit_prefix is None:
        limit_prefixes = None
    else:
        limit_prefixes = limit_prefix.split("|")

    fn = arg.file

    if not arg.no_case_normalization:
        for i in range(len(arg.terms)):
            
            arg.terms[i] = case_normalize_initial(arg.terms[i])

    f = open(fn)
    all_terms, term_by_id = parse_obo(f, limit_prefixes)
    
    
    for t in all_terms:
        t.resolve_references(term_by_id)

    if not arg.no_case_normalization:
        for t in all_terms:
            
            
            
            if t.obo_idspace() in ("FMA", "WBbt"):
                t.case_normalize_initial()
            elif t.obo_idspace() == "SAO":
                t.case_normalize_all_words()

    print >> sys.stderr, "OK, parsed %d (non-obsolete) terms." % len(all_terms)

    term_by_name = {}
    for t in all_terms:
        if t.name not in term_by_name:
            term_by_name[t.name] = t
        else:
            print >> sys.stderr, "Warning: duplicate name '%s'; no name->ID mapping possible" % t.name
            
            term_by_name[t.name] = None

    for rootterm in arg.terms:
        
        assert arg.separate_parents or rootterm in term_by_name, "Error: given term '%s' not found (or obsolete) in ontology!" % rootterm

    
    for t in all_terms:
        t.children = []
        t.parents  = []
    for t in all_terms:
        for ptid, pname in t.is_a:
            if ptid not in term_by_id:
                print >> sys.stderr, "Error: is_a term '%s' not found, removing" % ptid
                continue
            parent = term_by_id[ptid]
            
            
            if pname is not None and pname in term_by_name and term_by_name[pname] is not None:
                if parent != term_by_name[pname]:
                    print >> sys.stderr, "Warning: given parent name '%s' mismatches parent term name (via ID) '%s'" % (parent.name, pname)
            if t in parent.children:
                print >> sys.stderr, "Warning: ignoring dup parent %s for %s" % (ptid, str(t))
            else:
                t.parents.append(parent)
                parent.children.append(t)

    for t in all_terms:
        t.traversed = False
        t.excluded  = False

    for excludeterm in arg.exclude:
        assert excludeterm in term_by_name, "Error: exclude term '%s' not found (or obsolete) in ontology!" % excludeterm
        exclude_subtree(term_by_name[excludeterm])
        
    for t in all_terms:
        t.traversed = False

    rootterms = []
    if not arg.separate_parents:
        
        for t in arg.terms:
            if t not in term_by_name:
                print >> sys.stderr, "Error: given term '%s' not found!" % t
                return 1
            else:
                rootterms.append(term_by_name[t])

        
        if len(rootterms) == 0:
            for t in all_terms:
                if len(t.parents) == 0:
                    rootterms.append(t)
            
            print >> sys.stderr, "Extracting from %d root terms." % len(rootterms)

    else:
        assert not arg.separate_children, "Incompatible arguments"
        
        
        unique_parents = {}
        for t in arg.terms:
            
            if t in term_by_name:
                for p in term_by_name[t].parents:
                    unique_parents[p] = True
        assert len(unique_parents) != 0, "Failed to find any of given terms"

        
        for p in unique_parents:
            p.excluded = True

        
        
        rootterms = [p for p in unique_parents]
        
        rootterms.sort(lambda a,b: cmp(a.name,b.name))
        arg.separate_children = True

        
        print >> sys.stderr, "Splitting at the following:", ",".join(rootterms)

    for rootterm in rootterms:
        if not arg.separate_children:
            
            


            for t in get_subtree_terms(rootterm):
                strs = []
                strs.append("name:Name:"+t.name)
                if not arg.no_synonyms:
                    for synstr, syntype in t.synonyms:
                        
                        
                        strs.append("name:Synonym:"+synstr)
                if not arg.no_definitions:
                    for d in t.defs:
                        strs.append("info:Definition:"+d)
                
                id_ = t.tid.replace(t.obo_idspace()+':', '', 1) 
                print id_ + '\t' + '\t'.join(strs)

        else:
            
            for c in rootterm.children:
                stt = []
                get_subtree_terms(c, stt)
            for n, tid, ntype in stt:
                    print "%s\t%s\t%s\t%s" % (c.name, n, tid, ntype)

if __name__ == "__main__":
    sys.exit(main(sys.argv))
