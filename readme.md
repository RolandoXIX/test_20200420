# test_20200420

*Emiliano Demagistris*  
*eademagistris@gmail.com*

### Setup
```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

### Routes
Host: http://127.0.0.1:8000/
##### Average Current Temperature
GET ?latitude=44&longitude=33&filters=noaa,weather.com,accuweather


## Testing

### Run tests:
```bash
python manage.py test
```

```bash
System check identified no issues (0 silenced).
.....................
----------------------------------------------------------------------
Ran 21 tests in 0.018s

OK
```

### Run tests with coverage:
```bash
pip install coverage
coverage run --source='.' manage.py test
```

### Check coverage report:
```bash
coverage report
```

```bash
Name                                   Stmts   Miss  Cover
----------------------------------------------------------
app/__init__.py                            0      0   100%
app/apps.py                                3      3     0%
app/exceptions.py                         15      0   100%
app/middlewares.py                        17      0   100%
app/migrations/__init__.py                 0      0   100%
app/services/__init__.py                   0      0   100%
app/services/app.py                       19      0   100%
app/services/providers.py                 38      0   100%
app/tests/__init__.py                      0      0   100%
app/tests/services/__init__.py             0      0   100%
app/tests/services/test_api.py            32      0   100%
app/tests/services/test_providers.py      40      0   100%
app/tests/test_exceptions.py              14      0   100%
app/tests/test_middlewares.py             32      0   100%
app/tests/test_views.py                   19      0   100%
app/urls.py                                3      0   100%
app/views.py                              14      0   100%
manage.py                                 12      2    83%
test_20200420/__init__.py                  0      0   100%
test_20200420/asgi.py                      4      4     0%
test_20200420/settings.py                 18      0   100%
test_20200420/urls.py                      3      0   100%
test_20200420/wsgi.py                      4      4     0%
----------------------------------------------------------
TOTAL                                    287     13    95%
```