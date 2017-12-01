from .FsCrawler import FsCrawler

class CrawlerFactory():
    """
    Declare an interface for operations that create abstract product
    objects.
    """
    @staticmethod
    def create_crawler(name, base_path):
        if name == 'disk':
            return FsCrawler(base_path)

        raise NotImplementedError