from django.http import JsonResponse
from django.views.generic import View

from .services.app import AppService
from .exceptions import InvalidParameter


class AverageView(View):

    def get(self, request):

        """ Return the average current temperature for a given lat/lon. """

        try:
            latitude, longitude = request.GET['latitude'], request.GET['longitude']
        except KeyError:
            raise InvalidParameter(f'latitud and longitud are required')

        filters = request.GET.get('filters')

        current_temperature = AppService().get_current_temperature_average(latitude, longitude, filters)

        data = {'average current temperature': {
                    'fahrenheit': current_temperature[0],
                    'celsius': current_temperature[1]
                    }
                }

        return JsonResponse(data, json_dumps_params={'indent': 2})
