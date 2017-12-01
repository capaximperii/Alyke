from alyke import Config


class TestConfig(object):
    def test_config(self):
        config = Config({'a': 1, 'b': 2, 'c': 'stringtest', 'd': [1, 2]})
        assert config.a == 1
        assert config.b == 2
        assert config.c == 'stringtest'
        assert isinstance(config.d, list)

