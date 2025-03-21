from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('autre', views.other_page, name='other_page'),
]