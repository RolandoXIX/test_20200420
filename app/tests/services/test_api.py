from unittest.mock import patch, MagicMock

from django.test import SimpleTestCase

from app.services.app import AppService
from app.services.providers import WEATHER_SERVICES
from app.exceptions import InvalidParameter


class ApiServiceTests(SimpleTestCase):

    @patch('app.services.app.AppService.are_valid_parameters')
    def test_get_current_temperature_average(self, mock_are_valid_paramenters):

        mock_are_valid_paramenters.return_value = True
        mock = MagicMock()
        mock.get_current_temperature.return_value = (1, -17.22)

        dic = dict()
        for key in WEATHER_SERVICES.keys():
            dic[key] = mock

        with patch.dict('app.services.providers.WEATHER_SERVICES', dic):
            average = AppService().get_current_temperature_average('90', '90')
            self.assertTrue(AppService.are_valid_parameters.called)
            self.assertEqual(average, [1, -17.2])

    def test_are_valid_parameters_true_whit_filters(self):

        result = AppService().are_valid_parameters('90', '90', 'weather.com,noaa,accuweather')
        self.assertTrue(result)

    def test_are_valid_parameters_true_whitout_filters(self):

        result = AppService().are_valid_parameters('90', '90', None)
        self.assertTrue(result)

    def test_are_valid_parameters_with_invalid_latitude(self):

        with self.assertRaises(InvalidParameter):
            AppService().are_valid_parameters('91', '90', None)  # invalid latirude

    def test_are_valid_parameters_with_invalid_logitude(self):

        with self.assertRaises(InvalidParameter):
            AppService().are_valid_parameters('90', '181', None)  # invalid longitude

    def test_are_valid_parameters_with_invalid_filter(self):

        with self.assertRaises(InvalidParameter):
            AppService().are_valid_parameters('90', '90', 'invalid_filter')  # invalid filter