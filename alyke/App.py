"""

Represents the application as a module.
"""
from multiprocessing import Pool
from multiprocessing import cpu_count
from multiprocessing import Manager

from alyke.Config import Config
from crawler import CrawlerFactory
import crawler
from settings import config as cfg
import logging

logger = logging.getLogger("Alyke")

MANAGER = Manager()
QUEUE = MANAGER.Queue()
HASHES = {}

def hash_check(queue):
    """
    Helper function to compute hashes in multiprocess for extensibility.
    :params: queue The job queue containing resource
    :return: resource after digest computation

    """
    resource = queue.get()
    strategy_module = resource.compute_digest.__module__.split('.')[1]
    strategy_implementation = resource.compute_digest.__name__
    module = getattr(crawler, strategy_module)
    cls = getattr(module, strategy_module)
    compute_digest = getattr(cls, strategy_implementation)
    digest = compute_digest(resource.path)
    resource.set(digest)
    return resource

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
        self.count = 0

    def find_duplicates(self):
        """
        Utility function that walks path and discovers duplicates.

        :return: void 
        """
        pool = Pool(processes=cpu_count() * 2)
        for resource in self.crawler:
            QUEUE.put(resource)
            pool.apply_async(hash_check, args=(QUEUE,), callback=self.print_result)
        pool.close()
        pool.join()
        logger.info("Found %d duplicates" % (self.count))

    def print_result(self, resource):
        """
        Checks hash and prints result to the console and log.
        :params: resource containing file name and hash
        :return: None
        """
        if resource.digest in HASHES.keys():
            self.count += 1
            logger.info("Found duplicate file: %s of %s" % (resource.path, HASHES[resource.digest]))
        else:
            HASHES[resource.digest] = resource.path
