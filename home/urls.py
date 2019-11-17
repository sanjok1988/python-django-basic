
from django.urls import path
from .views import homeview,contactview
urlpatterns = [
    path('home/',homeview ),
    path('contact/',contactview )
]

