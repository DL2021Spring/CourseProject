


















import os
import sys
import time
import optparse
import subprocess
import threading
import Queue
import signal
import xml.dom.minidom
import shutil
import re

from utils import get_list_from_file











interesting_config_items = [
    "NS3_ENABLED_MODULES",
    "NS3_MODULE_PATH",
    "NSC_ENABLED",
    "ENABLE_REAL_TIME",
    "ENABLE_THREADING",
    "ENABLE_EXAMPLES",
    "ENABLE_TESTS",
    "EXAMPLE_DIRECTORIES",
    "ENABLE_PYTHON_BINDINGS",
    "ENABLE_CLICK",
    "ENABLE_OPENFLOW",
]

NSC_ENABLED = False
ENABLE_REAL_TIME = False
ENABLE_THREADING = False
ENABLE_EXAMPLES = True
ENABLE_TESTS = True
ENABLE_CLICK = False
ENABLE_OPENFLOW = False
EXAMPLE_DIRECTORIES = []





core_kinds = ["bvt", "core", "system", "unit"]





core_valgrind_skip_tests = [
    "ns3-tcp-cwnd",
    "nsc-tcp-loss",
    "ns3-tcp-interoperability",
    "routing-click",
]





core_nsc_missing_skip_tests = [
    "ns3-tcp-cwnd",
    "nsc-tcp-loss",
    "ns3-tcp-interoperability",
]







def parse_examples_to_run_file(
    examples_to_run_path,
    cpp_executable_dir,
    python_script_dir,
    example_tests,
    python_tests):

    
    if os.path.exists(examples_to_run_path):

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        cpp_examples = get_list_from_file(examples_to_run_path, "cpp_examples")
        for example_name, do_run, do_valgrind_run in cpp_examples:
            example_path = os.path.join(cpp_executable_dir, example_name)
            
            
            if os.path.exists(example_path):
                example_tests.append((example_path, do_run, do_valgrind_run))

        
        
        
        
        
        
        
        
        
        
        
        
        python_examples = get_list_from_file(examples_to_run_path, "python_examples")
        for example_name, do_run in python_examples:
            example_path = os.path.join(python_script_dir, example_name)
            
            
            if os.path.exists(example_path):
                python_tests.append((example_path, do_run))













TMP_OUTPUT_DIR = "testpy-output"

def read_test(test):
    result = test.find('Result').text
    name = test.find('Name').text
    if not test.find('Time') is None:
        time_real = test.find('Time').get('real')
    else:
        time_real = ''
    return (result, name, time_real)





def node_to_text (test, f):
    (result, name, time_real) = read_test(test)
    output = "%s: Test Suite \"%s\" (%s)\n" % (result, name, time_real)
    f.write(output)
    for details in test.findall('FailureDetails'):
        f.write("    Details:\n")
        f.write("      Message:   %s\n" % details.find('Message').text)
        f.write("      Condition: %s\n" % details.find('Condition').text)
        f.write("      Actual:    %s\n" % details.find('Actual').text)
        f.write("      Limit:     %s\n" % details.find('Limit').text)
        f.write("      File:      %s\n" % details.find('File').text)
        f.write("      Line:      %s\n" % details.find('Line').text)
    for child in test.findall('Test'):
        node_to_text(child, f)

def translate_to_text(results_file, text_file):
    f = open(text_file, 'w')
    import xml.etree.ElementTree as ET
    et = ET.parse (results_file)
    for test in et.findall('Test'):
        node_to_text (test, f)

    for example in et.findall('Example'):
        result = example.find('Result').text
        name = example.find('Name').text
        if not example.find('Time') is None:
            time_real = example.find('Time').get('real')
        else:
            time_real = ''
        output = "%s: Example \"%s\" (%s)\n" % (result, name, time_real)
        f.write(output)

    f.close()
    






def translate_to_html(results_file, html_file):
    f = open(html_file, 'w')
    f.write("<html>\n")
    f.write("<body>\n")
    f.write("<center><h1>ns-3 Test Results</h1></center>\n")

    
    
    
    import xml.etree.ElementTree as ET
    et = ET.parse(results_file)

    
    
    
    f.write("<h2>Test Suites</h2>\n")
    for suite in et.findall('Test'):     
        
        
        
        (result, name, time) = read_test (suite)

        
        
        
        
        
        
        if result == "PASS":
            f.write("<h3 style=\"color:green\">%s: %s (%s)</h3>\n" % (result, name, time))
        elif result == "SKIP":
            f.write("<h3 style=\"color:
        else:
            f.write("<h3 style=\"color:red\">%s: %s (%s)</h3>\n" % (result, name, time))

        
        
        
        f.write("<table border=\"1\">\n")

        
        
        
        f.write("<th> Result </th>\n")

        
        
        
        
        
        
        
        
        
        
        
        
        if result in ["CRASH", "SKIP", "VALGR"]:
            f.write("<tr>\n")
            if result == "SKIP":
                f.write("<td style=\"color:
            else:
                f.write("<td style=\"color:red\">%s</td>\n" % result)
            f.write("</tr>\n")
            f.write("</table>\n")
            continue

        
        
        
        
        
        
        
        
        f.write("<th>Test Case Name</th>\n")
        f.write("<th> Time </th>\n")

        
        
        
        
        
        
        
        
        if result == "FAIL":
            f.write("<th>Failure Details</th>\n")

        
        
        
        for case in suite.findall('Test'):

            
            
            
            
            (result, name, time) = read_test(case)

            
            
            
            
            if result == "FAIL":
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                

                first_row = True
                for details in case.findall('FailureDetails'):

                    
                    
                    
                    f.write("<tr>\n")

                    if first_row:
                        first_row = False
                        f.write("<td style=\"color:red\">%s</td>\n" % result)
                        f.write("<td>%s</td>\n" % name)
                        f.write("<td>%s</td>\n" % time)
                    else:
                        f.write("<td></td>\n")
                        f.write("<td></td>\n")
                        f.write("<td></td>\n")

                    f.write("<td>")
                    f.write("<b>Message: </b>%s, " % details.find('Message').text)
                    f.write("<b>Condition: </b>%s, " % details.find('Condition').text)
                    f.write("<b>Actual: </b>%s, " % details.find('Actual').text)
                    f.write("<b>Limit: </b>%s, " % details.find('Limit').text)
                    f.write("<b>File: </b>%s, " % details.find('File').text)
                    f.write("<b>Line: </b>%s" % details.find('Line').text)
                    f.write("</td>\n")
                    
                    
                    
                    
                    f.write("</td>\n")
            else:
                
                
                
                
                
                
                
                
                
                
                
                
                f.write("<tr>\n")
                f.write("<td style=\"color:green\">%s</td>\n" % result)
                f.write("<td>%s</td>\n" % name)
                f.write("<td>%s</td>\n" % time)
                f.write("<td></td>\n")
                f.write("</tr>\n")
        
        
        
        f.write("</table>\n")

    
    
    
    
    f.write("<h2>Examples</h2>\n")

    
    
    
    f.write("<table border=\"1\">\n")

    
    
    
    
    
    
    
    f.write("<th> Result </th>\n")
    f.write("<th>Example Name</th>\n")
    f.write("<th>Elapsed Time</th>\n")

    
    
    
    for example in et.findall("Example"):
        
        
        
        
        f.write("<tr>\n")
        
        
        
        
        (result, name, time) = read_test(example)

        
        
        
        
        if result == "PASS":
            f.write("<td style=\"color:green\">%s</td>\n" % result)
        elif result == "SKIP":
            f.write("<td style=\"color:
        else:
            f.write("<td style=\"color:red\">%s</td>\n" % result)

        
        
        
        f.write("<td>%s</td>\n" % name)

        
        
        
        f.write("<td>%s</td>\n" % time)

        
        
        
        f.write("</tr>\n")

    
    
    
    f.write("</table>\n")

    
    
    
    f.write("</body>\n")
    f.write("</html>\n")
    f.close()
    






thread_exit = False

def sigint_hook(signal, frame):
    global thread_exit
    thread_exit = True
    return 0


















def read_waf_config():
    for line in open(".lock-wafbuild", "rt"):
        if line.startswith("out_dir ="):
            key, val = line.split('=')
            out_dir = eval(val.strip())
    global NS3_BUILDDIR
    NS3_BUILDDIR = out_dir
    for line in open("%s/c4che/_cache.py" % out_dir).readlines():
        for item in interesting_config_items:
            if line.startswith(item):
                exec(line, globals())

    if options.verbose:
        for item in interesting_config_items:
            print "%s ==" % item, eval(item)











def make_paths():
    have_DYLD_LIBRARY_PATH = False
    have_LD_LIBRARY_PATH = False
    have_PATH = False
    have_PYTHONPATH = False

    keys = os.environ.keys()
    for key in keys:
        if key == "DYLD_LIBRARY_PATH":
            have_DYLD_LIBRARY_PATH = True
        if key == "LD_LIBRARY_PATH":
            have_LD_LIBRARY_PATH = True
        if key == "PATH":
            have_PATH = True
        if key == "PYTHONPATH":
            have_PYTHONPATH = True

    pypath = os.environ["PYTHONPATH"] = os.path.join (NS3_BUILDDIR, "bindings", "python")

    if not have_PYTHONPATH:
        os.environ["PYTHONPATH"] = pypath
    else:
        os.environ["PYTHONPATH"] += ":" + pypath

    if options.verbose:
        print "os.environ[\"PYTHONPATH\"] == %s" % os.environ["PYTHONPATH"]

    if sys.platform == "darwin":
        if not have_DYLD_LIBRARY_PATH:
            os.environ["DYLD_LIBRARY_PATH"] = ""
        for path in NS3_MODULE_PATH:
            os.environ["DYLD_LIBRARY_PATH"] += ":" + path
        if options.verbose:
            print "os.environ[\"DYLD_LIBRARY_PATH\"] == %s" % os.environ["DYLD_LIBRARY_PATH"]
    elif sys.platform == "win32":
        if not have_PATH:
            os.environ["PATH"] = ""
        for path in NS3_MODULE_PATH:
            os.environ["PATH"] += ';' + path
        if options.verbose:
            print "os.environ[\"PATH\"] == %s" % os.environ["PATH"]
    elif sys.platform == "cygwin":
        if not have_PATH:
            os.environ["PATH"] = ""
        for path in NS3_MODULE_PATH:
            os.environ["PATH"] += ":" + path
        if options.verbose:
            print "os.environ[\"PATH\"] == %s" % os.environ["PATH"]
    else:
        if not have_LD_LIBRARY_PATH:
            os.environ["LD_LIBRARY_PATH"] = ""
        for path in NS3_MODULE_PATH:
            os.environ["LD_LIBRARY_PATH"] += ":" + path
        if options.verbose:
            print "os.environ[\"LD_LIBRARY_PATH\"] == %s" % os.environ["LD_LIBRARY_PATH"]















































































VALGRIND_SUPPRESSIONS_FILE = "testpy.supp"

def run_job_synchronously(shell_command, directory, valgrind, is_python, build_path=""):
    (base, build) = os.path.split (NS3_BUILDDIR)
    suppressions_path = os.path.join (base, VALGRIND_SUPPRESSIONS_FILE)

    if is_python:
        path_cmd = "python " + os.path.join (base, shell_command)
    else:
        if len(build_path):
            path_cmd = os.path.join (build_path, shell_command)
        else:
            path_cmd = os.path.join (NS3_BUILDDIR, shell_command)

    if valgrind:
        cmd = "valgrind --suppressions=%s --leak-check=full --show-reachable=yes --error-exitcode=2 %s" % (suppressions_path, 
            path_cmd)
    else:
        cmd = path_cmd

    if options.verbose:
        print "Synchronously execute %s" % cmd

    start_time = time.time()
    proc = subprocess.Popen(cmd, shell = True, cwd = directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_results, stderr_results = proc.communicate()
    elapsed_time = time.time() - start_time

    retval = proc.returncode

    
    
    
    
    
    
    
    
    
    if valgrind and retval == 0 and "== LEAK SUMMARY:" in stderr_results:
        retval = 2
    
    if options.verbose:
        print "Return code = ", retval
        print "stderr = ", stderr_results

    return (retval, stdout_results, stderr_results, elapsed_time)





class Job:
    def __init__(self):
        self.is_break = False
        self.is_skip = False
        self.is_example = False
        self.is_pyexample = False
        self.shell_command = ""
        self.display_name = ""
        self.basedir = ""
        self.tempdir = ""
        self.cwd = ""
        self.tmp_file_name = ""
        self.returncode = False
        self.elapsed_time = 0
        self.build_path = ""

    
    
    
    
    
    def set_is_break(self, is_break):
        self.is_break = is_break

    
    
    
    
    def set_is_skip(self, is_skip):
        self.is_skip = is_skip

    
    
    
    
    
    
    def set_is_example(self, is_example):
        self.is_example = is_example

    
    
    
    
    
    
    def set_is_pyexample(self, is_pyexample):
        self.is_pyexample = is_pyexample

    
    
    
    
    
    def set_shell_command(self, shell_command):
        self.shell_command = shell_command

    
    
    
    
    
    def set_build_path(self, build_path):
        self.build_path = build_path

    
    
    
    
    
    
    def set_display_name(self, display_name):
        self.display_name = display_name

    
    
    
    
    
    
    
    
    def set_basedir(self, basedir):
        self.basedir = basedir

    
    
    
    
    def set_tempdir(self, tempdir):
        self.tempdir = tempdir

    
    
    
    
    
    
    
    
    def set_cwd(self, cwd):
        self.cwd = cwd

    
    
    
    
    
    
    def set_tmp_file_name(self, tmp_file_name):
        self.tmp_file_name = tmp_file_name

    
    
    
    def set_returncode(self, returncode):
        self.returncode = returncode

    
    
    
    def set_elapsed_time(self, elapsed_time):
        self.elapsed_time = elapsed_time






class worker_thread(threading.Thread):
    def __init__(self, input_queue, output_queue):
        threading.Thread.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue

    def run(self):
        while True:
            job = self.input_queue.get()
            
            
            
            
            if job.is_break:
                return
            
            
            
            
            
            if thread_exit == True:
                job.set_is_break(True)
                self.output_queue.put(job)
                continue

            
            
            
            
            if job.is_skip:
                if options.verbose:
                    print "Skip %s" % job.shell_command
                self.output_queue.put(job)
                continue

            
            
            
            else:
                if options.verbose:
                    print "Launch %s" % job.shell_command

                if job.is_example or job.is_pyexample:
                    
                    
                    
                    
                    
                    (job.returncode, standard_out, standard_err, et) = run_job_synchronously(job.shell_command, 
                        job.cwd, options.valgrind, job.is_pyexample, job.build_path)
                else:
                    
                    
                    
                    
                    
                    if options.update_data:
                        update_data = '--update-data'
                    else:
                        update_data = ''
                    (job.returncode, standard_out, standard_err, et) = run_job_synchronously(job.shell_command + 
                        " --xml --tempdir=%s --out=%s %s" % (job.tempdir, job.tmp_file_name, update_data), 
                        job.cwd, options.valgrind, False)

                job.set_elapsed_time(et)

                if options.verbose:
                    print "returncode = %d" % job.returncode
                    print "---------- begin standard out ----------"
                    print standard_out
                    print "---------- begin standard err ----------"
                    print standard_err
                    print "---------- end standard err ----------"

                self.output_queue.put(job)





def run_tests():
    
    
    
    
    
    
    if not options.nowaf:

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        if options.kinds or options.list or (len(options.constrain) and options.constrain in core_kinds):
            if sys.platform == "win32":
                waf_cmd = "waf --target=test-runner"
            else:
                waf_cmd = "./waf --target=test-runner"
        elif len(options.example):
            if sys.platform == "win32":
                waf_cmd = "waf --target=%s" % os.path.basename(options.example)
            else:
                waf_cmd = "./waf --target=%s" % os.path.basename(options.example)

        else:
            if sys.platform == "win32":
                waf_cmd = "waf"
            else:
                waf_cmd = "./waf"

        if options.verbose:
            print "Building: %s" % waf_cmd

        proc = subprocess.Popen(waf_cmd, shell = True)
        proc.communicate()
        if proc.returncode:
            print >> sys.stderr, "Waf died. Not running tests"
            return proc.returncode

    
    
    
    
    
    
    read_waf_config()
    make_paths()

    
    build_status_file = os.path.join (NS3_BUILDDIR, 'build-status.py')
    if os.path.exists(build_status_file):
        ns3_runnable_programs = get_list_from_file(build_status_file, "ns3_runnable_programs")
        ns3_runnable_scripts = get_list_from_file(build_status_file, "ns3_runnable_scripts")
    else:
        print >> sys.stderr, 'The build status file was not found.  You must do waf build before running test.py.'
        sys.exit(2)

    
    
    
    example_tests = []
    python_tests = []
    for directory in EXAMPLE_DIRECTORIES:
        
        example_directory   = os.path.join("examples", directory)
        examples_to_run_path = os.path.join(example_directory, "examples-to-run.py")
        cpp_executable_dir   = os.path.join(NS3_BUILDDIR, example_directory)
        python_script_dir    = os.path.join(example_directory)

        
        parse_examples_to_run_file(
            examples_to_run_path,
            cpp_executable_dir,
            python_script_dir,
            example_tests,
            python_tests)

    for module in NS3_ENABLED_MODULES:
        
        module = module[len("ns3-"):]

        
        module_directory     = os.path.join("src", module)
        example_directory    = os.path.join(module_directory, "examples")
        examples_to_run_path = os.path.join(module_directory, "test", "examples-to-run.py")
        cpp_executable_dir   = os.path.join(NS3_BUILDDIR, example_directory)
        python_script_dir    = os.path.join(example_directory)

        
        parse_examples_to_run_file(
            examples_to_run_path,
            cpp_executable_dir,
            python_script_dir,
            example_tests,
            python_tests)

    
    
    
    
    
    
    os.environ["NS_LOG"] = ""

    
    
    
    
    
    if options.kinds:
        path_cmd = os.path.join("utils", "test-runner --print-test-type-list")
        (rc, standard_out, standard_err, et) = run_job_synchronously(path_cmd, os.getcwd(), False, False)
        print standard_out

    if options.list:
        path_cmd = os.path.join("utils", "test-runner --print-test-name-list")
        (rc, standard_out, standard_err, et) = run_job_synchronously(path_cmd, os.getcwd(), False, False)
        print standard_out

    if options.kinds or options.list:
        return

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    date_and_time = time.strftime("%Y-%m-%d-%H-%M-%S-CUT", time.gmtime())

    if not os.path.exists(TMP_OUTPUT_DIR):
        os.makedirs(TMP_OUTPUT_DIR)

    testpy_output_dir = os.path.join(TMP_OUTPUT_DIR, date_and_time);

    if not os.path.exists(testpy_output_dir):
        os.makedirs(testpy_output_dir)

    
    
    
    
    xml_results_file = os.path.join(testpy_output_dir, "results.xml")
    f = open(xml_results_file, 'w')
    f.write('<?xml version="1.0"?>\n')
    f.write('<Results>\n')
    f.close()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if len(options.suite):
        
        path_cmd = os.path.join("utils", "test-runner --print-test-name-list")
        (rc, suites, standard_err, et) = run_job_synchronously(path_cmd, os.getcwd(), False, False)
        if options.suite in suites:
            suites = options.suite + "\n"
        else:
            print >> sys.stderr, 'The test suite was not run because an unknown test suite name was requested.'
            sys.exit(2)

    elif len(options.example) == 0 and len(options.pyexample) == 0:
        if len(options.constrain):
            path_cmd = os.path.join("utils", "test-runner --print-test-name-list --test-type=%s" % options.constrain)
            (rc, suites, standard_err, et) = run_job_synchronously(path_cmd, os.getcwd(), False, False)
        else:
            path_cmd = os.path.join("utils", "test-runner --print-test-name-list")
            (rc, suites, standard_err, et) = run_job_synchronously(path_cmd, os.getcwd(), False, False)
    else:
        suites = ""

    
    
    
    
    
    
    
    
    suite_list = suites.split('\n')

    
    
    
    
    
    input_queue = Queue.Queue(0)
    output_queue = Queue.Queue(0)

    jobs = 0
    threads=[]

    
    
    
    
    processors = 1

    if sys.platform != "win32":
        if 'SC_NPROCESSORS_ONLN'in os.sysconf_names:
            processors = os.sysconf('SC_NPROCESSORS_ONLN')
        else:
            proc = subprocess.Popen("sysctl -n hw.ncpu", shell = True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout_results, stderr_results = proc.communicate()
            if len(stderr_results) == 0:
                processors = int(stdout_results)

    
    
    
    
    for i in range(processors):
        thread = worker_thread(input_queue, output_queue)
        threads.append(thread)
        thread.start()

    
    
    
    total_tests = 0
    skipped_tests = 0

    
    
    
    
    
    
    
    
    
    
    for test in suite_list:
        test = test.strip()
        if len(test):
            job = Job()
            job.set_is_example(False)
            job.set_is_pyexample(False)
            job.set_display_name(test)
            job.set_tmp_file_name(os.path.join(testpy_output_dir, "%s.xml" % test))
            job.set_cwd(os.getcwd())
            job.set_basedir(os.getcwd())
            job.set_tempdir(testpy_output_dir)
            if (options.multiple):
                multiple = ""
            else:
                multiple = " --stop-on-failure"

            path_cmd = os.path.join("utils", "test-runner --test-name=%s%s" % (test, multiple))
            job.set_shell_command(path_cmd)

            if options.valgrind and test in core_valgrind_skip_tests:
                job.set_is_skip(True)

            
            if not NSC_ENABLED and test in core_nsc_missing_skip_tests:
                job.set_is_skip(True)

            if options.verbose:
                print "Queue %s" % test

            input_queue.put(job)
            jobs = jobs + 1
            total_tests = total_tests + 1
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if len(options.suite) == 0 and len(options.example) == 0 and len(options.pyexample) == 0:
        if len(options.constrain) == 0 or options.constrain == "example":
            if ENABLE_EXAMPLES:
                for test, do_run, do_valgrind_run in example_tests:

                    
                    if os.path.basename(test) in ns3_runnable_programs:
                        if eval(do_run):
                            job = Job()
                            job.set_is_example(True)
                            job.set_is_pyexample(False)
                            job.set_display_name(test)
                            job.set_tmp_file_name("")
                            job.set_cwd(testpy_output_dir)
                            job.set_basedir(os.getcwd())
                            job.set_tempdir(testpy_output_dir)
                            job.set_shell_command(test)
                            job.set_build_path("")

                            if options.valgrind and not eval(do_valgrind_run):
                                job.set_is_skip (True)

                            if options.verbose:
                                print "Queue %s" % test

                            input_queue.put(job)
                            jobs = jobs + 1
                            total_tests = total_tests + 1

    elif len(options.example):
        
        example_name = os.path.basename(options.example)
        if example_name not in ns3_runnable_programs:
            print "Example %s is not runnable." % example_name
        else:
            
            
            
            
            job = Job()
            job.set_is_example(True)
            job.set_is_pyexample(False)
            job.set_display_name(options.example)
            job.set_tmp_file_name("")
            job.set_cwd(testpy_output_dir)
            job.set_basedir(os.getcwd())
            job.set_tempdir(testpy_output_dir)
            job.set_shell_command(options.example)
            job.set_build_path(options.buildpath)

            if options.verbose:
                print "Queue %s" % options.example

            input_queue.put(job)
            jobs = jobs + 1
            total_tests = total_tests + 1

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if len(options.suite) == 0 and len(options.example) == 0 and len(options.pyexample) == 0:
        if len(options.constrain) == 0 or options.constrain == "pyexample":
            if ENABLE_EXAMPLES:
                for test, do_run in python_tests:

                    
                    if os.path.basename(test) in ns3_runnable_scripts:
                        if eval(do_run):
                            job = Job()
                            job.set_is_example(False)
                            job.set_is_pyexample(True)
                            job.set_display_name(test)
                            job.set_tmp_file_name("")
                            job.set_cwd(testpy_output_dir)
                            job.set_basedir(os.getcwd())
                            job.set_tempdir(testpy_output_dir)
                            job.set_shell_command(test)
                            job.set_build_path("")

                            
                            
                            
                            
                            
                            
                            
                            if options.valgrind:
                                job.set_is_skip (True)

                            
                            
                            
                            
                            
                            if not ENABLE_PYTHON_BINDINGS:
                                job.set_is_skip (True)

                            if options.verbose:
                                print "Queue %s" % test

                            input_queue.put(job)
                            jobs = jobs + 1
                            total_tests = total_tests + 1

    elif len(options.pyexample):
        
        example_name = os.path.basename(options.pyexample)
        if example_name not in ns3_runnable_scripts:
            print "Example %s is not runnable." % example_name
        else:
            
            
            
            
            job = Job()
            job.set_is_pyexample(True)
            job.set_display_name(options.pyexample)
            job.set_tmp_file_name("")
            job.set_cwd(testpy_output_dir)
            job.set_basedir(os.getcwd())
            job.set_tempdir(testpy_output_dir)
            job.set_shell_command(options.pyexample)
            job.set_build_path("")

            if options.verbose:
                print "Queue %s" % options.pyexample

            input_queue.put(job)
            jobs = jobs + 1
            total_tests = total_tests + 1

    
    
    
    
    for i in range(processors):
        job = Job()
        job.set_is_break(True)
        input_queue.put(job)

    
    
    
    
    
    
    
    
    
    
    passed_tests = 0
    failed_tests = 0
    crashed_tests = 0
    valgrind_errors = 0
    for i in range(jobs):
        job = output_queue.get()
        if job.is_break:
            continue

        if job.is_example or job.is_pyexample:
            kind = "Example"
        else:
            kind = "TestSuite"

        if job.is_skip:
            status = "SKIP"
            skipped_tests = skipped_tests + 1
        else:
            if job.returncode == 0:
                status = "PASS"
                passed_tests = passed_tests + 1
            elif job.returncode == 1:
                failed_tests = failed_tests + 1
                status = "FAIL"
            elif job.returncode == 2:
                valgrind_errors = valgrind_errors + 1
                status = "VALGR"
            else:
                crashed_tests = crashed_tests + 1
                status = "CRASH"

        print "%s: %s %s" % (status, kind, job.display_name)

        if job.is_example or job.is_pyexample:
            
            
            
            
            
            
            
            
            
            f = open(xml_results_file, 'a')
            f.write('<Example>\n')
            example_name = "  <Name>%s</Name>\n" % job.display_name
            f.write(example_name)

            if status == "PASS":
                f.write('  <Result>PASS</Result>\n')
            elif status == "FAIL":
                f.write('  <Result>FAIL</Result>\n')
            elif status == "VALGR":
                f.write('  <Result>VALGR</Result>\n')
            elif status == "SKIP":
                f.write('  <Result>SKIP</Result>\n')
            else:
                f.write('  <Result>CRASH</Result>\n')

            f.write('  <Time real="%.3f"/>\n' % job.elapsed_time)
            f.write('</Example>\n')
            f.close()

        else:
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            if job.is_skip:
                f = open(xml_results_file, 'a')
                f.write("<Test>\n")
                f.write("  <Name>%s</Name>\n" % job.display_name)
                f.write('  <Result>SKIP</Result>\n')
                f.write("</Test>\n")
                f.close()
            else:
                if job.returncode == 0 or job.returncode == 1 or job.returncode == 2:
                    f_to = open(xml_results_file, 'a')
                    f_from = open(job.tmp_file_name)
                    f_to.write(f_from.read())
                    f_to.close()
                    f_from.close()
                else:
                    f = open(xml_results_file, 'a')
                    f.write("<Test>\n")
                    f.write("  <Name>%s</Name>\n" % job.display_name)
                    f.write('  <Result>CRASH</Suite>\n')
                    f.write("</Test>\n")
                    f.close()

                    if job.returncode == 2:
                        f = open(xml_results_file, 'a')
                        f.write("<Test>\n")
                        f.write("  <Name>%s</Name>\n" % job.display_name)
                        f.write('  <Result>VALGR</Result>\n')
                        f.write("</Test>\n")
                        f.close()

    
    
    
    
    
    for thread in threads:
        thread.join()
    
    
    
    
    
    
    
    f = open(xml_results_file, 'a')
    f.write('</Results>\n')
    f.close()

    
    
    
    print "%d of %d tests passed (%d passed, %d skipped, %d failed, %d crashed, %d valgrind errors)" % (passed_tests, 
        total_tests, passed_tests, skipped_tests, failed_tests, crashed_tests, valgrind_errors)
    
    
    
    
    if len(options.html):
        translate_to_html(xml_results_file, options.html)

    if len(options.text):
        translate_to_text(xml_results_file, options.text)

    if len(options.xml):
        shutil.copyfile(xml_results_file, options.xml)

    
    
    
    if not ENABLE_TESTS or not ENABLE_EXAMPLES:
        print
        if not ENABLE_TESTS:
            print '***  Note: ns-3 tests are currently disabled. Enable them by adding'
            print '***  "--enable-tests" to ./waf configure or modifying your .ns3rc file.'
            print
        if not ENABLE_EXAMPLES:
            print '***  Note: ns-3 examples are currently disabled. Enable them by adding'
            print '***  "--enable-examples" to ./waf configure or modifying your .ns3rc file.'
            print
    
    
    
    
    
    
    if not options.retain:
        shutil.rmtree(testpy_output_dir)

    if passed_tests + skipped_tests == total_tests:
        return 0 
    else:
        return 1 

def main(argv):
    parser = optparse.OptionParser()
    parser.add_option("-b", "--buildpath", action="store", type="string", dest="buildpath", default="",
                      metavar="BUILDPATH",
                      help="specify the path where ns-3 was built (defaults to the build directory for the current variant)")

    parser.add_option("-c", "--constrain", action="store", type="string", dest="constrain", default="",
                      metavar="KIND",
                      help="constrain the test-runner by kind of test")

    parser.add_option("-e", "--example", action="store", type="string", dest="example", default="",
                      metavar="EXAMPLE",
                      help="specify a single example to run (with relative path)")

    parser.add_option("-u", "--update-data", action="store_true", dest="update_data", default=False,
                      help="If examples use reference data files, get them to re-generate them")

    parser.add_option("-g", "--grind", action="store_true", dest="valgrind", default=False,
                      help="run the test suites and examples using valgrind")

    parser.add_option("-k", "--kinds", action="store_true", dest="kinds", default=False,
                      help="print the kinds of tests available")

    parser.add_option("-l", "--list", action="store_true", dest="list", default=False,
                      help="print the list of known tests")

    parser.add_option("-m", "--multiple", action="store_true", dest="multiple", default=False,
                      help="report multiple failures from test suites and test cases")

    parser.add_option("-n", "--nowaf", action="store_true", dest="nowaf", default=False,
                      help="do not run waf before starting testing")

    parser.add_option("-p", "--pyexample", action="store", type="string", dest="pyexample", default="",
                      metavar="PYEXAMPLE",
                      help="specify a single python example to run (with relative path)")

    parser.add_option("-r", "--retain", action="store_true", dest="retain", default=False,
                      help="retain all temporary files (which are normally deleted)")

    parser.add_option("-s", "--suite", action="store", type="string", dest="suite", default="",
                      metavar="TEST-SUITE",
                      help="specify a single test suite to run")

    parser.add_option("-t", "--text", action="store", type="string", dest="text", default="",
                      metavar="TEXT-FILE",
                      help="write detailed test results into TEXT-FILE.txt")

    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", default=False,
                      help="print progress and informational messages")

    parser.add_option("-w", "--web", "--html", action="store", type="string", dest="html", default="",
                      metavar="HTML-FILE",
                      help="write detailed test results into HTML-FILE.html")

    parser.add_option("-x", "--xml", action="store", type="string", dest="xml", default="",
                      metavar="XML-FILE",
                      help="write detailed test results into XML-FILE.xml")

    global options
    options = parser.parse_args()[0]
    signal.signal(signal.SIGINT, sigint_hook)

    return run_tests()

if __name__ == '__main__':
    sys.exit(main(sys.argv))
