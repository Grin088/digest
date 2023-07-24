from logging import getLogger, config
from api.logger.logger_config import logger_config


logger = getLogger("logger")
config.dictConfig(logger_config)
