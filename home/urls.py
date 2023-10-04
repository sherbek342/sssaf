from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login,  name='login'),
    path('', views.home, name='home' ),
    path('registr', views.reg, name='registr' ),
    path('login/add', views.add, name="add")
]