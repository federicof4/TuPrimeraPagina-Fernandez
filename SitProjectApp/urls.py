from django.urls import path
from .views import index

app_name = 'SitProjectApp'

urlpatterns = [
    path('', index,name='index'),   
]