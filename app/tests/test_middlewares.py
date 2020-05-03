from django.test import SimpleTestCase, override_settings

from app.middlewares import MiddlewareCustomException
from unittest.mock import Mock

import json


class MiddlewareCustomExceptionTests(SimpleTestCase):
    
    def setUp(self):
        self.request = Mock()
        self.exception = Mock()
        self.get_response = Mock()
        self.custom_middleware = MiddlewareCustomException(self.get_response)

    def test_init(self):
        middleware = MiddlewareCustomException('response')
        self.assertEqual(middleware.get_response, 'response')

    def test_call(self):
        middleware = self.custom_middleware(self.request)
        self.assertTrue(self.custom_middleware.get_response.called)
    
    def test_process_exception_from_custom_exception(self):
     
        self.exception.json_dict = {'message': 'error_message'}
        self.exception.status_code = 400
        
        response = MiddlewareCustomException(Mock()).process_exception(self.request, self.exception)
        self.assertEqual(response.status_code, 400)
        
        response_dict = json.loads(response.content)
        self.assertEqual(response_dict['message'], 'error_message')

    def test_process_exception_from_no_custom_exceptions_debug_false(self):

        response = MiddlewareCustomException(Mock()).process_exception(self.request, Exception)
        self.assertEqual(response.status_code, 500)
        
        response_dict = json.loads(response.content)
        self.assertEqual(response_dict['error']['message'], 'Unexpected error')
        self.assertEqual(response_dict['error']['status'], 500)

    @override_settings(DEBUG=True)
    def test_process_exception_from_no_custom_exceptions_debug_true(self):
        
        response = MiddlewareCustomException(Mock()).process_exception(self.request, Exception)
        self.assertEqual(response, None)