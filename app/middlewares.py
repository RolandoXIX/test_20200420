from django.http import JsonResponse
from django.conf import settings


class MiddlewareCustomException:

    """ Custom middleware for catching exceptions and
        return a JsonResponse """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):

        # If exception is not custom, return JsonResponse if DEBUG=False

        try:
            status = exception.status_code
            exception_dict = exception.json_dict
        except AttributeError:
            if settings.DEBUG:
                return
            else:
                status = 500
                exception_dict = {
                    'error': {
                        'status': 500,
                        'message': 'Unexpected error',
                        },
                }

        return JsonResponse(exception_dict, status=status, json_dumps_params={'indent': 2})