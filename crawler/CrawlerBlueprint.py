"""

Provide an interface for creating families of related crawlers
for Crawler implementations to ihnerit from.
"""

import abc

class CrawlerBlueprint(metaclass=abc.ABCMeta):
    """
    Crawler implementation classes common constructor.
    """
    def __init__(self, base):
        self.base = base

    @abc.abstractmethod
    def __iter__(self):
        """
        Iterator design pattern to abstract away how concrete crawlers crawl and fetch data.
        :return: Standard Iterator 
        """

    @abc.abstractstaticmethod
    def partial_reader(filename, chunk_size):
        """
        Abstract method for reading a file in chunks
        :return: chunk_size bytes read from the resource.
        """

    @abc.abstractstaticmethod
    def compute_digest(filename):
        """
        Abstract method for hashing a file this can be content dependent.
        For example: Whether 2 images are equal is a different implementation of equality than pure binary implementation.

        """