
import sys
from optparse import OptionParser
import os


WSCRIPT_TEMPLATE = 



MODEL_CC_TEMPLATE = 



MODEL_H_TEMPLATE = 



HELPER_CC_TEMPLATE = 



HELPER_H_TEMPLATE = 


EXAMPLES_WSCRIPT_TEMPLATE = 

EXAMPLE_CC_TEMPLATE = 


TEST_CC_TEMPLATE = 


def main(argv):
    parser = OptionParser(usage=("Usage: %prog [options] modulename\n"
                                 "Utility script to create a basic template for a new ns-3 module"))
    (options, args) = parser.parse_args()
    if len(args) != 1:
        parser.print_help()
        return 1

    modname = args[0]
    assert os.path.sep not in modname

    moduledir = os.path.join(os.path.dirname(__file__), modname)

    if os.path.exists(moduledir):
        print >> sys.stderr, "Module %r already exists" % (modname,)
        return 2

    os.mkdir(moduledir)
    wscript = file(os.path.join(moduledir, "wscript"), "wt")
    wscript.write(WSCRIPT_TEMPLATE % dict(MODULE=modname))
    wscript.close()


    
    
    
    modeldir = os.path.join(moduledir, "model")
    os.mkdir(modeldir)

    model_cc = file(os.path.join(moduledir, "model", "%s.cc" % modname), "wt")
    model_cc.write(MODEL_CC_TEMPLATE % dict(MODULE=modname))
    model_cc.close()

    model_h = file(os.path.join(moduledir, "model", "%s.h" % modname), "wt")
    model_h.write(MODEL_H_TEMPLATE % dict(MODULE=modname, INCLUDE_GUARD="__%s_H__" % (modname.upper()),))
    model_h.close()



    
    
    
    testdir = os.path.join(moduledir, "test")
    os.mkdir(testdir)
    test_cc = file(os.path.join(moduledir, "test", "%s-test-suite.cc" % modname), "wt")
    test_cc.write(TEST_CC_TEMPLATE % dict(MODULE=modname,CAPITALIZED=modname.capitalize()))
    test_cc.close()



    
    
    
    helperdir = os.path.join(moduledir, "helper")
    os.mkdir(helperdir)

    helper_cc = file(os.path.join(moduledir, "helper", "%s-helper.cc" % modname), "wt")
    helper_cc.write(HELPER_CC_TEMPLATE % dict(MODULE=modname))
    helper_cc.close()

    helper_h = file(os.path.join(moduledir, "helper", "%s-helper.h" % modname), "wt")
    helper_h.write(HELPER_H_TEMPLATE % dict(MODULE=modname, INCLUDE_GUARD="__%s_HELPER_H__" % (modname.upper()),))
    helper_h.close()


    examplesdir = os.path.join(moduledir, "examples")
    os.mkdir(examplesdir)

    examples_wscript = file(os.path.join(examplesdir, "wscript"), "wt")
    examples_wscript.write(EXAMPLES_WSCRIPT_TEMPLATE % dict(MODULE=modname))
    examples_wscript.close()

    example_cc = file(os.path.join(moduledir, "examples", "%s-example.cc" % modname), "wt")
    example_cc.write(EXAMPLE_CC_TEMPLATE % dict(MODULE=modname))
    example_cc.close()


    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
