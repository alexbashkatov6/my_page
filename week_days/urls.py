from django.urls import path
from . import views

urlpatterns = [
    path('<int:week_day>/', views.get_info_int),
    path('<str:week_day>/', views.get_info, name="week-day-name"),
]
