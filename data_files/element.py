import collections
import re
import sys
import warnings
from bs4.dammit import EntitySubstitution

DEFAULT_OUTPUT_ENCODING = "utf-8"
PY3K = (sys.version_info[0] > 2)

whitespace_re = re.compile("\s+")

def _alias(attr):
    
    @property
    def alias(self):
        return getattr(self, attr)

    @alias.setter
    def alias(self):
        return setattr(self, attr)
    return alias


class NamespacedAttribute(unicode):

    def __new__(cls, prefix, name, namespace=None):
        if name is None:
            obj = unicode.__new__(cls, prefix)
        else:
            obj = unicode.__new__(cls, prefix + ":" + name)
        obj.prefix = prefix
        obj.name = name
        obj.namespace = namespace
        return obj

class AttributeValueWithCharsetSubstitution(unicode):
    

class CharsetMetaAttributeValue(AttributeValueWithCharsetSubstitution):
    

    def __new__(cls, original_value):
        obj = unicode.__new__(cls, original_value)
        obj.original_value = original_value
        return obj

    def encode(self, encoding):
        return encoding


class ContentMetaAttributeValue(AttributeValueWithCharsetSubstitution):
    

    CHARSET_RE = re.compile("((^|;)\s*charset=)([^;]*)", re.M)

    def __new__(cls, original_value):
        match = cls.CHARSET_RE.search(original_value)
        if match is None:
            
            return unicode.__new__(unicode, original_value)

        obj = unicode.__new__(cls, original_value)
        obj.original_value = original_value
        return obj

    def encode(self, encoding):
        def rewrite(match):
            return match.group(1) + encoding
        return self.CHARSET_RE.sub(rewrite, self.original_value)


class PageElement(object):
    

    
    
    
    
    
    
    
    
    
    
    
    
    FORMATTERS = {
        "html" : EntitySubstitution.substitute_html,
        "minimal" : EntitySubstitution.substitute_xml,
        None : None
        }

    @classmethod
    def format_string(self, s, formatter='minimal'):
        
        if not callable(formatter):
            formatter = self.FORMATTERS.get(
                formatter, EntitySubstitution.substitute_xml)
        if formatter is None:
            output = s
        else:
            output = formatter(s)
        return output

    def setup(self, parent=None, previous_element=None):
        
        self.parent = parent
        self.previous_element = previous_element
        if previous_element is not None:
            self.previous_element.next_element = self
        self.next_element = None
        self.previous_sibling = None
        self.next_sibling = None
        if self.parent is not None and self.parent.contents:
            self.previous_sibling = self.parent.contents[-1]
            self.previous_sibling.next_sibling = self

    nextSibling = _alias("next_sibling")  
    previousSibling = _alias("previous_sibling")  

    def replace_with(self, replace_with):
        if replace_with is self:
            return
        if replace_with is self.parent:
            raise ValueError("Cannot replace a Tag with its parent.")
        old_parent = self.parent
        my_index = self.parent.index(self)
        self.extract()
        old_parent.insert(my_index, replace_with)
        return self
    replaceWith = replace_with  

    def unwrap(self):
        my_parent = self.parent
        my_index = self.parent.index(self)
        self.extract()
        for child in reversed(self.contents[:]):
            my_parent.insert(my_index, child)
        return self
    replace_with_children = unwrap
    replaceWithChildren = unwrap  

    def wrap(self, wrap_inside):
        me = self.replace_with(wrap_inside)
        wrap_inside.append(me)
        return wrap_inside

    def extract(self):
        
        if self.parent is not None:
            del self.parent.contents[self.parent.index(self)]

        
        
        
        last_child = self._last_descendant()
        next_element = last_child.next_element

        if self.previous_element is not None:
            self.previous_element.next_element = next_element
        if next_element is not None:
            next_element.previous_element = self.previous_element
        self.previous_element = None
        last_child.next_element = None

        self.parent = None
        if self.previous_sibling is not None:
            self.previous_sibling.next_sibling = self.next_sibling
        if self.next_sibling is not None:
            self.next_sibling.previous_sibling = self.previous_sibling
        self.previous_sibling = self.next_sibling = None
        return self

    def _last_descendant(self):
        "Finds the last element beneath this object to be parsed."
        last_child = self
        while hasattr(last_child, 'contents') and last_child.contents:
            last_child = last_child.contents[-1]
        return last_child
    
    _lastRecursiveChild = _last_descendant

    def insert(self, position, new_child):
        if new_child is self:
            raise ValueError("Cannot insert a tag into itself.")
        if (isinstance(new_child, basestring)
            and not isinstance(new_child, NavigableString)):
            new_child = NavigableString(new_child)

        position = min(position, len(self.contents))
        if hasattr(new_child, 'parent') and new_child.parent is not None:
            
            
            if new_child.parent is self:
                current_index = self.index(new_child)
                if current_index < position:
                    
                    
                    
                    
                    position -= 1
            new_child.extract()

        new_child.parent = self
        previous_child = None
        if position == 0:
            new_child.previous_sibling = None
            new_child.previous_element = self
        else:
            previous_child = self.contents[position - 1]
            new_child.previous_sibling = previous_child
            new_child.previous_sibling.next_sibling = new_child
            new_child.previous_element = previous_child._last_descendant()
        if new_child.previous_element is not None:
            new_child.previous_element.next_element = new_child

        new_childs_last_element = new_child._last_descendant()

        if position >= len(self.contents):
            new_child.next_sibling = None

            parent = self
            parents_next_sibling = None
            while parents_next_sibling is None and parent is not None:
                parents_next_sibling = parent.next_sibling
                parent = parent.parent
                if parents_next_sibling is not None:
                    
                    break
            if parents_next_sibling is not None:
                new_childs_last_element.next_element = parents_next_sibling
            else:
                
                
                new_childs_last_element.next_element = None
        else:
            next_child = self.contents[position]
            new_child.next_sibling = next_child
            if new_child.next_sibling is not None:
                new_child.next_sibling.previous_sibling = new_child
            new_childs_last_element.next_element = next_child

        if new_childs_last_element.next_element is not None:
            new_childs_last_element.next_element.previous_element = new_childs_last_element
        self.contents.insert(position, new_child)

    def append(self, tag):
        
        self.insert(len(self.contents), tag)

    def insert_before(self, predecessor):
        
        if self is predecessor:
            raise ValueError("Can't insert an element before itself.")
        parent = self.parent
        if parent is None:
            raise ValueError(
                "Element has no parent, so 'before' has no meaning.")
        
        
        if isinstance(predecessor, PageElement):
            predecessor.extract()
        index = parent.index(self)
        parent.insert(index, predecessor)

    def insert_after(self, successor):
        
        if self is successor:
            raise ValueError("Can't insert an element after itself.")
        parent = self.parent
        if parent is None:
            raise ValueError(
                "Element has no parent, so 'after' has no meaning.")
        
        
        if isinstance(successor, PageElement):
            successor.extract()
        index = parent.index(self)
        parent.insert(index+1, successor)

    def find_next(self, name=None, attrs={}, text=None, **kwargs):
        
        return self._find_one(self.find_all_next, name, attrs, text, **kwargs)
    findNext = find_next  

    def find_all_next(self, name=None, attrs={}, text=None, limit=None,
                    **kwargs):
        
        return self._find_all(name, attrs, text, limit, self.next_elements,
                             **kwargs)
    findAllNext = find_all_next  

    def find_next_sibling(self, name=None, attrs={}, text=None, **kwargs):
        
        return self._find_one(self.find_next_siblings, name, attrs, text,
                             **kwargs)
    findNextSibling = find_next_sibling  

    def find_next_siblings(self, name=None, attrs={}, text=None, limit=None,
                           **kwargs):
        
        return self._find_all(name, attrs, text, limit,
                              self.next_siblings, **kwargs)
    findNextSiblings = find_next_siblings   
    fetchNextSiblings = find_next_siblings  

    def find_previous(self, name=None, attrs={}, text=None, **kwargs):
        
        return self._find_one(
            self.find_all_previous, name, attrs, text, **kwargs)
    findPrevious = find_previous  

    def find_all_previous(self, name=None, attrs={}, text=None, limit=None,
                        **kwargs):
        
        return self._find_all(name, attrs, text, limit, self.previous_elements,
                           **kwargs)
    findAllPrevious = find_all_previous  
    fetchPrevious = find_all_previous    

    def find_previous_sibling(self, name=None, attrs={}, text=None, **kwargs):
        
        return self._find_one(self.find_previous_siblings, name, attrs, text,
                             **kwargs)
    findPreviousSibling = find_previous_sibling  

    def find_previous_siblings(self, name=None, attrs={}, text=None,
                               limit=None, **kwargs):
        
        return self._find_all(name, attrs, text, limit,
                              self.previous_siblings, **kwargs)
    findPreviousSiblings = find_previous_siblings   
    fetchPreviousSiblings = find_previous_siblings  

    def find_parent(self, name=None, attrs={}, **kwargs):
        
        
        
        r = None
        l = self.find_parents(name, attrs, 1)
        if l:
            r = l[0]
        return r
    findParent = find_parent  

    def find_parents(self, name=None, attrs={}, limit=None, **kwargs):
        

        return self._find_all(name, attrs, None, limit, self.parents,
                             **kwargs)
    findParents = find_parents   
    fetchParents = find_parents  

    @property
    def next(self):
        return self.next_element

    @property
    def previous(self):
        return self.previous_element

    

    def _find_one(self, method, name, attrs, text, **kwargs):
        r = None
        l = method(name, attrs, text, 1, **kwargs)
        if l:
            r = l[0]
        return r

    def _find_all(self, name, attrs, text, limit, generator, **kwargs):
        "Iterates over a generator looking for things that match."

        if isinstance(name, SoupStrainer):
            strainer = name
        elif text is None and not limit and not attrs and not kwargs:
            
            if name is True or name is None:
                return [element for element in generator
                        if isinstance(element, Tag)]
            
            elif isinstance(name, basestring):
                return [element for element in generator
                        if isinstance(element, Tag) and element.name == name]
            else:
                strainer = SoupStrainer(name, attrs, text, **kwargs)
        else:
            
            strainer = SoupStrainer(name, attrs, text, **kwargs)
        results = ResultSet(strainer)
        while True:
            try:
                i = next(generator)
            except StopIteration:
                break
            if i:
                found = strainer.search(i)
                if found:
                    results.append(found)
                    if limit and len(results) >= limit:
                        break
        return results

    
    
    @property
    def next_elements(self):
        i = self.next_element
        while i is not None:
            yield i
            i = i.next_element

    @property
    def next_siblings(self):
        i = self.next_sibling
        while i is not None:
            yield i
            i = i.next_sibling

    @property
    def previous_elements(self):
        i = self.previous_element
        while i is not None:
            yield i
            i = i.previous_element

    @property
    def previous_siblings(self):
        i = self.previous_sibling
        while i is not None:
            yield i
            i = i.previous_sibling

    @property
    def parents(self):
        i = self.parent
        while i is not None:
            yield i
            i = i.parent

    

    tag_name_re = re.compile('^[a-z0-9]+$')

    
    
    
    
    
    
    
    attribselect_re = re.compile(
        r'^(?P<tag>\w+)?\[(?P<attribute>\w+)(?P<operator>[=~\|\^\$\*]?)' +
        r'=?"?(?P<value>[^\]"]*)"?\]$'
        )

    def _attr_value_as_string(self, value, default=None):
        
        value = self.get(value, default)
        if isinstance(value, list) or isinstance(value, tuple):
            value =" ".join(value)
        return value

    def _attribute_checker(self, operator, attribute, value=''):
        
        if operator == '=':
            
            return lambda el: el._attr_value_as_string(attribute) == value
        elif operator == '~':
            
            
            def _includes_value(element):
                attribute_value = element.get(attribute, [])
                if not isinstance(attribute_value, list):
                    attribute_value = attribute_value.split()
                return value in attribute_value
            return _includes_value
        elif operator == '^':
            
            return lambda el: el._attr_value_as_string(
                attribute, '').startswith(value)
        elif operator == '$':
            
            return lambda el: el._attr_value_as_string(
                attribute, '').endswith(value)
        elif operator == '*':
            
            return lambda el: value in el._attr_value_as_string(attribute, '')
        elif operator == '|':
            
            
            def _is_or_starts_with_dash(element):
                attribute_value = element._attr_value_as_string(attribute, '')
                return (attribute_value == value or attribute_value.startswith(
                        value + '-'))
            return _is_or_starts_with_dash
        else:
            return lambda el: el.has_attr(attribute)

    def select(self, selector):
        
        tokens = selector.split()
        current_context = [self]
        for index, token in enumerate(tokens):
            if tokens[index - 1] == '>':
                
                
                continue
            m = self.attribselect_re.match(token)
            if m is not None:
                
                tag, attribute, operator, value = m.groups()
                if not tag:
                    tag = True
                checker = self._attribute_checker(operator, attribute, value)
                found = []
                for context in current_context:
                    found.extend(
                        [el for el in context.find_all(tag) if checker(el)])
                current_context = found
                continue

            if '#' in token:
                
                tag, id = token.split('#', 1)
                if tag == "":
                    tag = True
                el = current_context[0].find(tag, {'id': id})
                if el is None:
                    return [] 
                current_context = [el]
                continue

            if '.' in token:
                
                tag_name, klass = token.split('.', 1)
                if not tag_name:
                    tag_name = True
                classes = set(klass.split('.'))
                found = []
                def classes_match(tag):
                    if tag_name is not True and tag.name != tag_name:
                        return False
                    if not tag.has_attr('class'):
                        return False
                    return classes.issubset(tag['class'])
                for context in current_context:
                    found.extend(context.find_all(classes_match))
                current_context = found
                continue

            if token == '*':
                
                found = []
                for context in current_context:
                    found.extend(context.findAll(True))
                current_context = found
                continue

            if token == '>':
                
                tag = tokens[index + 1]
                if not tag:
                    tag = True

                found = []
                for context in current_context:
                    found.extend(context.find_all(tag, recursive=False))
                current_context = found
                continue

            
            if not self.tag_name_re.match(token):
                return []
            found = []
            for context in current_context:
                found.extend(context.findAll(token))
            current_context = found
        return current_context

    
    
    def nextGenerator(self):
        return self.next_elements

    def nextSiblingGenerator(self):
        return self.next_siblings

    def previousGenerator(self):
        return self.previous_elements

    def previousSiblingGenerator(self):
        return self.previous_siblings

    def parentGenerator(self):
        return self.parents


class NavigableString(unicode, PageElement):

    PREFIX = ''
    SUFFIX = ''

    def __new__(cls, value):
        
        if isinstance(value, unicode):
            return unicode.__new__(cls, value)
        return unicode.__new__(cls, value, DEFAULT_OUTPUT_ENCODING)

    def __getnewargs__(self):
        return (unicode(self),)

    def __getattr__(self, attr):
        
        if attr == 'string':
            return self
        else:
            raise AttributeError(
                "'%s' object has no attribute '%s'" % (
                    self.__class__.__name__, attr))

    def output_ready(self, formatter="minimal"):
        output = self.format_string(self, formatter)
        return self.PREFIX + output + self.SUFFIX


class PreformattedString(NavigableString):
    

    def output_ready(self, formatter="minimal"):
        
        self.format_string(self, formatter)
        return self.PREFIX + self + self.SUFFIX

class CData(PreformattedString):

    PREFIX = u'<![CDATA['
    SUFFIX = u']]>'

class ProcessingInstruction(PreformattedString):

    PREFIX = u'<?'
    SUFFIX = u'?>'

class Comment(PreformattedString):

    PREFIX = u'<!--'
    SUFFIX = u'-->'


class Declaration(PreformattedString):
    PREFIX = u'<!'
    SUFFIX = u'!>'


class Doctype(PreformattedString):

    @classmethod
    def for_name_and_ids(cls, name, pub_id, system_id):
        value = name
        if pub_id is not None:
            value += ' PUBLIC "%s"' % pub_id
            if system_id is not None:
                value += ' "%s"' % system_id
        elif system_id is not None:
            value += ' SYSTEM "%s"' % system_id

        return Doctype(value)

    PREFIX = u'<!DOCTYPE '
    SUFFIX = u'>\n'


class Tag(PageElement):

    

    def __init__(self, parser=None, builder=None, name=None, namespace=None,
                 prefix=None, attrs=None, parent=None, previous=None):
        "Basic constructor."

        if parser is None:
            self.parser_class = None
        else:
            
            
            self.parser_class = parser.__class__
        if name is None:
            raise ValueError("No value provided for new tag's name.")
        self.name = name
        self.namespace = namespace
        self.prefix = prefix
        if attrs is None:
            attrs = {}
        elif builder.cdata_list_attributes:
            attrs = builder._replace_cdata_list_attribute_values(
                self.name, attrs)
        else:
            attrs = dict(attrs)
        self.attrs = attrs
        self.contents = []
        self.setup(parent, previous)
        self.hidden = False

        
        if builder is not None:
            builder.set_up_substitutions(self)
            self.can_be_empty_element = builder.can_be_empty_element(name)
        else:
            self.can_be_empty_element = False

    parserClass = _alias("parser_class")  

    @property
    def is_empty_element(self):
        
        return len(self.contents) == 0 and self.can_be_empty_element
    isSelfClosing = is_empty_element  

    @property
    def string(self):
        
        if len(self.contents) != 1:
            return None
        child = self.contents[0]
        if isinstance(child, NavigableString):
            return child
        return child.string

    @string.setter
    def string(self, string):
        self.clear()
        self.append(string.__class__(string))

    def _all_strings(self, strip=False):
        
        for descendant in self.descendants:
            if not isinstance(descendant, NavigableString):
                continue
            if strip:
                descendant = descendant.strip()
                if len(descendant) == 0:
                    continue
            yield descendant
    strings = property(_all_strings)

    @property
    def stripped_strings(self):
        for string in self._all_strings(True):
            yield string

    def get_text(self, separator=u"", strip=False):
        
        return separator.join([s for s in self._all_strings(strip)])
    getText = get_text
    text = property(get_text)

    def decompose(self):
        
        self.extract()
        i = self
        while i is not None:
            next = i.next_element
            i.__dict__.clear()
            i = next

    def clear(self, decompose=False):
        
        if decompose:
            for element in self.contents[:]:
                if isinstance(element, Tag):
                    element.decompose()
                else:
                    element.extract()
        else:
            for element in self.contents[:]:
                element.extract()

    def index(self, element):
        
        for i, child in enumerate(self.contents):
            if child is element:
                return i
        raise ValueError("Tag.index: element not in tag")

    def get(self, key, default=None):
        
        return self.attrs.get(key, default)

    def has_attr(self, key):
        return key in self.attrs

    def __hash__(self):
        return str(self).__hash__()

    def __getitem__(self, key):
        
        return self.attrs[key]

    def __iter__(self):
        "Iterating over a tag iterates over its contents."
        return iter(self.contents)

    def __len__(self):
        "The length of a tag is the length of its list of contents."
        return len(self.contents)

    def __contains__(self, x):
        return x in self.contents

    def __nonzero__(self):
        "A tag is non-None even if it has no contents."
        return True

    def __setitem__(self, key, value):
        
        self.attrs[key] = value

    def __delitem__(self, key):
        "Deleting tag[key] deletes all 'key' attributes for the tag."
        self.attrs.pop(key, None)

    def __call__(self, *args, **kwargs):
        
        return self.find_all(*args, **kwargs)

    def __getattr__(self, tag):
        
        if len(tag) > 3 and tag.endswith('Tag'):
            
            tag_name = tag[:-3]
            warnings.warn(
                '.%sTag is deprecated, use .find("%s") instead.' % (
                    tag_name, tag_name))
            return self.find(tag_name)
        
        elif not tag.startswith("__") and not tag=="contents":
            return self.find(tag)
        raise AttributeError(
            "'%s' object has no attribute '%s'" % (self.__class__, tag))

    def __eq__(self, other):
        
        if self is other:
            return True
        if (not hasattr(other, 'name') or
            not hasattr(other, 'attrs') or
            not hasattr(other, 'contents') or
            self.name != other.name or
            self.attrs != other.attrs or
            len(self) != len(other)):
            return False
        for i, my_child in enumerate(self.contents):
            if my_child != other.contents[i]:
                return False
        return True

    def __ne__(self, other):
        
        return not self == other

    def __repr__(self, encoding=DEFAULT_OUTPUT_ENCODING):
        
        return self.encode(encoding)

    def __unicode__(self):
        return self.decode()

    def __str__(self):
        return self.encode()

    if PY3K:
        __str__ = __repr__ = __unicode__

    def encode(self, encoding=DEFAULT_OUTPUT_ENCODING,
               indent_level=None, formatter="minimal",
               errors="xmlcharrefreplace"):
        
        
        u = self.decode(indent_level, encoding, formatter)
        return u.encode(encoding, errors)

    def decode(self, indent_level=None,
               eventual_encoding=DEFAULT_OUTPUT_ENCODING,
               formatter="minimal"):
        
        attrs = []
        if self.attrs:
            for key, val in sorted(self.attrs.items()):
                if val is None:
                    decoded = key
                else:
                    if isinstance(val, list) or isinstance(val, tuple):
                        val = ' '.join(val)
                    elif not isinstance(val, basestring):
                        val = unicode(val)
                    elif (
                        isinstance(val, AttributeValueWithCharsetSubstitution)
                        and eventual_encoding is not None):
                        val = val.encode(eventual_encoding)

                    text = self.format_string(val, formatter)
                    decoded = (
                        unicode(key) + '='
                        + EntitySubstitution.quoted_attribute_value(text))
                attrs.append(decoded)
        close = ''
        closeTag = ''

        prefix = ''
        if self.prefix:
            prefix = self.prefix + ":"

        if self.is_empty_element:
            close = '/'
        else:
            closeTag = '</%s%s>' % (prefix, self.name)

        pretty_print = (indent_level is not None)
        if pretty_print:
            space = (' ' * (indent_level - 1))
            indent_contents = indent_level + 1
        else:
            space = ''
            indent_contents = None
        contents = self.decode_contents(
            indent_contents, eventual_encoding, formatter)

        if self.hidden:
            
            s = contents
        else:
            s = []
            attribute_string = ''
            if attrs:
                attribute_string = ' ' + ' '.join(attrs)
            if pretty_print:
                s.append(space)
            s.append('<%s%s%s%s>' % (
                    prefix, self.name, attribute_string, close))
            if pretty_print:
                s.append("\n")
            s.append(contents)
            if pretty_print and contents and contents[-1] != "\n":
                s.append("\n")
            if pretty_print and closeTag:
                s.append(space)
            s.append(closeTag)
            if pretty_print and closeTag and self.next_sibling:
                s.append("\n")
            s = ''.join(s)
        return s

    def prettify(self, encoding=None, formatter="minimal"):
        if encoding is None:
            return self.decode(True, formatter=formatter)
        else:
            return self.encode(encoding, True, formatter=formatter)

    def decode_contents(self, indent_level=None,
                       eventual_encoding=DEFAULT_OUTPUT_ENCODING,
                       formatter="minimal"):
        
        pretty_print = (indent_level is not None)
        s = []
        for c in self:
            text = None
            if isinstance(c, NavigableString):
                text = c.output_ready(formatter)
            elif isinstance(c, Tag):
                s.append(c.decode(indent_level, eventual_encoding,
                                  formatter))
            if text and indent_level:
                text = text.strip()
            if text:
                if pretty_print:
                    s.append(" " * (indent_level - 1))
                s.append(text)
                if pretty_print:
                    s.append("\n")
        return ''.join(s)

    def encode_contents(
        self, indent_level=None, encoding=DEFAULT_OUTPUT_ENCODING,
        formatter="minimal"):
        
        contents = self.decode_contents(indent_level, encoding, formatter)
        return contents.encode(encoding)

    
    def renderContents(self, encoding=DEFAULT_OUTPUT_ENCODING,
                       prettyPrint=False, indentLevel=0):
        if not prettyPrint:
            indentLevel = None
        return self.encode_contents(
            indent_level=indentLevel, encoding=encoding)

    

    def find(self, name=None, attrs={}, recursive=True, text=None,
             **kwargs):
        
        r = None
        l = self.find_all(name, attrs, recursive, text, 1, **kwargs)
        if l:
            r = l[0]
        return r
    findChild = find

    def find_all(self, name=None, attrs={}, recursive=True, text=None,
                 limit=None, **kwargs):
        

        generator = self.descendants
        if not recursive:
            generator = self.children
        return self._find_all(name, attrs, text, limit, generator, **kwargs)
    findAll = find_all       
    findChildren = find_all  

    
    @property
    def children(self):
        
        return iter(self.contents)  

    @property
    def descendants(self):
        if not len(self.contents):
            return
        stopNode = self._last_descendant().next_element
        current = self.contents[0]
        while current is not stopNode:
            yield current
            current = current.next_element

    
    def childGenerator(self):
        return self.children

    def recursiveChildGenerator(self):
        return self.descendants

    
    
    
    has_key = has_attr


class SoupStrainer(object):
    

    def __init__(self, name=None, attrs={}, text=None, **kwargs):
        self.name = self._normalize_search_value(name)
        if not isinstance(attrs, dict):
            
            
            kwargs['class'] = attrs
            attrs = None

        if 'class_' in kwargs:
            
            
            kwargs['class'] = kwargs['class_']
            del kwargs['class_']

        if kwargs:
            if attrs:
                attrs = attrs.copy()
                attrs.update(kwargs)
            else:
                attrs = kwargs
        normalized_attrs = {}
        for key, value in attrs.items():
            normalized_attrs[key] = self._normalize_search_value(value)

        self.attrs = normalized_attrs
        self.text = self._normalize_search_value(text)

    def _normalize_search_value(self, value):
        
        
        if (isinstance(value, unicode) or callable(value) or hasattr(value, 'match')
            or isinstance(value, bool) or value is None):
            return value

        
        if isinstance(value, bytes):
            return value.decode("utf8")

        
        if hasattr(value, '__iter__'):
            new_value = []
            for v in value:
                if (hasattr(v, '__iter__') and not isinstance(v, bytes)
                    and not isinstance(v, unicode)):
                    
                    
                    
                    new_value.append(v)
                else:
                    new_value.append(self._normalize_search_value(v))
            return new_value

        
        
        
        return unicode(str(value))

    def __str__(self):
        if self.text:
            return self.text
        else:
            return "%s|%s" % (self.name, self.attrs)

    def search_tag(self, markup_name=None, markup_attrs={}):
        found = None
        markup = None
        if isinstance(markup_name, Tag):
            markup = markup_name
            markup_attrs = markup
        call_function_with_tag_data = (
            isinstance(self.name, collections.Callable)
            and not isinstance(markup_name, Tag))

        if ((not self.name)
            or call_function_with_tag_data
            or (markup and self._matches(markup, self.name))
            or (not markup and self._matches(markup_name, self.name))):
            if call_function_with_tag_data:
                match = self.name(markup_name, markup_attrs)
            else:
                match = True
                markup_attr_map = None
                for attr, match_against in list(self.attrs.items()):
                    if not markup_attr_map:
                        if hasattr(markup_attrs, 'get'):
                            markup_attr_map = markup_attrs
                        else:
                            markup_attr_map = {}
                            for k, v in markup_attrs:
                                markup_attr_map[k] = v
                    attr_value = markup_attr_map.get(attr)
                    if not self._matches(attr_value, match_against):
                        match = False
                        break
            if match:
                if markup:
                    found = markup
                else:
                    found = markup_name
        if found and self.text and not self._matches(found.string, self.text):
            found = None
        return found
    searchTag = search_tag

    def search(self, markup):
        
        found = None
        
        
        if hasattr(markup, '__iter__') and not isinstance(markup, (Tag, basestring)):
            for element in markup:
                if isinstance(element, NavigableString) \
                       and self.search(element):
                    found = element
                    break
        
        
        elif isinstance(markup, Tag):
            if not self.text or self.name or self.attrs:
                found = self.search_tag(markup)
        
        elif isinstance(markup, NavigableString) or \
                 isinstance(markup, basestring):
            if not self.name and not self.attrs and self._matches(markup, self.text):
                found = markup
        else:
            raise Exception(
                "I don't know how to match against a %s" % markup.__class__)
        return found

    def _matches(self, markup, match_against):
        
        result = False
        if isinstance(markup, list) or isinstance(markup, tuple):
            
            
            if (isinstance(match_against, unicode)
                and ' ' in match_against):
                
                
                
                
                
                
                
                return (whitespace_re.split(match_against) == markup)
            else:
                for item in markup:
                    if self._matches(item, match_against):
                        return True
                return False

        if match_against is True:
            
            return markup is not None

        if isinstance(match_against, collections.Callable):
            return match_against(markup)

        
        
        if isinstance(markup, Tag):
            markup = markup.name

        
        markup = self._normalize_search_value(markup)

        if markup is None:
            
            return not match_against

        if isinstance(match_against, unicode):
            
            return markup == match_against

        if hasattr(match_against, 'match'):
            
            return match_against.search(markup)

        if hasattr(match_against, '__iter__'):
            
            
            return markup in match_against


class ResultSet(list):
    
    def __init__(self, source):
        list.__init__([])
        self.source = source
