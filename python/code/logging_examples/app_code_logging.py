import logging
import os
import sys

from logged_library import printer


def config_logger(root_level, library_level):
    logger = logging.getLogger()

    # Configure root console logger
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s %(levelname)-s:%(module)-s:%(funcName)-s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Configure root file logger
    log_filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "file.log")
    handler = logging.FileHandler(log_filepath, mode='a')
    formatter = logging.Formatter('%(asctime)s %(levelname)-s:%(module)-s:%(funcName)-s: %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    logger.setLevel(root_level)

    # Configure library level
    logger = logging.getLogger("logged_library")
    logger.setLevel(library_level)


def main():
    config_logger(root_level=logging.DEBUG, library_level=logging.ERROR)

    logger = logging.getLogger()
    logger.debug("root_print")
    printer.log_print_info("log_print")
    printer_class = printer.Printer()
    printer_class.log_class_print_warning("log_print_class")


if __name__ == '__main__':
    main()



