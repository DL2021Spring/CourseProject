

import sys
import os.path

import pybindgen.settings
from pybindgen.gccxmlparser import ModuleParser, PygenClassifier, PygenSection, WrapperWarning, find_declaration_from_name
from pybindgen.typehandlers.codesink import FileCodeSink
from pygccxml.declarations import templates
from pygccxml.declarations.enumeration import enumeration_t
from pygccxml.declarations.class_declaration import class_t
from pygccxml.declarations.calldef import free_function_t, member_function_t, constructor_t, calldef_t




import ns3modulegen_core_customizations




class ErrorHandler(pybindgen.settings.ErrorHandler):
    def handle_error(self, dummy_wrapper, dummy_exception, dummy_traceback_):
        return True
pybindgen.settings.error_handler = ErrorHandler()
import warnings
warnings.filterwarnings(category=WrapperWarning, action='ignore')


import ns3modulescan
type_annotations = ns3modulescan.type_annotations


def get_ns3_relative_path(path):
    l = []
    head = path
    while head:
        new_head, tail = os.path.split(head)
        if new_head == head:
            raise ValueError
        head = new_head
        if tail == 'ns3':
            return os.path.join(*l)
        l.insert(0, tail)
    raise AssertionError("is the path %r inside ns3?!" % path)

class PreScanHook:

    def __init__(self, headers_map, module):
        self.headers_map = headers_map
        self.module = module

    def __call__(self, module_parser,
                 pygccxml_definition,
                 global_annotations,
                 parameter_annotations):
        try:
            ns3_header = get_ns3_relative_path(pygccxml_definition.location.file_name)
        except ValueError: 
            return 

        definition_module = self.headers_map[ns3_header]

        
        
        
        

        
        
        global_annotations['pygen_comment'] = "%s (module %r): %s" % \
            (ns3_header, definition_module, pygccxml_definition)


        
        
        
        if isinstance(pygccxml_definition, member_function_t) \
                and pygccxml_definition.parent.name == 'Object' \
                and pygccxml_definition.name == 'GetObject':
            template_args = templates.args(pygccxml_definition.demangled_name)
            if template_args == ['ns3::Object']:
                global_annotations['template_instance_names'] = 'ns3::Object=>GetObject'

        
        if isinstance(pygccxml_definition, member_function_t) \
                and pygccxml_definition.parent.name == 'Simulator' \
                and pygccxml_definition.name.startswith('Schedule'):
            global_annotations['ignore'] = None

        
        if isinstance(pygccxml_definition, member_function_t) \
                and pygccxml_definition.parent.name == 'Simulator' \
                and pygccxml_definition.name == 'Run':
            global_annotations['ignore'] = True

        
        if isinstance(pygccxml_definition, calldef_t):
            for arg in pygccxml_definition.arguments:
                if arg.default_value is None:
                    continue
                elif arg.default_value == "ns3::MilliSeconds( )":
                    arg.default_value = "ns3::MilliSeconds(0)"
                elif arg.default_value == "ns3::Seconds( )":
                    arg.default_value = "ns3::Seconds(0)"

        
        if isinstance(pygccxml_definition, class_t):
            print >> sys.stderr, pygccxml_definition
            
            
            

            
            
            
            
            
            
            if templates.is_instantiation(pygccxml_definition.decl_string):
                cls_name, template_parameters = templates.split(pygccxml_definition.name)
                template_parameters_decls = [find_declaration_from_name(module_parser.global_ns, templ_param)
                                             for templ_param in template_parameters]
                
                
                template_parameters_modules = []
                for templ in template_parameters_decls:
                    if not hasattr(templ, 'location'):
                        continue
                    try:
                        h = get_ns3_relative_path(templ.location.file_name)
                    except ValueError:
                        continue
                    template_parameters_modules.append(self.headers_map[h])

                for templ_mod in template_parameters_modules:
                    if templ_mod == self.module:
                        definition_module = templ_mod
                        break
                


            if definition_module != self.module:
                global_annotations['import_from_module'] = 'ns.%s' % (definition_module.replace('-', '_'),)

            if pygccxml_definition.decl_string.startswith('::ns3::SimpleRefCount<'):
                global_annotations['incref_method'] = 'Ref'
                global_annotations['decref_method'] = 'Unref'
                global_annotations['peekref_method'] = 'GetReferenceCount'
                global_annotations['automatic_type_narrowing'] = 'true'
                return

            if pygccxml_definition.decl_string.startswith('::ns3::Callback<'):
                
                global_annotations['ignore'] = None
                return

            if pygccxml_definition.decl_string.startswith('::ns3::TracedCallback<'):
                global_annotations['ignore'] = None
                return

            if pygccxml_definition.decl_string.startswith('::ns3::Ptr<'):
                
                global_annotations['ignore'] = None
                return

            
            try:
                annotations = type_annotations[pygccxml_definition.decl_string]
            except KeyError:
                pass
            else:
                global_annotations.update(annotations)

        
        if isinstance(pygccxml_definition, enumeration_t):
            if definition_module != self.module:
                global_annotations['import_from_module'] = 'ns.%s' % definition_module

        
        if isinstance(pygccxml_definition, free_function_t):

            if definition_module != self.module:
                global_annotations['ignore'] = None
                return

            if pygccxml_definition.name == 'PeekPointer':
                global_annotations['ignore'] = None
                return

        
        if isinstance(pygccxml_definition, (free_function_t, member_function_t, constructor_t)):
            try:
                annotations = type_annotations[str(pygccxml_definition)]
            except KeyError:
                pass
            else:
                for key,value in annotations.items():
                    if key == 'params':
                        parameter_annotations.update (value)
                        del annotations['params']
                global_annotations.update(annotations)










def scan_callback_classes(module_parser, callback_classes_file):
    callback_classes_file.write("callback_classes = [\n")
    for cls in module_parser.module_namespace.classes(function=module_parser.location_filter,
                                                      recursive=False):
        if not cls.name.startswith("Callback<"):
            continue
        assert templates.is_instantiation(cls.decl_string), "%s is not a template instantiation" % cls
        dummy_cls_name, template_parameters = templates.split(cls.decl_string)
        callback_classes_file.write("    %r,\n" % template_parameters)
    callback_classes_file.write("]\n")


def ns3_module_scan(top_builddir, module_name, headers_map, output_file_name, cflags):
    module_parser = ModuleParser('ns.%s' % module_name.replace('-', '_'), 'ns3')
    module_parser.add_pre_scan_hook(PreScanHook(headers_map, module_name))
    

    gccxml_options = dict(
        include_paths=[top_builddir],
         define_symbols={
            
            
            },
        cflags=('--gccxml-cxxflags "%s -DPYTHON_SCAN"' % cflags)
        )

    try:
        os.unlink(output_file_name)
    except OSError:
        pass
    try:
        os.makedirs(os.path.dirname(output_file_name))
    except OSError:
        pass
    output_file = open(output_file_name, "wt")
    output_sink = FileCodeSink(output_file)

    
    
    scan_header = os.path.join(os.path.dirname(output_file_name), "scan-header.h")
    if not os.path.exists(scan_header):
        scan_header = os.path.join(top_builddir, "ns3", "%s-module.h" % module_name)

    module_parser.parse_init([scan_header],
                             None, whitelist_paths=[top_builddir],
                             
                             pygen_sink=output_sink,
                             gccxml_options=gccxml_options)
    module_parser.scan_types()

    callback_classes_file = open(os.path.join(os.path.dirname(output_file_name), "callbacks_list.py"), "wt")
    scan_callback_classes(module_parser, callback_classes_file)
    callback_classes_file.close()


    module_parser.scan_methods()
    module_parser.scan_functions()
    module_parser.parse_finalize()

    output_file.close()
    os.chmod(output_file_name, 0400)


if __name__ == '__main__':
    if len(sys.argv) != 6:
        print "ns3modulescan-modular.py top_builddir module_path module_headers output_file_name cflags"
        sys.exit(1)
    ns3_module_scan(sys.argv[1], sys.argv[2], eval(sys.argv[3]), sys.argv[4], sys.argv[5])
    sys.exit(0)
