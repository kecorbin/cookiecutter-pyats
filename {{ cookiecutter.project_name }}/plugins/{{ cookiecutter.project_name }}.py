# Example
# --------
#
#   {{ cookiecutter.project_name }} plugin

import logging
import argparse
import datetime

from pyats.easypy.plugins.bases import BasePlugin

logger = logging.getLogger("{{ cookiecutter.project_name }}_PLUGIN".upper())

class {{ cookiecutter.project_name }}Plugin(BasePlugin):
    '''{{ cookiecutter.project_name }} plugin

    Runs before and after each job and task, saluting the world and printing
    out the job/task runtime if a custom flag is used.
    '''

    # each plugin may have a unique name
    # set it by setting the 'name' class variable.
    # (defaults to the current class name)
    name = '{{ cookiecutter.project_name }}Plugin'

    # each plugin may have a parser to parse its own command line arguments.
    # these parsers are expected to add arguments to the main easypy parser
    @classmethod
    def configure_parser(cls, parser, legacy_cli=False):
        '''
        plugin parser configurations

        Arguments
        ---------
            parser: main program parser to update
            legacy_cli: boolean indicating whether to support legacy args or
                        not
        '''
        # always create a plugin's own parser group
        parser = parser.add_argument_group("My Hello World")

        # custom arguments shall always use -- as prefix
        # positional custom arguments are NOT allowed.
        parser.add_argument('--print-timestamp',
                            action = 'store_true',
                            default = False)

    # plugins may define its own class constructor __init__, though, it
    # must respect the parent __init__, so super() needs to be called.
    # any additional arguments defined in the plugin config file would be
    # passed to here as keyword arguments
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    # define your plugin's stage actions as methods
    # as this plugin should run pre and post job
    # we need to deifne 'pre_job' and 'post_job' methods.

    # define the pre-job action
    # if 'job' is specified as a function argument, the current Job
    # object is provided as input to this action method when called
    def pre_job(self, job):

        # plugin parser results are stored under self.runtime.args
        if self.runtime.args.print_timestamp:
            self.job_start = datetime.datetime.now()
            logger.info('Current time is: %s' % self.job_start)

        logger.info('Pre-Job %s: Hello World!' % job.name)

    # define post_job action
    def post_job(self, job):

        if self.runtime.args.print_timestamp:
            self.job_end = datetime.datetime.now()
            logger.info('Job run took: %s' % self.job_end - self.job_start)

        logger.info('Post-Job %s: Hello World!' % job.name)

    # similarly, with pre and post-task methods
    # if a 'task' argument is specified as a function argument, the current
    # Task object is provided as input to this action method on call.
    def pre_task(self, task):
        if self.runtime.args.print_timestamp:
            self.task_start = datetime.datetime.now()
            logger.info('Current time is: %s' % self.task_start)

        logger.info('Pre-Task %s: Hello World!' % task.taskid)

    def post_task(self, task):
        if self.runtime.args.print_timestamp:
            self.task_end = datetime.datetime.now()
            logger.info('Task run took: %s' %
                        self.task_end - self.task_start)

        logger.info('Post-Task %s: Hello World!' % task.taskid)
