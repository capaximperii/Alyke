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
        pass
