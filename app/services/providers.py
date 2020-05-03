import requests

from app.exceptions import ApiCallProviderError


class BaseWeatherService():

    """
    Base class for all weather providers.
    """

    def _make_request(self, url, method='GET', params=None, data=None, headers=None):

        # base method for fetching data from different endpoints.

        response = getattr(requests, method.lower())(url, params=params, json=data, headers=headers)
        if not response.ok:
            raise ApiCallProviderError('Unexpected error')

        return response.json()

    def fahrenheit_to_celsius(self, fahrenheit):

        return round((float(fahrenheit) - 32) * 5/9, 2)


class WeatherdotcomService(BaseWeatherService):

    PROVIDER = 'weather.com'
    ENDPOINT = 'http://127.0.0.1:5000/weatherdotcom'

    def get_current_temperature(self, latitude, longitude):

        data = {'lat': float(latitude),
                'lon': float(longitude)}

        response = self._make_request(self.ENDPOINT, method='POST', data=data)

        fahrenheit = response['query']['results']['channel']['condition']['temp']
        celsius = self.fahrenheit_to_celsius(fahrenheit)

        return float(fahrenheit), float(celsius)


class NoaaService(BaseWeatherService):

    PROVIDER = 'noaa'
    ENDPOINT = 'http://127.0.0.1:5000/noaa'

    def get_current_temperature(self, latitude, longitude):

        params = {'latlon': ','.join([str(latitude), str(longitude)])}

        response = self._make_request(self.ENDPOINT, params=params)

        fahrenheit = response['today']['current']['fahrenheit']
        celsius = response['today']['current']['celsius']

        return float(fahrenheit), float(celsius)


class AccuweatherService(BaseWeatherService):

    PROVIDER = 'accuweather'
    ENDPOINT = 'http://127.0.0.1:5000/accuweather'

    def get_current_temperature(self, latitude, longitude):

        params = {'latitude': latitude,
                  'longitude': longitude}

        response = self._make_request(self.ENDPOINT, params=params)

        fahrenheit = response['simpleforecast']['forecastday'][0]['current']['fahrenheit']
        celsius = response['simpleforecast']['forecastday'][0]['current']['celsius']

        return float(fahrenheit), float(celsius)


WEATHER_SERVICES= {
    WeatherdotcomService.PROVIDER: WeatherdotcomService(),
    NoaaService.PROVIDER: NoaaService(),
    AccuweatherService.PROVIDER: AccuweatherService(),
}
