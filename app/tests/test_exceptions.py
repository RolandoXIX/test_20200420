from django.test import SimpleTestCase
from app.exceptions import BaseCustomException


class BaseCustomExceptionTests(SimpleTestCase):

    def setUp(self):
        self.custom_exception = BaseCustomException('error message')
        self.custom_exception.status_code = 400
        self.custom_exception.detail = 'error detail'

    def test_init(self):

        custom_exception = BaseCustomException('message')
        self.assertEqual(custom_exception.error_message, 'message')

    def test_json_dict(self):

        json_dict = self.custom_exception.json_dict
        
        expected_dict = {
            "error": {
                "status": 400,
                "type": "BaseCustomException",
                "message": "error message",
                "detail": "error detail"
            }
        }

        self.assertEqual(json_dict, expected_dict)

