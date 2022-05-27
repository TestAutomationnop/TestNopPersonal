import logging


def loggen():
    logging.basicConfig(filename="my_log_file.log", filemode='w', format='%(asctime)s %(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p')
    logger = logging.getLogger('Example')
    logger.setLevel(logging.INFO)
    return logger
