#*******************************************************************************
#*                           Easypy Job File Template
#* ----------------------------------------------------------------------------
#* ABOUT THIS TEMPLATE - Please read
#*
#* - Any comments with "#*" in front of them (like this entire comment box) are
#*   for template clarifications only and should be removed from the final
#*   product.
#*
#* - Anything enclosed in <> must be replaced by the appropriate text for your
#*   application
#*
#* Author:
#*    Siming Yuan, Automation Strategy - Core Software Group (CSG)
#*
#* Support:
#*    pyats-support@cisco.com
#*
#* Description:
#*   This template file describes how to write a standard pyATS Easypy style
#*   job file.
#*
#* Read More:
#*   For the complete and up-to-date information on using jobfiles, refer to:
#*   URL= http://wwwin-pyats.cisco.com/documentation/html/easypy/jobfile.html
#*
#*******************************************************************************

#*******************************************************************************
#* DOCSTRINGS
#*
#*   All job files should use the built-in Python docstrings functionality 
#*   to define their headers
#*
#* Format:
#*   Docstring format should follow:
#*   URL= http://sphinxcontrib-napoleon.readthedocs.org/en/latest/index.html
#*
#* Read More:
#*   Python Docstrings, PEP 257: 
#*   URL= http://legacy.python.org/dev/peps/pep-0257/
#*******************************************************************************
'''template_job.py

This is an example docstring for an a job file. The header should describe which
scripts are included as part of this job, their required topology, and any other
information which may concern the person that runs this job.

Purpose:
    < State Purpose Here >

Usage:
    bash$ easypy <pyats_root>/templates/enhanced/job/template_job.py

Description:
    < descriptiveText >

Requirements:
    - < yourRequirements >

Noes:
    <something>

'''

#
# optional author information
#
__author__ = 'Cisco Systems Inc.'
__copyright__ = 'Copyright (c) 2017, Cisco Systems Inc.'
__contact__ = ['pyats-support@cisco.com', 'pyats-support-ext@cisco.com']
__date__= 'June 15, 2015'
__version__ = 2.0


#*******************************************************************************
#* IMPORTS
#*
#*   import all modules that are needed in your test script here. Use some 
#*   form of sorting to make it easy to read. 
#*
#* Convention:
#*   - one module per import for clarity
#*   - sort imports either alphabetically or per length to give ease of reading,
#*     also try to differentiate by functionality/distributor
#*
#* Examples:
#*   import os
#*   from ats.easypy import run
#*
#* Read More:
#*   Python Import System
#*   URL= https://docs.python.org/3/reference/import.html
#*******************************************************************************

#
# import block
#
import os
import logging
import argparse

from ats.easypy import run

# import logic statements from datastructures module
from ats.datastructures.logic import And, Or, Not

#*******************************************************************************
#* ENVIRONMENT
#*
#*   often it may be necessary to parse environment variables to set up script
#*   inputs/arguments based on them. This allows dynamic information from the
#*   environment (such as EARMs) to control certain behavior of the job.
#*
#*   Example
#*   -------
#*      # beware that environment values are always in strings, and need
#*      # to be casted to python objects
#*      # note that below is effectively the same as writing
#*      #  if 'force_all_tests_to_pass' in os.environ:
#*      #      force_all_pass = bool(os.environ['force_all_tests_to_pass'])
#*      #  else:
#*      #      force_all_pass = False
#*      *
#*      force_all_pass = bool(os.environ.get('force_all_tests_to_pass', False))
#*
#*      # now call the script with this arg
#*      # it's not a good idea to make all tests pass :( but it's black magic!
#*      run(testscript='/path/to/script.py',
#*          force_all_pass = force_all_pass)
#*
#*******************************************************************************

#
# logic here to process environment variables.
#
loglevel = os.environ.get('loglevel', 'INFO')
groups = os.environ.get('execution_group', None)
my_variable = os.environ.get('my_variable', 'default_value')

#*******************************************************************************
#* PARSING COMMAND LINE ARGUMENTS
#*
#*  Easypy & AEtest features argument propagation: propagating custom command
#*  line arguments to jobfile & the testscript. In a nutshell, the requirement
#*  is simple: parse only what you need using parse_known_args(), leave the 
#*  rest in sys.argv.
#*
#*  If your jobfile requires additional command line arguments, you'll need to
#*  create an argparse section here. 
#*
#*  note - argparse modules are already imported for your convenience above.
#*
#*******************************************************************************

#
# create your custom job file argument parser here
#
parser = argparse.ArgumentParser(description='example job file cli args parser')
parser.add_argument('--argument_a',
                    help='example argument a',
                    default = None)
parser.add_argument('--argument_b',
                    help='example argument b',
                    default = None)

#*******************************************************************************
#* TESTBED INFORMATION
#*
#*  when executing a jobfile using easypy, testbed file should be provided to 
#*  easypy launcher using argument -testbed_file. Easypy will automatically 
#*  load this provided testbed file into topology objects, and pass it to each
#*  testscript as script argument "testbed". 
#*       easypy myjobfile.py -testbed_file mytestbed.yaml
#*
#*  as long as the argument is used properly, there's nothing extra the user 
#*  has to do. Testscripts will automatically be passed the parameter 'testbed',
#*  along with all the topology objects.
#*
#*
#* TOPOLOGY INFORMATION
#*
#*  in an effort to abstract the script's topology/device requirements away
#*  from the actual testbed being used, user may choose to provide certain 
#*  alias/uut information as script arguments.
#*
#*  the idea behind it is simple: decouple the testscript from hard-coding
#*  device and interface/link names in the script by:
#*      - providing a label mapping from the jobfile, and/or
#*      - using the topology alias feature.
#*
#*  topology module/objects supports alias-lookups: refering to testbed devices,
#*  links and interfaces by an 'alternative name', which maps to the actual HW
#*  names defined in testbed YAML file. See documentation on alias here:
#*  URL= http://wwwin-pyats.cisco.com/documentation/html/topology/usage.html
#*
#*  in addition, users may also choose to provide a dictionary argument, mapping
#*  labels referenced in the testscript vs actual device names, and make use of
#*  this information within their testscripts. Eg:
#*      labels = {
#*          'pe1': 'device_one',
#*          'uut': 'device_two',
#*      }
#*
#*  it is also a good idea to pass in a list of devices and links to be used
#*  by the testscript. This allows configurability of the testscripts, and
#*  choosing which links/interfaces/devices of the current topology to test on.
#*      routers = ['device_one', 'device_two', 'device_three']
#*      links = ['link_one', 'link_two', 'link_three']
#*      tgns = []
#*
#*  Handling Multiple Testbeds
#*  --------------------------
#*   in the case where your job file is shared across multiple testbeds, you can
#*   test for the current testbed object and set your topology information 
#*   accordingly. Eg:
#*
#*      if runtime.testbed:
#*
#*          if runtime.testbed.name == 'testbed_ONE':
#*              labels = {<label mapping for testbed_ONE>}
#*              routers = [<routers to use for testbed_ONE>]
#*              links = [<links to use for testbed_ONE]
#*              tgns = [<tgns to use for testbed_ONE]
#*
#*          elif runtime.testbed.name == 'testbed_TWO'
#*              labels = {<label mapping for testbed_TWO>}
#*              routers = [<routers to use for testbed_TWO>]
#*              links = [<links to use for testbed_TWO]
#*              tgns = [<tgns to use for testbed_TWO
#*
#*      else:
#           # if your script requires a testbed topology, this is a good place
#*          # to throw an exception
#*          raise ValueError('testbed file not provided by -testbed_file')
#*
#*  note - this is simply a typical use-case of aetest testscript arguments. It
#*  is not a hard-coded requirement/input to the infrastructure.
#*******************************************************************************

#
# topology references example definitions
#
labels = {}
routers = []
links = []
tgns = []


#*******************************************************************************
#* MAIN FUNCTION
#*
#*  Each job file must have a main() function where testscripts/task runs are
#*  defined. After a job file is imported, easypy will lookup main() function
#*  to run. 
#*
#*  main() funtion shall have a single argument called 'runtime'. This allows
#*  the engine to automatically pass in the current Easypy runtime object. The
#*  following should be performed within the main() function:
#*      - parse any custom command-line arguments
#*      - configure logger log-levels, if any
#*      - run each and every testscript file
#*
#*  Examples
#*  --------
#*      
#*      def main(runtime):
#*
#*          # do parse command line job file arguments
#*          args = parser.parse_known_args()
#*
#*          # configure some loggers
#*          logging.getLogger('ats.aetest').setLevel('DEBUG')
#*          logging.getLogger('mymodule.myfeature').setLevel('INFO')
#*
#*          # simple run
#*          run(testscript = "/path/to/my/script.py", runtime = runtime)
#*
#*          # specify a custom task id
#*          run(testscript = "/path/to/my/script.py",
#*              task_id = "custom_task_id",
#*              runtime = runtime)
#*
#*          # passing script arguments from job file to script
#*          run(testscript = "/path/to/my/script.py",
#*              task_id = "custom_task_id",
#*              runtime = runtime,
#*              script_arg_1 = 'some value 1',
#*              script_arg_2 = 'some value 2',
#*              script_arg_x = 'some value X')
#*
#*          # calling with AEtest options
#*          run(testscript = "/path/to/my/script.py",
#*              submitter = 'chambers',
#*              runtime = runtime)
#*
#*          # making life complicated
#*          run(testscript = "/path/to/my/script.py",
#*              runtime = runtime,
#*              task_id = "custom_task_id",
#*              script_arg_1 = 'some value 1',
#*              script_arg_2 = 'some value 2',
#*              script_arg_x = args.myargument,
#*              submitter = 'chambers')
#*
#*  for detailed jobfile description, visit:
#*  URL= http://wwwin-pyats.cisco.com/documentation/html/easypy/jobfile.html
#*
#*  for detailed list of aetest arguments, visit:
#*  URL=http://wwwin-pyats.cisco.com/documentation/html/aetest/run.html
#*
#*******************************************************************************


#*******************************************************************************
#* SCRIPT ARGUMENTS
#*
#*  Aside from standard run() and aetest infrastructure arguments, all other 
#*  keyword arguments (*kwargs) to run() api are effectively script arguments.
#* 
#*  Once passed to the testscript, script arguments are updated into testscript
#*  parameters for this run, accessible throughout script sections using the
#*  test-parameters feature. In effect, testcase parameters is a superset of 
#*  of the testscript parameters, which itself contains jobfile arguments.
#*      
#*          +---------------------------------------------+
#*          | +----------------------------+     testcase |
#*          | | +-----------+   testscript |   parameters |
#*          | | | Job File  |   parameters |              |
#*          | | | arguments |              |              |
#*          | | +-----------+              |              |
#*          | +----------------------------+              |
#*          +---------------------------------------------+
#*  
#*  if any jobfile arguments names clash with existing testscript parameters, 
#*  it will overwrite the one from the testscript. This allows users to set
#*  default testscript parameters within the script, and use job file arguments
#*  to overwrite them.
#*                          overwrites
#*      Jobfile Arguments --------------> TestScript Parameters.
#*
#* For more details on test parameters, refer to:
#* URL= http://wwwin-pyats.cisco.com/documentation/html/aetest/parameters.html
#*******************************************************************************


# compute the script path from this location
script_path = os.path.join(os.path.dirname(__file__), '..')

# 
# main logic, run testscripts inside
#
def main(runtime):
    
    # parse custom command-line arguments
    custom_args = parser.parse_known_args()[0]
 
    #**************************************
    #* Log Levels
    #*
    #*  within the job file main() section, you can set the various logger's
    #*  loglevels for your following testscripts. This allows users to modify
    #*  the logging output within the job file, for various modules & etc,
    #*  without modifying testscript and libraries.

    # set log levels for various modules
    # eg, set aetest to INFO, set your library to DEBUG
    logging.getLogger('ats.aetest').setLevel('INFO')
    logging.getLogger('libs').setLevel('DEBUG')

    #
    # run the template script
    # 
    run(testscript= os.path.join(script_path, 'template.py'),
        runtime = runtime,
        labels = labels,
        routers = routers,
        links = links,
        tgns = tgns)

    #
    # run the variant script with custom args
    # 
    run(testscript= os.path.join(script_path, 'variant.py'),
        runtime = runtime,
        **vars(custom_args))

    #**************************************
    #* Run by ID
    #*
    #*  use 'uids' feature to specify which test section uids should run.
    #*  'uids' accepts a callable argument. In this example, instead of writing
    #*  a callable function, we'll leverage datastructure.logic classes.
    #*
    #*  Read More:
    #*  http://wwwin-pyats.cisco.com/documentation/html/aetest/control.html

    #
    # eg, only run ExampleTestcase
    #
    run(testscript= os.path.join(script_path, 'template.py'),
        runtime = runtime,
        uids = Or('ExampleTestcase'))

    #**************************************
    #* Run by Groups
    #*
    #*  use 'groups' feature to specify which testcase groups should run.
    #*  'groups' accepts a callable argument. In this example, we'll also be
    #*  using datastructure.logic classes.
    #*
    #*  Read More:
    #*  http://wwwin-pyats.cisco.com/documentation/html/aetest/control.html

    #
    # eg, only run testcases in group_A 
    #
    run(testscript= os.path.join(script_path, 'variant.py'),
        runtime = runtime,
        groups = Or('group_A'))
