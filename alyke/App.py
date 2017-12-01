
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
            if resource.digest in HASHES.keys():
                print("Found duplicate file: %s of %s" % (resource.path, HASHES[resource.digest]))
                count += 1
            else:
                HASHES[resource.digest] = resource.path
        if count == 0:
            print("No duplicates found.")
        else:
            print("Duplicates found:", count)