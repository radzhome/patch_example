import facebook
import simple_facebook
import mock
import unittest


# pip install facebook-sdk for py 2.7
class SimpleFacebookTestCase(unittest.TestCase):

    # Getting error, 'self' parameter lacking default value on assert_called
    # @mock.patch.object(facebook.GraphAPI, 'put_object', autospec=True,
    #                    return_value=mock.Mock(spec_set=facebook.GraphAPI),
    #                    post_message=mock.Mock())
    @staticmethod
    def test_post_message():
        mock_put_object = mock.create_autospec(simple_facebook.SimpleFacebook)
        sf = mock_put_object("fake oauth token")
        print mock_put_object.post_message("Hello World!")

        # verify
        mock_put_object.post_message.assert_called_once_with(message="Hello World!")


    # @staticmethod
    # def test_upload_complete():
    #     # build our dependencies, create_autospec creates a functionally equivalent instance to the provided class.
    #     mock_removal_service = mock.create_autospec(RemovalService)
    #     reference = UploadService(mock_removal_service)
    #
    #     # call upload_complete, which should, in turn, call `rm`:
    #     reference.upload_complete("my uploaded file")
    #
    #     # test that it called the rm method
    #     mock_removal_service.rm.assert_called_with("my uploaded file")