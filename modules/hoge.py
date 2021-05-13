import logging


logger = logging.getLogger("hoge")


class Hoge(object):

    def __init__(self):
        logger.debug("hoge.DEBUG")
        logger.info("hoge.INFO")
        logger.warning("hoge.WARN")
        logger.error("hoge.ERROR")
