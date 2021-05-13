import logging


logger = logging.getLogger("fuga")


class Fuga(object):

    def __init__(self):
        logger.debug("fuga.DEBUG")
        logger.info("fuga.INFO")
        logger.warning("fuga.WARN")
        logger.error("fuga.ERROR")
