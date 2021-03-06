
'''Test{{cookiecutter.testcase_class}}Device.py

These test cases will be ran against each device in the testbed

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


# Local libaries which can contain helpers/etc
from libs import {{cookiecutter.project_name}} as {{cookiecutter.project_name}}


log = logging.getLogger("{{ cookiecutter.project_name}}".upper())


class common_setup(aetest.CommonSetup):
    """ Common Setup section """

    # Mark this test to run against all devices in the testbed
    @aetest.subsection
    def setup(self, testbed):
        # initalize genie testbed
        testbed = Genie.init(testbed)
        # execute check for each device in the testbed using loops
        device_names = [d for d in testbed.devices.keys()]
        aetest.loop.mark({{cookiecutter.testcase_class}}Device,
                         uids=device_names,
                         device=testbed.devices.values())


# TESTCASE DEFINITIONS
#
#  the testcase bodies defined here are to be inherited from your main scripts.
#  any testcase data required should be clearly outlined in its headers, so
#  that when inherited, such data can be provided in the actual testscript.
#
class {{cookiecutter.testcase_class}}Device(aetest.Testcase):
    '''{{ cookiecutter.testcase_class}}

    {{ cookiecutter.testcase_description }}

    Arguments:
        < data required to run this testcase >
    '''

    # Testcase grouping feature enables testcases to be “associated” together by
    # certain keywords, allowing a testscript execution be limited to only running
    # testcases of one or more particular groups that matches up to input
    # criterion.
    groups = ['device_health']

    # Setup Section
    #
    #  setup section is optional within each Testcase. It is always run if
    #  defined. If the setup section's result is not Passed, Passx or Skipped
    #  all test sections will be skipped as a consequence.
    @aetest.setup
    def connect_to_device(self, device):
        '''connect_to_device

        Connects to the device
        '''

        log.info("Connecting to device {}".format(device.name))
        device.connect()

    @aetest.test
    def run_show_version(self, device):
        '''run_show_commands

        runs show version on device
        '''

        log.info("Running show version on {}".format(device.name))
        device.execute('show version')


    # Test Section
    #
    #  each testcase contains one or more tests. Each test is run one after
    #  the other, in their defined order.
    # @aetest.test
    # def collect_info(self, steps, device):
    #     '''collect info
    #
    #     this test collects some operational issue from the device being tested
    #     this is information is used by later test sections
    #     '''
    #
    #     #  use steps whenever possible they are awesome
    #     # steps enables smaller breakdown of functions into smaller steps,
    #     # and thus provides finer granuality in your testscript logs.
    #     with steps.start('Parse Static Routes'):
    #         routing_cls = get_ops('static_routing', device)
    #         routing = routing_cls(device)
    #         routing.learn()
    #         log.info("Routing Info: {}".format(routing.info))
    #
    #     # with steps.start('Check Platform Info'):
    #     #     platform_class = get_ops('platform', device)
    #     #     platform = platform_class(device)
    #     #     platform.learn()
    #     #     log.info("Device Version: {}".format(platform.version))
    #     #     log.info("Serial Number: {}".format(platform.chassis_sn))
    #
    #     with steps.start('Parse ARP Table'):
    #         arp_cls = get_ops('arp', device)
    #         arp = arp_cls(device)
    #         arp.learn()
    #         log.info("ARP Info: {}".format(arp.info))

    # looped test section
    # both iterations are run per testcase iteration
    # @aetest.loop(uids=['ping_primary_dns', 'ping_secondary_dns'],
    #              addr=['4.2.2.2', '8.8.8.8'])
    # @aetest.test
    # def test_dns_reachability(self, device, addr):
    #     '''Test DNS reachability
    #
    #     this test issues a ping to the primary and secondary DNS servers
    #     '''
    #
    #     output = device.ping(addr=addr)
    #     log.info(output)

    # always run last in a testcase, the cleanup section is optional, and,
    # when defined, runs regardless of previous testcase/setup pass/fail
    # results.
    @aetest.cleanup
    def cleanup(self):
        '''{{ cookiecutter.testcase_class}} cleanup

        any other cleanup activities can be done here.
        '''

        pass
