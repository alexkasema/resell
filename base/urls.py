from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name=''),
    path('contact/', views.contact, name='contact'),
]