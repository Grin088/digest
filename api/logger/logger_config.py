import os

path_to_log_file = os.path.abspath("logger/logs/digest.log")
os.makedirs(os.path.dirname(path_to_log_file), exist_ok=True)

logger_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "base": {
            "format": "%(levelname)s | %(asctime)s | %(filename)s:%(lineno)d | %(message)s\n",
        },
        "with_traceback": {
            "format": "%(levelname)s | %(asctime)s | %(filename)s:%(lineno)d  | %(message)s\n"
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "base",
            "stream": "ext://sys.stdout",
        },
        "file": {
            "class": "logging.handlers.TimedRotatingFileHandler",
            "level": "DEBUG",
            "formatter": "with_traceback",
            "filename": path_to_log_file,
            "when": "D",
            "interval": 7,
            "backupCount": 5,
            "encoding": "utf-8",
            "utc": False,
        },
    },
    "loggers": {
        "logger": {
            "level": "DEBUG",
            "handlers": ["console", "file"],
            "exc_info": True,
        }
    },
}
