from django.test import SimpleTestCase

from app.services.providers import BaseWeatherService, WeatherdotcomService, NoaaService, AccuweatherService
from app.exceptions import ApiCallProviderError

from unittest.mock import Mock, patch
import requests


class BaseWeatherServiceTests(SimpleTestCase):

	@patch('app.services.providers.requests.get')
	def test_make_resquest_ok(self, mock_get):

		mock_get.return_value.ok = True
		response = BaseWeatherService()._make_request('url')
		self.assertTrue(requests.get.called)
		self.assertIsNotNone(response)

	@patch('app.services.providers.requests.get')
	def test_make_resquest_error(self, mock_get):

		mock_get.return_value.ok = False
		with self.assertRaises(ApiCallProviderError):
			response = BaseWeatherService()._make_request('url')

	def test_fahrenheit_to_celsius(self):

		fahrenheit = 1
		celsius = BaseWeatherService().fahrenheit_to_celsius(fahrenheit)
		self.assertEqual(celsius, -17.22)


class WheaterdotcomServiceTests(SimpleTestCase):

	@patch('app.services.providers.WeatherdotcomService._make_request')
	def test_get_current_temperature(self, mock_make_request):

		response = {"query": {"results": {"channel": {"condition": {"temp": "1"}}}}}
		mock_make_request.return_value = response
		
		current_temperature = WeatherdotcomService().get_current_temperature('90', '90')

		self.assertTrue(WeatherdotcomService._make_request.called)
		self.assertEqual(current_temperature, (1.0, -17.22))


class NoaaServiceTests(SimpleTestCase):

	@patch('app.services.providers.NoaaService._make_request')
	def test_get_current_temperature(self, mock_make_request):

		response = {"today": {"current": {"fahrenheit": "1", "celsius": "-17.22"}}}
		mock_make_request.return_value = response
		
		current_temperature = NoaaService().get_current_temperature('90', '90')

		self.assertTrue(NoaaService._make_request.called)
		self.assertEqual(current_temperature, (1.0, -17.22))


class AccuweatherServiceTests(SimpleTestCase):

	@patch('app.services.providers.AccuweatherService._make_request')
	def test_get_current_temperature(self, mock_make_request):

		response = {"simpleforecast": {"forecastday": [{"current": {"fahrenheit": "1", "celsius": "-17.22"}}]}}
		mock_make_request.return_value = response
		
		current_temperature = AccuweatherService().get_current_temperature('90', '90')

		self.assertTrue(AccuweatherService._make_request.called)
		self.assertEqual(current_temperature, (1.0, -17.22))
