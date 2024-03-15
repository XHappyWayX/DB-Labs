from django.urls import path
from .views import GetData

urlpatterns = [
    path('getdata/', GetData().as_view(), name='getdata'),
]