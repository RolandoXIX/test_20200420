from statistics import mean

from .providers import WEATHER_SERVICES
from app.exceptions import InvalidParameter


class AppService():

    def get_current_temperature_average(self, latitude, longitude, filters=None):

        if self.are_valid_parameters(latitude, longitude, filters):

            # if not filters, takes all services for calculations.
            services_to_fletch = WEATHER_SERVICES.keys() if not filters else filters.lower().split(',')

            temperatures = []
            for service in services_to_fletch:
                current_temp = getattr(WEATHER_SERVICES[service], 'get_current_temperature')(latitude, longitude)
                temperatures.append(current_temp)

            return [round(mean(x), 1) for x in zip(*temperatures)]

    def are_valid_parameters(self, latitude, longitude, filters):

        is_valid_lat = -90 <= int(latitude) <= 90
        is_valid_lon = -180 <= int(longitude) <= 180
        is_valid_filters = all(i in WEATHER_SERVICES.keys() for i in str(filters).lower().split(',')) or not filters

        if is_valid_lat and is_valid_lon and is_valid_filters:
            return True
        else:
            raise InvalidParameter('Incorrect latitude, longitude or filter')