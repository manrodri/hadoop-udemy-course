import logging


# Create logger custom class
class Logger(object):
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)

        # Create file handler
        self.fh = logging.FileHandler('logger.log')
        self.fh.setLevel(logging.DEBUG)

        # Create console handler
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)

        # Create formatter
        self.formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

        # Add formatter to handlers
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)

        # Add handlers to logger
        self.logger.addHandler(self.fh)
        self.logger.addHandler(self.ch)

    def add_new_formatter(self, new_format):
        self.formatter = logging.Formatter(new_format)
        self.fh.setFormatter(self.formatter)
        self.ch.setFormatter(self.formatter)

    def add_group_tag(self):
        group_tag = '##[group]'
        self.add_new_formatter(group_tag + ' ' + self.formatter._fmt)

    def remove_group_tag(self):
        self.add_new_formatter(self.formatter._fmt.replace('##[group] ', ''))

    def get_logger(self):
        return self.logger


def main():
    # Create logger object
    my_logging_instance = Logger('logger')
    logger = my_logging_instance.get_logger()

    # Log some messages
    logger.info('This is an info message')

    # add new formatter to handlers
    my_logging_instance.add_group_tag()
    logger.info('This is an info message')
    my_logging_instance.remove_group_tag()
    logger.info('This is an info message')


# run this file as script
if __name__ == '__main__':
    main()
