"""
Alyke: Duplicate file detector.

Usage:
  main.py [--crawler_type=<type>] [--base_path=<path>]
  main.py -h | --help

Options:
  -h --help     Show this screen.
  --crawler_type=<type>  One of disk, web.
  --base_path=<path> URL to start checking from
"""

import time
import logging
from docopt import docopt
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
    cmdline = docopt(__doc__)
    app = App(cmdline)
    logger = setup_logging(app.config.log_level)
    logger.debug("--- Starting ---")
    app.find_duplicates()
    logger.debug("--- %s seconds ---" % (time.time() - start_time))

