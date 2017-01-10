import mock
import unittest


class Target(object):
    @staticmethod
    def apply(value):
        return value


def method(target, value):
    return target.apply(value)


class MethodTestCase(unittest.TestCase):

    @staticmethod
    def test_method():
        target = mock.Mock()

        method(target, "value")

        target.apply.assert_called_with("value")
