import time
import os
import logging
from connect.eaas.core.logging import ExtensionLogHandler


if __name__ == "__main__":
    print("Running logzcheck...")
    logger = logging.getLogger('dummy-logger')
    logz_token = os.getenv('LOGZ_TOKEN')
    logger.addHandler(ExtensionLogHandler(logz_token, default_extra_fields={}))
    logger.warning('EAAS INFRA VERIFICATION')
    print("logzcheck finished!")
