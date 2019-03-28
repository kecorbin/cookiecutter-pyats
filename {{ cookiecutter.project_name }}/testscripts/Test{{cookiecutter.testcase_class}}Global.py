# *******************************************************************************
# *                              Template Testcases
# * ----------------------------------------------------------------------------
# * ABOUT THIS TEMPLATE - Please read
# *
# * - Any comments with "#*" in front of them (like this entire comment box) are
# *   for template clarifications only and should be removed from the final
# *   product.
# *
# * - Anything enclosed in <> must be replaced by the appropriate text for your
# *   application
# *
# * Author:
# *    Siming Yuan, Automation Strategy - Core Software Group (CSG)
# *
# * Support:
# *    pyats-support@cisco.com
# *
# * Description:
# *  This file contains some template testcases used by template base and variant
# *  script. It serves as an example demonstrating the usage & benefits of using
# *  testcase files.
# *
# * Note:
# *   instead of duplicating information, this template file will only expand
# *   on details where necessary. You may refer to template.py for details.
# *
# * Note Also:
# *   the use of testcase files, and its ideas, are software development
# *   methodologies, and an optional use-case of pyATS testscripts.
# *
# * Read More:
# *   For the complete and up-to-date user guide on AEtest template, visit:
# *   URL= https://developer.cisco.com/site/pyats/
# *
# *******************************************************************************

'''template_testcases.py

< describe your testcases >

Arguments:
    <name> (<type>): <description of your testscript argument>

Testcases:
    < provide examples on how to use this test script. >

References:
    < provide references here. >

Notes:
    < provide notes if needed >
'''

# optional author information
__author__ = '{{cookiecutter.author_name}}'
__copyright__ = 'Copyright (c) 2017, Cisco Systems Inc.'
__contact__ = ['{{cookiecutter.author_email}}']
__version__ = 1.0


#
# imports statements
#
import logging
from ats import aetest
from ats.log.utils import banner
from genie.conf import Genie

try:
    from genie.ops.utils import get_ops
except ModuleNotFoundError:
    from genie.ops.base import get_ops

# **********************************
# * Using Local Libraries
import libs.{{cookiecutter.project_name}}
import processors.{{cookiecutter.project_name}} as processors

log = logging.getLogger(__name__)

# *******************************************************************************
# * TESTCASE DEFINITIONS
# *
# *  the testcase bodies defined here are to be inherited from your main scripts.
# *  any testcase data required should be clearly outlined in its headers, so
# *  that when inherited, such data can be provided in the actual testscript.
# *
# * Docs
# * https://pubhub.devnetcloud.com/media/pyats/docs/aetest/structure.html#testcases
@aetest.processors(pre=[processors.pre_processor],
                   post=[processors.post_processor],
                   exception=[processors.exception_processor])
class {{ cookiecutter.testcase_class }}Global(aetest.Testcase):
    '''{{ cookiecutter.testcase_class}}

    {{ cookiecutter.testcase_description }}

    Arguments:
        < data required to run this testcase >
    '''

    # **********************************
    # * Setup Section
    # *
    # *  setup section is optional within each Testcase. It is always run if
    # *  defined. If the setup section's result is not Passed, Passx or Skipped,
    # *  all test sections will be skipped as a consequence.
    @aetest.setup
    def setup(self):
        '''{{ cookiecutter.testcase_class}} Setup

        setup required by {{ cookiecutter.testcase_class}}
        '''

        pass

    # **********************************
    # * Test Section
    # *
    # *  each testcase contains one or more tests. Each test is run one after
    # *  the other, in their defined order.
    @aetest.test
    def section1(self, steps):
        '''section1

        section1 description goes here
        '''

        # **********************************
        # * Testcase Steps
        # *
        # *  testcases should always leverage the steps feature of AEtest. Doing
        # *  so provides more visual clues of the actions taken of each section
        # *  and so on.
        # *
        # *  Steps is applicable to subsections, setups, tests and cleanups
        # *
        # *  Full documentation here:
        # *  https://pubhub.devnetcloud.com/media/pyats/docs/aetest/steps.html
        with steps.start('one small step for [a] man'):
            log.info('one small step for [a] man')

        with steps.start('one giant leap for mankind'):
            log.info('one giant leap for mankind')

        with steps.start('nested steps from external lib') as step:
            libs.{{ cookiecutter.project_name}}.{{cookiecutter.project_name}}(step)


    #**********************************
    #* Cleanup Section
    #*
    #*  always run last in a testcase, the cleanup section is optional, and,
    #*  when defined, runs regardless of previous testcase/setup pass/fail
    #*  results.
    @aetest.cleanup
    def cleanup(self):
        '''{{ cookiecutter.testcase_class}} cleanup

        < docstring description of this cleanup >
        '''

        pass
