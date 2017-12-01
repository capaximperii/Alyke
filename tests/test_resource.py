from resource import Resource


class TestResource(object):
    def setup(self):
        self.resource = Resource('/tmp/a', 'digest')

    def teardown(self):
        print ("Resource teardown")

    def test_get(self):
        result = self.resource.get()
        assert result[1] == '/tmp/a'
        assert result[0] == 'digest'

    def test_to_string(self):
        result = str(self.resource)
        assert result == '/tmp/a --> digest'