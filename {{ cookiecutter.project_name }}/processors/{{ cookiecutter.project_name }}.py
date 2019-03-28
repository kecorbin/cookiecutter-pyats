
import logging

logger = logging.getLogger("{{ cookiecutter.project_name }}_PROCESSORS".upper())

# define a function that prints the section's uid
def pre_processor(section):
    print('running pre_processor for section: {}'.format(section.uid))

# define a function that prints the section result
def post_processor(section):
    logger.info('post_processor, section result: {}'.format(section.result))

# define another function that prints the exception message and suppress the
# exception
def exception_processor(section, exc_type, exc_value, exc_traceback):

    logger.info('Exception Processor Handling : {}:{}'.format(exc_type,
                                                     exc_value))

    # apply some corrective action
    return True
