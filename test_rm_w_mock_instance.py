#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mymodule import RemovalService, UploadService

import mock
import unittest


class RemovalServiceTestCase(unittest.TestCase):
    @mock.patch('mymodule.os.path')
    @mock.patch('mymodule.os')
    def test_rm(self, mock_os, mock_path):
        # instantiate our service
        reference = RemovalService()

        # set up the mock
        mock_path.isfile.return_value = False

        reference.rm("any path")

        # test that the remove call was NOT called.
        self.assertFalse(mock_os.remove.called, "Failed to not remove the file if not present.")

        # make the file 'exist'
        mock_path.isfile.return_value = True

        reference.rm("any path")

        mock_os.remove.assert_called_with("any path")


# Simply create an auto-spec for the RemovalService class
class UploadServiceTestCase(unittest.TestCase):

    @staticmethod
    def test_upload_complete():
        # build our dependencies, create_autospec creates a functionally equivalent instance to the provided class.
        mock_removal_service = mock.create_autospec(RemovalService)
        reference = UploadService(mock_removal_service)

        # call upload_complete, which should, in turn, call `rm`:
        reference.upload_complete("my uploaded file")

        # test that it called the rm method
        mock_removal_service.rm.assert_called_with("my uploaded file")