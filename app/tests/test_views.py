from unittest.mock import patch

from django.test import SimpleTestCase, Client

from app.exceptions import InvalidParameter


class AverageViewTests(SimpleTestCase):

	def setUp(self):
		self.client = Client()

	@patch('app.services.app.AppService.get_current_temperature_average')
	def test_get(self, mock_get_current_temperature_average):

		mock_get_current_temperature_average.return_value = [1, 17.2] 

		params = {
			'latitude': '90',
			'longitude': '90',
			'filters': 'weather.com,noaa,accuweather'
		}
		
		response = self.client.get('', params)

		expected_response = {
  			"average current temperature": {
    			"fahrenheit": 1,
    			"celsius": 17.2
  				}
			}

		self.assertTrue(mock_get_current_temperature_average.called)
		self.assertEqual(response.status_code, 200)
		self.assertJSONEqual(response.content, expected_response)


	def test_get_with_missing_params(self):
		
			response = self.client.get('')  # no params

			expected_response = {
				"error": {
			    	"status": 400,
			    	"type": "InvalidParameter",
			    	"message": "latitud and longitud are required",
			    	"detail": "Must provide valid query params <latitude> (+/- 90), <longitude> (+/- 180) and an optional <filters> (accuweather,noaa,weather.com)"
			  	}
			}

			self.assertEqual(response.status_code, 400)
			self.assertJSONEqual(response.content, expected_response)
