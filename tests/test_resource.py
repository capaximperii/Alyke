from resource import Resource

def dummy_compute_digest(path):
    return "digest"

class TestResource(object):
    def setup(self):
        self.resource = Resource('/tmp/a', dummy_compute_digest)

    def teardown(self):
        print ("Resource teardown")

    def test_get(self):
        self.resource.compute_digest()
        result = self.resource.get()
        assert result[1] == '/tmp/a'
        assert result[0] == 'digest'

    def test_to_string(self):
        self.resource.compute_digest()
        result = str(self.resource)
        assert result == '/tmp/a --> digest'