"""

Represents the application as a module.
"""
from multiprocessing import Pool

from alyke.Config import Config
from crawler import CrawlerFactory
from settings import config as cfg
import logging

logger = logging.getLogger("Alyke")

HASHES = {}

def hash_check(resource):
    resource.compute_digest()
    return resource

def print_result(resource):
    if resource.digest in HASHES.keys():
        logger.info("Found duplicate file: %s of %s" % (resource.path, HASHES[resource.digest]))
    else:
        HASHES[resource.digest] = resource.path


class App(object):
    """ 
    Encapsulates application logic.
    
    """
    def __init__(self, cmdline):
        """
        Constructor uses Abstract Factory pattern and instantiates a Crawler depending on 
        settings specified by the user.
        
        """
        # Remove all unset values.
        cmdline = dict((k, v) for k, v in cmdline.items() if v is not None)
        self.config = Config(cfg)
        self.config.update(cmdline)
        self.crawler = CrawlerFactory.create_crawler(self.config.crawler_type, self.config.base_path)


    def find_duplicates(self):
        """
        Utility function that walks path and discovers duplicates.
        
        :return: void 
        """
        pool = Pool(processes=10)
        for i in self.crawler:
            pool.apply_async(hash_check, args=(i,), callback=print_result)
        pool.close()
        pool.join()