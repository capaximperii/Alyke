"""

Represents the application as a module.
"""

from alyke.Config import Config
from crawler import CrawlerFactory
from settings import config
import logging

logger = logging.getLogger("Alyke")

HASHES = {}

class App(object):
    """ 
    Encapsulates application logic.
    
    """
    def __init__(self):
        """
        Constructor uses Abstract Factory pattern and instantiates a Crawler depending on 
        settings specified by the user.
        
        """
        self.config = Config(config)
        self.crawler = CrawlerFactory.create_crawler(self.config.crawler_type, self.config.base_path)

    def find_duplicates(self):
        """
        Utility function that walks path and discovers duplicates.
        
        :return: void 
        """
        count = 0
        for resource in self.crawler:
            if resource.digest in HASHES.keys():
                logger.info("Found duplicate file: %s of %s" % (resource.path, HASHES[resource.digest]))
                count += 1
            else:
                HASHES[resource.digest] = resource.path
        if count == 0:
            logger.info("No duplicates found.")
        else:
            logger.info("Duplicates found: %d" % (count))