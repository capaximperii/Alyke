from crawler.CrawlerBlueprint import CrawlerBlueprint
from pathlib import Path

class FsCrawler(CrawlerBlueprint):
    def __init__(self, base):
        super(FsCrawler, self).__init__( base);
        self.path = Path(base)

    def __iter__(self):
        for f in self.path.glob('**/*'):
            if f.is_file():
                yield f

    def partial_reader(filename, chunk_size):
        """Generator that reads a file in chunks of bytes"""

        while True:
            chunk = fobj.read(chunk_size)
            if not chunk:
                return
            yield chunk
