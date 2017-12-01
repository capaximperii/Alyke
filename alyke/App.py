import hashlib

from alyke.Config import Config
from crawler import CrawlerFactory
from settings import config

HASHES = {}

class App(object):
    def __init__(self):
        self.config = Config(config)
        self.crawler = CrawlerFactory.create_crawler(self.config.crawler_type, self.config.base_path)

    def find_duplicates(self):
        count = 0
        for resource in self.crawler:
            file = resource.open('rb')
            hash = hashlib.sha512()
            # https://docs.python.org/3/library/functions.html#iter
            for part in iter(lambda: file.read( 4 * 1024 * 1024), b''):
                hash.update(part)
            digest = hash.digest()
            if digest in HASHES.keys():
                print("Found duplicate file: {0} of {1}", (resource.absolute(), HASHES[digest]))
                count += 1
            else:
                HASHES[digest] = resource.absolute()
        if count == 0:
            print("No duplicates found.")
        else:
            print("Duplicates found:", count)