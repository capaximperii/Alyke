"""

Implements a simple Config parser.

TODO: Add methods to merge command line arguments along with config file.
"""
class Config(object):
    """ Represents a user configuration instance. """
    def __init__(self, d):
        """
        Constructor converts config file dictionary into class members.
        :param d: User settings dictionary
        """
        for a, b in d.items():
            if isinstance(b, (list, tuple)):
                setattr(self, a, [Config(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, Config(b) if isinstance(b, dict) else b)
