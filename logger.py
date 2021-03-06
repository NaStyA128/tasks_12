from logging.config import dictConfig
import logging
import requests


class SpaceHandler(logging.Handler):

    def __init__(self, src, *args, **kwargs):
        self.src = src
        super().__init__(*args, **kwargs)

    def emit(self, record):
        resp = requests.post(
            'http://127.0.0.1:8000/login/',
            {
                'username': 'admin',
                'password': '456756yfcnz',
            }
        )
        cookies = dict(sessionid=resp.cookies["sessionid"])

        resp_two = requests.post(
            'http://127.0.0.1:8000/',
            cookies=cookies,
            data={
                'level': record.levelname,
                'name_logger': record.name,
                'message': record.getMessage(),
            }
        )
        # print(record.getMessage())


logging_config = dict(
    version=1,
    formatters={
        'f': {'format':
              '[%(asctime)s] [%(name)-12s] [%(levelname)-8s] [%(message)s]'}
        },
    handlers={
        'h': {'class': 'logging.StreamHandler',
              'formatter': 'f',
              'level': logging.DEBUG}
        },
    root={
        'handlers': ['h'],
        'level': logging.DEBUG,
        },
)

dictConfig(logging_config)

logger = logging.getLogger('spam_application')
logger.setLevel("DEBUG")


# create console handler with a higher log level
# ch = logging.StreamHandler()
space_handler = SpaceHandler('http://127.0.0.1:8000/')
# ch.setLevel("DEBUG")
space_handler.setLevel("DEBUG")

# create formatter and add it to the handlers
formatter = logging.Formatter()

# ch.setFormatter(formatter)
space_handler.setFormatter(formatter)
# logger.addHandler(ch)
logger.addHandler(space_handler)

# logger.debug('debug')
logger.info('info')
# logger.warning('warning')
# logger.error('error')
# logger.critical('critical')
