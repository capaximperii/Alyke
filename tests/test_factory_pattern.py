from crawler import CrawlerFactory
from crawler.DiskCrawler import DiskCrawler

def test_factory_pattern():
    diskcrawler = CrawlerFactory.create_crawler('disk', '.')
    assert isinstance(diskcrawler, DiskCrawler)
    try:
        fail = CrawlerFactory.create_crawler('null', '.')
    except Exception as e:
        assert isinstance(e, NotImplementedError)


def test_disk_crawler():
    diskcrawler = CrawlerFactory.create_crawler('disk', '.')
    assert isinstance(diskcrawler, DiskCrawler)
    assert diskcrawler.compute_digest(__file__) is not None