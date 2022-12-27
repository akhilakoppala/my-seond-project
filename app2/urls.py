from django.urls import path
from app2.views import *
app_name='something'

urlpatterns=[
    path('ashok/',ashok,name='ashok'),
    path('aravind/',aravind,name='aravind'),
]