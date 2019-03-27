# *******************************************************************************
# *                              Template Local Library
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
# *    This is a local library file that lives with the testscript. Local
# *    libraries contains functions, classes & methods local to a testscript
# *    only. Because they are local and are not shared with other
# *    scripts/modules, the use of them should be minimized (not used if
# *    possible). Common code/libraries should be shared with the testing
# *    community in repositories such as xbu_shared.
# *
# * Note:
# *   the use of local library files, and its ideas, are software development
# *   methodologies, and an optional use-case of pyATS testscripts.
# *
# * Read More:
# *   For the complete and up-to-date user guide on AEtest template, visit:
# *   URL= http://wwwin-pyats.cisco.com/documentation/html/aetest/index.html
# *
# *******************************************************************************

'''{{ cookiecutter.project_name}}.py

Shared code used by  {{ cookiecutter.project_name}}

{{ cookiecutter.project_description }}

References:
    < provide references here. >

Notes:
    < provide notes if needed >
'''

# optional author information
__author__ = '{{ cookiecutter.author_name}}'
__contact__ = ["{{ cookiecutter.author_name}}"]
__date__= 'June 15, 2015'
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
def library_function(step):
    '''library_function

    This function demonstrate the use of steps within function APIs. This
    enables smaller breakdown of functions into smaller steps, and thus
    provides finer granuality in your testscript logs.

    Arguments
    ---------
        steps   (obj): the step object to be passed in from the testscript

    '''

    with step.start('library_function step one'):
        # do some meaningful testing
        pass

    with step.start('library_function step two'):
        # do some meaningful testing
        pass

    with step.start('function step three'):
        # do some meaningful testing
        pass

    return
