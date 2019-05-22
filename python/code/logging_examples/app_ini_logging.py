import logging
import logging.config

from logged_library import printer


def main():
    logging.config.fileConfig("config.ini")
    logger = logging.getLogger()
    logger.debug("root_print")
    printer.log_print_info("log_print")
    printer_class = printer.Printer()
    printer_class.log_class_print_warning("log_print_class")


if __name__ == '__main__':
    main()
