"""

Implements a simple Config parser.

TODO: Add methods to merge command line arguments along with config file.
"""
class Config(object):
    """ Represents a user configuration instance. """
    def __init__(self, cfg):
        """
        Constructor converts config file dictionary into class members.
        :param cfg: User settings dictionary
        """
        self.update(cfg)

    def update(self, cfg):
        """
        Allows config update after constructor has been called, for example to override via commandline

        :param cfg: command line dictionary
        :return: None
        """
        for a, b in cfg.items():
            a = a.replace('--', '')
            if isinstance(b, (list, tuple)):
                setattr(self, a, [Config(x) if isinstance(x, dict) else x for x in b])
            else:
                setattr(self, a, Config(b) if isinstance(b, dict) else b)