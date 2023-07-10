import datetime
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def run(event, context):
    space = os.environ['AWS_PARAMETER_SPACE']
    current_time = datetime.datetime.now().time()
    name = context.function_name
    logger.info("Your space: " + space +",Your cron function: " + name + " ran at " + str(current_time))
