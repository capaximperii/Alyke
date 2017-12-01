from crawler.CrawlerBlueprint import CrawlerBlueprint
from pathlib import Path
from resource import Resource
import hashlib
import os

class FsCrawler(CrawlerBlueprint):
    def __init__(self, base):
        super(FsCrawler, self).__init__( base);
        self.path = Path(base)

    def __iter__(self):
        for f in self.path.glob('**/*'):
            if f.is_file() and not os.stat(str(f.resolve())).st_size == 0:
                digest = FsCrawler.compute_digest(str(f.resolve()))
                yield Resource(str(f.resolve()), digest)

    @staticmethod
    def partial_reader(filename, chunk_size):
        """Generator that reads a file in chunks of bytes"""
        try:
            file = open(filename, 'rb')
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    return
                yield chunk
        except IOError as e:
            # TODO: Log
            return

    @staticmethod
    def compute_digest(path):
        hash = hashlib.sha512()
        for part in FsCrawler.partial_reader(path, 4 * 1024 * 1024):
            hash.update(part)
        return hash.digest()