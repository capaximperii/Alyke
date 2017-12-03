"""
Each asset discovered and processed by Crawler is encapsulated as Resource.

"""

from functools import partial


class Resource(object):
    """    
    Represents each result object as a hash computed from the contents.

    """
    def __init__(self, path=None, compute_digest=None):
        """
        Constructor for a resource
        :param path: URL to the resource
        :param digest: Application specific digest for comparision and equality
        :param compute_digest: Application specific method for computing digest

        """
        self.path = path
        self.digest = None
        self.compute_digest_algo = partial(compute_digest, self.path)

    def __str__(self):
        """
        String representation of the object.
        :return: None

        """
        return self.path + ' --> ' + self.digest

    def get(self):
        """
        Represents resource as a tuple
        :return: Tuple

        """
        return (self.digest, self.path)


    def compute_digest(self):
        """
        Sets the digest of the Resource.
        :param: digest of the asset

        """
        self.digest = self.compute_digest_algo()
