"""
Provide an interface for creating families of related or dependent
objects without specifying their concrete classes.
"""

import abc

class CrawlerBlueprint(metaclass=abc.ABCMeta):
    """
    Implement the operations to create concrete product objects.
    """
    def __init__(self, base):
        self.base = base

    @abc.abstractmethod
    def __iter__(self):
        """
        
        :return: 
        """

    @abc.abstractstaticmethod
    def partial_reader(filename, chunk_size):
        """
        Abstract method for reading a file in chunks
        """

    @abc.abstractstaticmethod
    def compute_digest(filename):
        """
        Abstract method for hashing a file
        """