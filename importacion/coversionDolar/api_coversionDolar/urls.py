from django.urls import path
from .views import conversionDolares

urlpatterns= [
    path('conversionDeMoneda',conversionDolares.as_view()),
]