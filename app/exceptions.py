

class BaseCustomException(Exception):

    status_code = None
    error_message = None
    detail = None

    def __init__(self, error_message):
        self.error_message = error_message
        super().__init__(self)

    @property
    def json_dict(self):
        return {'error': {
                    'status': self.status_code,
                    'type': self.__class__.__name__,
                    'message': self.error_message,
                    'detail': self.detail,
                    }
                }


class InvalidParameter(BaseCustomException):
    status_code = 400
    detail = f'Must provide valid query params <latitude> (+/- 90), <longitude> (+/- 180) and an optional <filters> (accuweather,noaa,weather.com)'


class ApiCallProviderError(BaseCustomException):
    status_code = 500
    detail = '-'
