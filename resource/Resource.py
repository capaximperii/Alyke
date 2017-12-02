"""
Each asset discovered and processed by Crawler is encapsulated as Resource.

"""

class Resource(object):
    """
    
    Represents each result object as a hash computed from the contents.
    """
    def __init__(self, path=None, digest=None):
        """
        Constructor for a resource
        :param path: URL to the resource
        :param digest: Application specific digest for comparision and equality
        """
        self.path = path
        self.digest = digest

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


    def set(self, digest):
        """
        Sets digest of a resource
        :param digest of the file
        :return: 
        """
        self.digest = digest
