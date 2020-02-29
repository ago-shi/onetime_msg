from django.urls import path
from . import views

app_name = 'onetime_msg'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]