import logging


def log_print_info(text):
    logger = logging.getLogger(__name__)
    logger.info(text)


class Printer:
    def __init__(self):
        self._logger = logging.getLogger(__name__ + "." + self.__class__.__name__)

    def log_class_print_warning(self, text):
        self._logger.warning(text)


