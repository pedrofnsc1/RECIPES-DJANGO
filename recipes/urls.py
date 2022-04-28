from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view),
    path('sobre/', views.sobre),
    path('contato/', views.contato)
]
