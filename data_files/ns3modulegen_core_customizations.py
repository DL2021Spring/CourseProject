import re

from pybindgen.typehandlers import base as typehandlers
from pybindgen import ReturnValue, Parameter
from pybindgen.cppmethod import CustomCppMethodWrapper, CustomCppConstructorWrapper
from pybindgen.typehandlers.codesink import MemoryCodeSink
from pybindgen.typehandlers import ctypeparser
from pybindgen import cppclass
import warnings

from pybindgen.typehandlers.base import CodeGenerationError

import sys

class SmartPointerTransformation(typehandlers.TypeTransformation):
    
    def __init__(self):
        super(SmartPointerTransformation, self).__init__()
        self.rx = re.compile(r'(ns3::|::ns3::|)Ptr<([^>]+)>\s*$')

    def _get_untransformed_type_traits(self, name):
        m = self.rx.match(name)
        is_const = False
        if m is None:
            return None, False
        else:
            name1 = m.group(2).strip()
            if name1.startswith('const '):
                name1 = name1[len('const '):]
                is_const = True
            if name1.endswith(' const'):
                name1 = name1[:-len(' const')]
                is_const = True
            new_name = name1+' *'

            if new_name.startswith('::'):
                new_name = new_name[2:]
            return new_name, is_const

    def get_untransformed_name(self, name):
        new_name, dummy_is_const = self._get_untransformed_type_traits(name)
        return new_name

    def create_type_handler(self, type_handler, *args, **kwargs):
        if issubclass(type_handler, Parameter):
            kwargs['transfer_ownership'] = False
        elif issubclass(type_handler, ReturnValue):
            kwargs['caller_owns_return'] = False
        else:
            raise AssertionError

        
        orig_ctype, is_const = self._get_untransformed_type_traits(args[0])
        if is_const:
            correct_ctype = 'ns3::Ptr< %s const >' % orig_ctype[:-2]
        else:
            correct_ctype = 'ns3::Ptr< %s >' % orig_ctype[:-2]
        args = tuple([correct_ctype] + list(args[1:]))

        handler = type_handler(*args, **kwargs)
        handler.set_tranformation(self, orig_ctype)
        return handler

    def untransform(self, type_handler, declarations, code_block, expression):
        return 'const_cast<%s> (ns3::PeekPointer (%s))' % (type_handler.untransformed_ctype, expression)

    def transform(self, type_handler, declarations, code_block, expression):
        assert type_handler.untransformed_ctype[-1] == '*'
        return 'ns3::Ptr< %s > (%s)' % (type_handler.untransformed_ctype[:-1], expression)


transf = SmartPointerTransformation()
typehandlers.return_type_matcher.register_transformation(transf)
typehandlers.param_type_matcher.register_transformation(transf)
del transf


class ArgvParam(Parameter):
    

    DIRECTIONS = [Parameter.DIRECTION_IN]
    CTYPES = []
    
    def convert_c_to_python(self, wrapper):
        raise NotImplementedError

    def convert_python_to_c(self, wrapper):
        py_name = wrapper.declarations.declare_variable('PyObject*', 'py_' + self.name)
        argc_var = wrapper.declarations.declare_variable('int', 'argc')
        name = wrapper.declarations.declare_variable('char**', self.name)
        idx = wrapper.declarations.declare_variable('Py_ssize_t', 'idx')
        wrapper.parse_params.add_parameter('O!', ['&PyList_Type', '&'+py_name], self.name)

        

        wrapper.before_call.write_code("%s = (char **) malloc(sizeof(char*)*PyList_Size(%s));"
                                       % (name, py_name))
        wrapper.before_call.add_cleanup_code('free(%s);' % name)
        wrapper.before_call.write_code( % vars())
        wrapper.before_call.sink.indent()
        wrapper.before_call.write_code( % vars())
        
        wrapper.before_call.write_error_check(
            '!PyString_Check(item)',
            failure_cleanup=('PyErr_SetString(PyExc_TypeError, '
                             '"argument %s must be a list of strings");') % self.name)
        wrapper.before_call.write_code(
            '%s[%s] = PyString_AsString(item);' % (name, idx))
        wrapper.before_call.sink.unindent()
        wrapper.before_call.write_code('}')
        wrapper.before_call.write_code('%s = PyList_Size(%s);' % (argc_var, py_name))
        
        wrapper.call_params.append(argc_var)
        wrapper.call_params.append(name)


class CallbackImplProxyMethod(typehandlers.ReverseWrapperBase):
    

    def __init__(self, return_value, parameters):
        super(CallbackImplProxyMethod, self).__init__(return_value, parameters)

    def generate_python_call(self):
        
        build_params = self.build_params.get_parameters(force_tuple_creation=True)
        if build_params[0][0] == '"':
            build_params[0] = '(char *) ' + build_params[0]
        args = self.before_call.declare_variable('PyObject*', 'args')
        self.before_call.write_code('%s = Py_BuildValue(%s);'
                                    % (args, ', '.join(build_params)))
        self.before_call.add_cleanup_code('Py_DECREF(%s);' % args)
        self.before_call.write_code('py_retval = PyObject_CallObject(m_callback, %s);' % args)
        self.before_call.write_error_check('py_retval == NULL')
        self.before_call.add_cleanup_code('Py_DECREF(py_retval);')




def generate_callback_classes(out, callbacks):
    for callback_impl_num, template_parameters in enumerate(callbacks):
        sink = MemoryCodeSink()
        cls_name = "ns3::Callback< %s >" % ', '.join(template_parameters)
        
        class_name = "PythonCallbackImpl%i" % callback_impl_num
        sink.writeln( % (class_name, ', '.join(template_parameters), class_name, class_name, class_name, class_name))
        sink.indent()
        callback_return = template_parameters[0]
        return_ctype = ctypeparser.parse_type(callback_return)
        if ('const' in return_ctype.remove_modifiers()):
            kwargs = {'is_const': True}
        else:
            kwargs = {}
        try:
            return_type = ReturnValue.new(str(return_ctype), **kwargs)
        except (typehandlers.TypeLookupError, typehandlers.TypeConfigurationError), ex:
            warnings.warn("***** Unable to register callback; Return value '%s' error (used in %s): %r"
                          % (callback_return, cls_name, ex),
                          Warning)
            continue

        arguments = []
        ok = True
        callback_parameters = [arg for arg in template_parameters[1:] if arg != 'ns3::empty']
        for arg_num, arg_type in enumerate(callback_parameters):
            arg_name = 'arg%i' % (arg_num+1)

            param_ctype = ctypeparser.parse_type(arg_type)
            if ('const' in param_ctype.remove_modifiers()):
                kwargs = {'is_const': True}
            else:
                kwargs = {}
            try:
                arguments.append(Parameter.new(str(param_ctype), arg_name, **kwargs))
            except (typehandlers.TypeLookupError, typehandlers.TypeConfigurationError), ex:
                warnings.warn("***** Unable to register callback; parameter '%s %s' error (used in %s): %r"
                              % (arg_type, arg_name, cls_name, ex),
                              Warning)
                ok = False
        if not ok:
            continue

        wrapper = CallbackImplProxyMethod(return_type, arguments)
        wrapper.generate(sink, 'operator()', decl_modifiers=[])
            
        sink.unindent()
        sink.writeln('};\n')
        sink.flush_to(out)
        
        class PythonCallbackParameter(Parameter):
            "Class handlers"
            CTYPES = [cls_name]
            print >> sys.stderr, "***** registering callback handler: %r" % ctypeparser.normalize_type_string(cls_name)
            DIRECTIONS = [Parameter.DIRECTION_IN]
            PYTHON_CALLBACK_IMPL_NAME = class_name
            TEMPLATE_ARGS = template_parameters

            def convert_python_to_c(self, wrapper):
                "parses python args to get C++ value"
                assert isinstance(wrapper, typehandlers.ForwardWrapperBase)

                if self.default_value is None:
                    py_callback = wrapper.declarations.declare_variable('PyObject*', self.name)
                    wrapper.parse_params.add_parameter('O', ['&'+py_callback], self.name)
                    wrapper.before_call.write_error_check(
                        '!PyCallable_Check(%s)' % py_callback,
                        'PyErr_SetString(PyExc_TypeError, "parameter \'%s\' must be callbale");' % self.name)
                    callback_impl = wrapper.declarations.declare_variable(
                        'ns3::Ptr<%s>' % self.PYTHON_CALLBACK_IMPL_NAME,
                        '%s_cb_impl' % self.name)
                    wrapper.before_call.write_code("%s = ns3::Create<%s> (%s);"
                                                   % (callback_impl, self.PYTHON_CALLBACK_IMPL_NAME, py_callback))
                    wrapper.call_params.append(
                        'ns3::Callback<%s> (%s)' % (', '.join(self.TEMPLATE_ARGS), callback_impl))
                else:
                    py_callback = wrapper.declarations.declare_variable('PyObject*', self.name, 'NULL')
                    wrapper.parse_params.add_parameter('O', ['&'+py_callback], self.name, optional=True)
                    value = wrapper.declarations.declare_variable(
                        'ns3::Callback<%s>' % ', '.join(self.TEMPLATE_ARGS),
                        self.name+'_value',
                        self.default_value)

                    wrapper.before_call.write_code("if (%s) {" % (py_callback,))
                    wrapper.before_call.indent()

                    wrapper.before_call.write_error_check(
                        '!PyCallable_Check(%s)' % py_callback,
                        'PyErr_SetString(PyExc_TypeError, "parameter \'%s\' must be callbale");' % self.name)

                    wrapper.before_call.write_code("%s = ns3::Callback<%s> (ns3::Create<%s> (%s));"
                                                   % (value, ', '.join(self.TEMPLATE_ARGS),
                                                      self.PYTHON_CALLBACK_IMPL_NAME, py_callback))

                    wrapper.before_call.unindent()
                    wrapper.before_call.write_code("}") 
                                        
                    wrapper.call_params.append(value)
                    

            def convert_c_to_python(self, wrapper):
                raise typehandlers.NotSupportedError("Reverse wrappers for ns3::Callback<...> types "
                                                     "(python using callbacks defined in C++) not implemented.")








def Simulator_customizations(module):
    Simulator = module['ns3::Simulator']

    
    Simulator.add_custom_method_wrapper("Schedule", "_wrap_Simulator_Schedule",
                                        flags=["METH_VARARGS", "METH_KEYWORDS", "METH_STATIC"])


    
    Simulator.add_custom_method_wrapper("ScheduleNow", "_wrap_Simulator_ScheduleNow",
                                        flags=["METH_VARARGS", "METH_KEYWORDS", "METH_STATIC"])


    
    Simulator.add_custom_method_wrapper("ScheduleDestroy", "_wrap_Simulator_ScheduleDestroy",
                                        flags=["METH_VARARGS", "METH_KEYWORDS", "METH_STATIC"])

    Simulator.add_custom_method_wrapper("Run", "_wrap_Simulator_Run",
                                        flags=["METH_VARARGS", "METH_KEYWORDS", "METH_STATIC"])


def CommandLine_customizations(module):
    CommandLine = module['ns3::CommandLine']
    CommandLine.add_method('Parse', None, [ArgvParam(None, 'argv')],
                           is_static=False)
    CommandLine.add_custom_method_wrapper("AddValue", "_wrap_CommandLine_AddValue",
                                          flags=["METH_VARARGS", "METH_KEYWORDS"])


def Object_customizations(module):
    
    
    
    
    
    
    try:
        Object = module['ns3::Object']
    except KeyError:
        return

    
    def helper_class_hook(helper_class):
        decl =   % (helper_class.name, helper_class.class_.full_name)

        helper_class.add_custom_method(decl)
        helper_class.add_post_generation_code(
            "NS_OBJECT_ENSURE_REGISTERED (%s);" % helper_class.name)
    Object.add_helper_class_hook(helper_class_hook)

    def ns3_object_instance_creation_function(cpp_class, code_block, lvalue,
                                              parameters, construct_type_name):
        assert lvalue
        assert not lvalue.startswith('None')
        if cpp_class.cannot_be_constructed:
            raise CodeGenerationError("%s cannot be constructed (%s)"
                                      % cpp_class.full_name)
        if cpp_class.incomplete_type:
            raise CodeGenerationError("%s cannot be constructed (incomplete type)"
                                      % cpp_class.full_name)
        code_block.write_code("%s = new %s(%s);" % (lvalue, construct_type_name, parameters))
        code_block.write_code("%s->Ref ();" % (lvalue))

    def ns3_object_post_instance_creation_function(cpp_class, code_block, lvalue,
                                                   parameters, construct_type_name):
        code_block.write_code("ns3::CompleteConstruct(%s);" % (lvalue, ))

    Object.set_instance_creation_function(ns3_object_instance_creation_function)
    Object.set_post_instance_creation_function(ns3_object_post_instance_creation_function)


def Attribute_customizations(module):
    
    

    
    
    
    

    
    
    

    for cls in module.classes:
        for meth in cls.get_all_methods():
            for param in meth.parameters:
                if isinstance(param, cppclass.CppClassRefParameter):
                    if param.cpp_class.name == 'AttributeValue' \
                            and param.default_value is not None \
                            and param.default_value_type is None:
                        param.default_value_type = 'ns3::EmptyAttributeValue'


def TypeId_customizations(module):
    TypeId = module['ns3::TypeId']
    TypeId.add_custom_method_wrapper("LookupByNameFailSafe", "_wrap_TypeId_LookupByNameFailSafe",
                                     flags=["METH_VARARGS", "METH_KEYWORDS", "METH_STATIC"])


def add_std_ofstream(module):
    module.add_include('<fstream>')
    ostream = module.add_class('ostream', foreign_cpp_namespace='::std')
    ostream.set_cannot_be_constructed("abstract base class")
    ofstream = module.add_class('ofstream', foreign_cpp_namespace='::std', parent=ostream)
    ofstream.add_enum('openmode', [
            ('app', 'std::ios_base::app'),
            ('ate', 'std::ios_base::ate'),
            ('binary', 'std::ios_base::binary'),
            ('in', 'std::ios_base::in'),
            ('out', 'std::ios_base::out'),
            ('trunc', 'std::ios_base::trunc'),
            ])
    ofstream.add_constructor([Parameter.new("const char *", 'filename'),
                              Parameter.new("::std::ofstream::openmode", 'mode', default_value="std::ios_base::out")])
    ofstream.add_method('close', None, [])
    
    add_std_ios_openmode(module)


def add_std_ios_openmode(module):
    import pybindgen.typehandlers.base
    for alias in "std::_Ios_Openmode", "std::ios::openmode":
        pybindgen.typehandlers.base.param_type_matcher.add_type_alias(alias, "int")

    for flag in 'in', 'out', 'ate', 'app', 'trunc', 'binary':
        module.after_init.write_code('PyModule_AddIntConstant(m, (char *) "STD_IOS_%s", std::ios::%s);'
                                     % (flag.upper(), flag))



def add_ipv4_address_tp_hash(module):
    module.body.writeln()
    module.header.writeln('long _ns3_Ipv4Address_tp_hash (PyObject *obj);')
    module['Ipv4Address'].pytype.slots['tp_hash'] = "_ns3_Ipv4Address_tp_hash"
