"""

Abstract Factory Design pattern
"""

from .DiskCrawler import DiskCrawler
import logging

logger = logging.getLogger("Alyke")

class CrawlerFactory():
    """
    Declare an interface for operations that create crawler objects.
    
    """
    @staticmethod
    def create_crawler(name, base_path):
        if name == 'disk':
            logging.info('Creating a disk crawler')
            return DiskCrawler(base_path)

        logger.error('Failed to open file', exc_info=True)
        raise NotImplementedError