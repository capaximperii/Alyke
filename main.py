"""
Entry point of the program.

"""
import time
import logging
from alyke import App

def setup_logging(log_level):
    logger = logging.getLogger("Alyke")
    handler =logging.FileHandler('alyke.log')
    logger.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

if __name__ == '__main__':
    start_time = time.time()
    app = App()
    logger = setup_logging(app.config.log_level)
    logger.debug("--- Starting ---")
    app.find_duplicates()
    logger.debug("--- %s seconds ---" % (time.time() - start_time))

