#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import rm

import mock
import unittest
# See https://www.toptal.com/python/an-introduction-to-mocking-in-python
# sudo pip install mock  (for py 2.7)


# Mock an item where it is used, not where it came from.
class RmTestCase(unittest.TestCase):
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os):
        rm("any path")
        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with("any path")