

































from __future__ import with_statement

import sys
import codecs
from datetime import datetime
from os.path import dirname, basename, splitext, join

import sqlite3 as sqlite

try:
    import simstring
except ImportError:
    errorstr = 
    print >> sys.stderr, errorstr
    sys.exit(1)


DEFAULT_INPUT_ENCODING = 'UTF-8'



NORM_DB_STRING = 'NORM_DB_VERSION'
NORM_DB_VERSION = '1.0.1'


SQL_DB_FILENAME_EXTENSION = 'db'


SS_DB_FILENAME_EXTENSION = 'ss.db'


DEFAULT_NGRAM_LENGTH = 3


DEFAULT_INCLUDE_MARKS = False


MAX_ERROR_LINES = 100


TYPE_VALUES = ["name", "attr", "info"]


TABLE_FOR_TYPE = {
    "name" : "names",
    "attr" : "attributes",
    "info" : "infos",
}


TABLE_HAS_NORMVALUE = {
    "names" : True,
    "attributes" : True,
    "infos" : False,
}


assert set(TYPE_VALUES) == set(TABLE_FOR_TYPE.keys())
assert set(TABLE_FOR_TYPE.values()) == set(TABLE_HAS_NORMVALUE.keys())


CREATE_TABLE_COMMANDS = [
,
,
,
,
,
]
CREATE_INDEX_COMMANDS = [
"CREATE INDEX entities_uid ON entities (uid);",
"CREATE INDEX names_value ON names (value);",
"CREATE INDEX names_normvalue ON names (normvalue);",
"CREATE INDEX names_entity_id ON names (entity_id);",
"CREATE INDEX attributes_value ON attributes (value);",
"CREATE INDEX attributes_normvalue ON attributes (normvalue);",
"CREATE INDEX attributes_entity_id ON attributes (entity_id);",

"CREATE INDEX infos_entity_id ON infos (entity_id);",
]



SELECT_SIMSTRING_STRINGS_COMMAND = 









def string_norm_form(s):
    return s.lower().strip().replace('-', ' ')

def default_db_dir():
    
    

    
    sys.path.append(join(dirname(__file__), '..'))
    try:
        from config import WORK_DIR
        return WORK_DIR
    except ImportError:
        print >> sys.stderr, "Warning: failed to determine brat work directory, using current instead."
        return "."

def argparser():
    import argparse

    ap=argparse.ArgumentParser(description="Create normalization DBs for given file")
    ap.add_argument("-v", "--verbose", default=False, action="store_true", help="Verbose output")
    ap.add_argument("-d", "--database", default=None, help="Base name of databases to create (default by input file name in brat work directory)")
    ap.add_argument("-e", "--encoding", default=DEFAULT_INPUT_ENCODING, help="Input text encoding (default "+DEFAULT_INPUT_ENCODING+")")
    ap.add_argument("file", metavar="FILE", help="Normalization data")
    return ap

def sqldb_filename(dbname):
    
    return join(default_db_dir(), dbname+'.'+SQL_DB_FILENAME_EXTENSION)

def ssdb_filename(dbname):
    
    return join(default_db_dir(), dbname+'.'+SS_DB_FILENAME_EXTENSION)

def main(argv):
    arg = argparser().parse_args(argv[1:])

    
    assert DEFAULT_NGRAM_LENGTH == 3, "Error: unsupported n-gram length"
    assert DEFAULT_INCLUDE_MARKS == False, "Error: begin/end marks not supported"

    infn = arg.file

    if arg.database is None:
        
        bn = splitext(basename(infn))[0]
        sqldbfn = sqldb_filename(bn)
        ssdbfn = ssdb_filename(bn)
    else:
        sqldbfn = arg.database+'.'+SQL_DB_FILENAME_EXTENSION
        ssdbfn = arg.database+'.'+SS_DB_FILENAME_EXTENSION

    if arg.verbose:
        print >> sys.stderr, "Storing SQL DB as %s and" % sqldbfn
        print >> sys.stderr, "  simstring DB as %s" % ssdbfn
    start_time = datetime.now()

    import_count, duplicate_count, error_count, simstring_count = 0, 0, 0, 0

    with codecs.open(infn, 'rU', encoding=arg.encoding) as inf:        

        
        try:
            connection = sqlite.connect(sqldbfn)
        except sqlite.OperationalError, e:
            print >> sys.stderr, "Error connecting to DB %s:" % sqldbfn, e
            return 1
        cursor = connection.cursor()

        
        if arg.verbose:
            print >> sys.stderr, "Creating tables ...",

        for command in CREATE_TABLE_COMMANDS:
            try:
                cursor.execute(command)
            except sqlite.OperationalError, e:
                print >> sys.stderr, "Error creating %s:" % sqldbfn, e, "(DB exists?)"
                return 1

        
        if arg.verbose:
            print >> sys.stderr, "done."
            print >> sys.stderr, "Importing data ...",

        next_eid = 1
        label_id = {}
        next_lid = 1
        next_pid = dict([(t,1) for t in TYPE_VALUES])

        for i, l in enumerate(inf):
            l = l.rstrip('\n')

            
            try:
                id_, rest = l.split('\t', 1)
            except ValueError:
                if error_count < MAX_ERROR_LINES:
                    print >> sys.stderr, "Error: skipping line %d: expected tab-separated fields, got '%s'" % (i+1, l)
                elif error_count == MAX_ERROR_LINES:
                    print >> sys.stderr, "(Too many errors; suppressing further error messages)"
                error_count += 1
                continue

            
            try:
                triples = []
                for triple in rest.split('\t'):
                    type_, label, string = triple.split(':', 2)
                    if type_ not in TYPE_VALUES:
                        print >> sys.stderr, "Unknown TYPE %s" % type_
                    triples.append((type_, label, string))
            except ValueError:
                if error_count < MAX_ERROR_LINES:
                    print >> sys.stderr, "Error: skipping line %d: expected tab-separated TYPE:LABEL:STRING triples, got '%s'" % (i+1, rest)
                elif error_count == MAX_ERROR_LINES:
                    print >> sys.stderr, "(Too many errors; suppressing further error messages)"
                error_count += 1
                continue

            
            eid = next_eid
            next_eid += 1
            try:
                cursor.execute("INSERT into entities VALUES (?, ?)", (eid, id_))
            except sqlite.IntegrityError, e:
                if error_count < MAX_ERROR_LINES:
                    print >> sys.stderr, "Error inserting %s (skipping): %s" % (id_, e)
                elif error_count == MAX_ERROR_LINES:
                    print >> sys.stderr, "(Too many errors; suppressing further error messages)"
                error_count += 1
                continue

            
            labels = set([l for t,l,s in triples])
            new_labels = [l for l in labels if l not in label_id]
            for label in new_labels:
                lid = next_lid
                next_lid += 1
                cursor.execute("INSERT into labels VALUES (?, ?)", (lid, label))
                label_id[label] = lid

            
            for type_, label, string in triples:
                table = TABLE_FOR_TYPE[type_]
                pid = next_pid[type_]
                next_pid[type_] += 1
                lid = label_id[label] 
                if TABLE_HAS_NORMVALUE[table]:
                    normstring = string_norm_form(string)
                    cursor.execute("INSERT into %s VALUES (?, ?, ?, ?, ?)" % table,
                                   (pid, eid, lid, string, normstring))
                else:
                    cursor.execute("INSERT into %s VALUES (?, ?, ?, ?)" % table,
                                   (pid, eid, lid, string))

            import_count += 1

            if arg.verbose and (i+1)%10000 == 0:
                print >> sys.stderr, '.',

        if arg.verbose:
            print >> sys.stderr, "done."

        
        if arg.verbose:
            print >> sys.stderr, "Creating indices ...",

        for command in CREATE_INDEX_COMMANDS:
            try:
                cursor.execute(command)
            except sqlite.OperationalError, e:
                print >> sys.stderr, "Error creating index", e
                return 1

        if arg.verbose:
            print >> sys.stderr, "done."

        
        connection.commit()

        
        if arg.verbose:
            print >> sys.stderr, "Creating simstring DB ...",
        
        try:
            ssdb = simstring.writer(ssdbfn)
            for row in cursor.execute(SELECT_SIMSTRING_STRINGS_COMMAND):
                
                s = row[0].encode('utf-8')
                ssdb.insert(s)
                simstring_count += 1
            ssdb.close()
        except:
            print >> sys.stderr, "Error building simstring DB"
            raise

        if arg.verbose:
            print >> sys.stderr, "done."

        cursor.close()

    
    delta = datetime.now() - start_time

    if arg.verbose:
        print >> sys.stderr
        print >> sys.stderr, "Done in:", str(delta.seconds)+"."+str(delta.microseconds/10000), "seconds"
    
    print "Done, imported %d entries (%d strings), skipped %d duplicate keys, skipped %d invalid lines" % (import_count, simstring_count, duplicate_count, error_count)

    return 0
    
if __name__ == "__main__":
    sys.exit(main(sys.argv))
