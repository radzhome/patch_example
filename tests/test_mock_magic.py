import mock
import unittest


class Target(object):

    @staticmethod
    def apply(value, are_you_sure):
        if are_you_sure:
            return value
        else:
            return None


def method(target, value, are_you_sure):
    return target.apply(value, are_you_sure)


class MethodTestCase(unittest.TestCase):

    @staticmethod
    def test_method():

        # Still passes this way since target is a mock, calling target.apply will work with 1 param
        # target = mock.Mock()

        # So now lets use, and with a single param should fail
        target = mock.create_autospec(Target)

        # So use both and it passes
        # method(target, "value")
        method(target, value="value", are_you_sure=True)

        # target.apply.assert_called_with("value")
        target.apply.assert_called_with("value", True)
