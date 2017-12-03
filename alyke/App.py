"""

Represents the application as a module.
"""
from collections import defaultdict
from alyke.Config import Config
from crawler import CrawlerFactory
from settings import config as cfg
import logging

logger = logging.getLogger("Alyke")

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
        filecount = 0
        groupcount = 0
        dupcount = 0
        hashlist = []
        for resource in self.crawler:
            filecount += 1
            resource.compute_digest()
            hashlist.append(resource.get())
        # Group all elements with same dictionary value.
        HASHES = defaultdict(list)
        for k, v in hashlist:
            HASHES[k].append(v)
        for k,dups in HASHES.items():
            if len(dups) > 1:
                dupcount += len(dups) - 1 # Coz 1 file is original
                groupcount += 1
                logger.info("Duplicate Group : %d:" %(groupcount))
                list(map(lambda x: print("\t%s" %(x)), dups))
        logger.info("Found total %d duplicates in %d groups out of %d files.", dupcount, groupcount, filecount)
        logger.info("%d percent Duplicate " % (100 * dupcount / filecount))