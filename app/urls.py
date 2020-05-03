from django.urls import path
from .views import AverageView


urlpatterns = [
    path('', AverageView.as_view(), name='average')
]