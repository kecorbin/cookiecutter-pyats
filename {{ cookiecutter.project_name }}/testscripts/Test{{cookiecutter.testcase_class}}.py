'''Test{{cookiecutter.testcase_class}}.py

Runs some overall tests

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

logger = logging.getLogger(__name__)

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
class {{ cookiecutter.testcase_class }}(aetest.Testcase):
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
    def yak_shaving(self):
        '''yak_shaving

        sometimes you have to do a little yak shaving
        https://seths.blog/2005/03/dont_shave_that/

        '''
        logger.info('Beginning Setup: {}'.format(__name__))


    # Test Section
    # each testcase contains one or more tests. Each test is run one after
    # the other, in their defined order.
    @aetest.test
    def hello_world(self):
        main_idea = "Execute some python code"
        logger.info('code ran with no errors, test will pass')

    @aetest.test
    def to_pass_or_not_to_pass(self):
        logger.info("determining whether something worked or not")
        worked = True
        if worked:
            self.passed('send out the all clear signal')
        else:
            self.failed('or the bat signal')

    @aetest.test
    def errors_arent_failures(self):
        # you can either handle exceptions, or raise them for ERROR result
        try:
            raise Exception
        except Exception:
            pass

        logger.info("shit happens...you don't have to catch it")
        raise Exception("sometimes you do")

    # Tests can pass data to one another by
    # updating `self` to share within the testcase, or `self.parent` to share
    # across testcases
    @aetest.test
    def load_datafile_config(self, expected_routes):
        logger.info('Expected Routes: {}'.format(expected_routes))
        self.expected_routes = expected_routes

    @aetest.test
    def access_prev_info(self):
        logger.info('Expected Routes: {}'.format(self.expected_routes))


    @aetest.test
    def crawl_walk_run(self, steps):
        '''crawl_walk_run

        some common steps patterns
        '''
        # testcases should always leverage the steps feature of AEtest. Doing
        # so provides more visual clues of the actions taken of each section
        # and so on.
        # Full documentation here
        # https://pubhub.devnetcloud.com/media/pyats/docs/aetest/steps.html
        with steps.start('Crawl') as step:
            logger.info('crawling ')

        with steps.start('Walk') as step:

            with step.start('one foot'):
                logger.info('one foot')

            with step.start('in front of the other'):
                logger.info('in front of the other')

        with steps.start('Run (any pyhon code)'):
            logger.info('here are some pointers')
            import this

        with steps.start('Run (your existing code)') as step:
            libs.{{ cookiecutter.project_name}}.{{cookiecutter.project_name}}(step)


    #  always runs last in a testcase, the cleanup section is optional, and,
    #  when defined, runs regardless of previous testcase/setup pass/fail
    #  results.
    @aetest.cleanup
    def cleanup_after_yourself(self):
        '''{{ cookiecutter.testcase_class}} cleanup

        < docstring description of this cleanup >
        '''
        logger.info('Beginning Cleanup: {}'.format(__name__))
        pass
