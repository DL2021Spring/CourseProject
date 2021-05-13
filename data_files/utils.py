





import os
import sys

def get_list_from_file(file_path, list_name):
    

    list = []

    
    if os.path.exists(file_path):
        file_in = open(file_path, "r")

        
        list_string = ""
        parsing_multiline_list = False
        for line in file_in:
            if list_name in line or parsing_multiline_list:
                list_string += line

                
                if ']' not in list_string:
                    parsing_multiline_list = True
                else:
                    
                    
                    list = eval(list_string.split('=', 1)[1].strip())
                    break

        
        file_in.close()

    return list


def get_bool_from_file(file_path, bool_name, value_if_missing):
    

    
    if os.path.exists(file_path):
        file_in = open(file_path, "r")

        
        bool_found = False
        for line in file_in:
            if bool_name in line:
                
                
                bool = eval(line.split('=', 1)[1].strip())
                bool_found = True
                break

        
        file_in.close()

    if bool_found:
        return bool
    else:
        return value_if_missing






def read_config_file():
    
    
    modules_enabled  = ['all_modules']
    examples_enabled = False
    tests_enabled    = False

    
    
    config_file_exists = False
    dot_ns3rc_name = '.ns3rc'
    dot_ns3rc_path = dot_ns3rc_name
    if not os.path.exists(dot_ns3rc_path):
        dot_ns3rc_path = os.path.expanduser('~/') + dot_ns3rc_name
        if not os.path.exists(dot_ns3rc_path):
            
            return (config_file_exists, modules_enabled, examples_enabled, tests_enabled)

    config_file_exists = True

    
    modules_enabled = get_list_from_file(dot_ns3rc_path, 'modules_enabled')
    if not modules_enabled:
        
        modules_enabled = ['all_modules']

    
    value_if_missing = False
    examples_enabled = get_bool_from_file(dot_ns3rc_path, 'examples_enabled', value_if_missing)

    
    value_if_missing = False
    tests_enabled = get_bool_from_file(dot_ns3rc_path, 'tests_enabled', value_if_missing)

    return (config_file_exists, modules_enabled, examples_enabled, tests_enabled)

