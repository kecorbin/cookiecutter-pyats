'''{{cookiecutter.project_name}}_job.py

This is an example docstring for an a job file. The header should describe which
scripts are included as part of this job, their required topology, and any other
information which may concern the person that runs this job.

Purpose:
    This job file examines the `testscripts` directory and runs any testscript
    that is located in this directory.  Any file in this directory with "Test"
    (case-sensitive) is assumed to be a testscript

Usage:
    easypy {{ cookiecutter.project_name }}_job.py  \
      -configuration easypy_config.yaml  \
      -html_log . \
      -testbed_file testbeds/default.yaml \
      --print-timestamp


Description:
    < descriptiveText >

Requirements:
    - < yourRequirements >

Noes:
    <something>

'''
import os
import pathlib
import logging
import argparse

from ats.easypy import run

# import logic statements from datastructures module
from ats.datastructures.logic import And, Or, Not

# allow some settings from local environment
loglevel = os.environ.get('loglevel', 'INFO')
groups = os.environ.get('execution_group', None)
my_variable = os.environ.get('my_variable', 'default_value')

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


# pyATS features argument propagation: propagating custom command
# line arguments to jobfile & the testscript. In a nutshell, the requirement
# is simple: parse only what you need using parse_known_args(), leave the
# rest in sys.argv.
parser = argparse.ArgumentParser(description='example job file cli args parser')
parser.add_argument('--group',
                    action='store',
                    dest='group',
                    help='only run tests in a specific group',
                    default=None)
parser.add_argument('--only-global',
                    action='store_true',
                    dest='only_global',
                    help='Only Run ',
                    default=False)


def get_testscripts():
    '''Run all test scripts in the testscript directory, test scripts are
    identified by whether the filename contains `Test` (case-senstive)
    '''
    testscript_dir = os.path.join(os.path.dirname(__file__), 'testscripts')
    p = pathlib.Path(testscript_dir)
    files = list(p.iterdir())
    testscripts = [str(f) for f in files if 'Test' in str(f)]
    return testscripts

# MAIN FUNCTION
#
# Each job file must have a main() function where testscripts/task runs are
# defined. After a job file is imported, easypy will lookup main() function
# to run.
#
# main() funtion shall have a single argument called 'runtime'. This allows
# the engine to automatically pass in the current Easypy runtime object. The
# following should be performed within the main() function:
#       - parse any custom command-line arguments
#       - configure logger log-levels, if any
#       - run each and every testscript file
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
    logging.getLogger('testscripts.libs').setLevel('DEBUG')

    if custom_args.only_global:
        # only run Test{{ cookiecutter.testcase_class}}

        script_path = os.path.join(os.path.dirname(__file__), 'testscripts')
        testscript = os.path.join(script_path,
                                  'Test{{ cookiecutter.testcase_class}}.py')
        run(testscript=testscript,
            datafile='data/datafile.yaml',
            runtime=runtime,
            uids=Or('{{ cookiecutter.testcase_class }}'))

    # limit tests to a specific group
    elif custom_args.group:
        for script in get_testscripts():
            run(testscript=script,
                runtime=runtime,
                labels=labels,
                routers=routers,
                links=links,
                tgns=tgns,
                groups = Or(custom_args.group),
                **vars(custom_args))

    else:

        for script in get_testscripts():
            run(testscript=script,
                runtime=runtime,
                labels=labels,
                routers=routers,
                links=links,
                tgns=tgns,
                **vars(custom_args))


    #
