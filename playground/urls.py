from django.urls import path
from . import views

# URLConfiguration module -> URLConf
urlpatterns = [
    path('hello/', views.say_hello)
]