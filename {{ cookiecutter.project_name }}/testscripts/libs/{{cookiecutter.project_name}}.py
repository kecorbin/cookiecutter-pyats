

'''{{ cookiecutter.project_name}}.py

Shared code used by  {{ cookiecutter.project_name}}

{{ cookiecutter.project_description }}

References:
    < provide references here. >

Notes:
    < provide notes if needed >
'''

# optional author information
# optional author information
__author__ = '{{cookiecutter.author_name}}'
__copyright__ = 'Copyright (c) 2017, Cisco Systems Inc.'
__contact__ = ['{{cookiecutter.author_email}}']
__version__ = 1.0


#
# import statements
#
import logging

#
# create a logger for this module
#
logger = logging.getLogger(__name__)


# ****************************************************************************
# * Function & Class Defitions
# *
# *  Local library functions should support the use of steps: creating smaller
# *  steps within test sections to identify the actions taken in a library
# *  function.
# *
# *  to use step in your functions, provide it the current step object, and
# *  create further step swithin your functions.
def {{cookiecutter.project_name}}(step):
    ''' helper / library function

    This function demonstrate the use of steps within function APIs. This
    enables smaller breakdown of functions into smaller steps, and thus
    provides finer granuality in your testscript logs.

    Arguments
    ---------
        steps   (obj): the step object to be passed in from the testscript

    '''

    with step.start('testscripts.libs.{{cookiecutter.project_name}} step one'):
        # do some meaningful testing
        logger.info('testscripts.libs.{{cookiecutter.project_name}} step one')

    with step.start('testscripts.libs.{{cookiecutter.project_name}} step two'):
        # do some meaningful testing
        logger.info('testscripts.libs.{{cookiecutter.project_name}} step two')


    return
