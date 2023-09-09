import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    level =logging.DEBUG
)
logger = logging.getLogger('Custom Log')
logger.debug('Debug Message')
logger.error('Some Error Happened')
logger.warning('Warning message')