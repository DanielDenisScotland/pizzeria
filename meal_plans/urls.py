from django.urls import path
from . import views

app_name = 'meal_plans'
urlpatterns = [
    # hp
    path('', views.index, name='index'),
]