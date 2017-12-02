"""
Locally connected storage crawler implementation.

"""
import os
import hashlib
from pathlib import Path
from crawler.CrawlerBlueprint import CrawlerBlueprint
from resource import Resource
import logging

logger = logging.getLogger("Alyke")

class DiskCrawler(CrawlerBlueprint):
    """
    Concrete implementation of CrawlerBlueprint class.
    """
    def __init__(self, base):
        """
        Constructor
        :param base: The base path in the filesystem to start exploring from. 
        """
        super(DiskCrawler, self).__init__(base);
        self.path = Path(base)

    def __iter__(self):
        """
        Implements a generator to process one file at a time.
        :return: 
        """
        for f in self.path.glob('**/*'):
            if f.is_file() and not os.stat(str(f.resolve())).st_size == 0:
                # digest = DiskCrawler.compute_digest(str(f.resolve()))
                yield Resource(str(f.resolve()), None)

    @staticmethod
    def partial_reader(filename, chunk_size):
        """
        Generator that reads a file in chunks of bytes
        :param: chunk_size to read from the file
        :return: chunk_size bytes
        """
        try:
            file = open(filename, 'rb')
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    file.close()
                    return
                yield chunk
        except IOError as e:
            logger.error("IOError: %s" %(str(e)), exc_info=True)
            return

    def compute_digest(self):
        """
        Computes a hash depending on the content in the file.
        
        :param path: URL or the resource. 
        :return: SHA-512 digest of the file contents.
        """
        hash = hashlib.sha512()
        for part in DiskCrawler.partial_reader(self.path, 4 * 1024 * 1024):
            hash.update(part)
        self.digest = hash.hexdigest