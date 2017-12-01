"""

"""

import hashlib

class Resource(object):
    def __init__(self, path=None, digest=None):
        self.update(path, digest)

    def update(self, path, digest):
        self.path = path
        self.digest = digest

    def __str__(self):
        print(self.path, '-->', self.digest)

    def get(self):
        return (self.digest, self.path)

