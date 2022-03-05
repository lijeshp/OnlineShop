from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns =[
    path('<int:ProductFree_id>/',views.home,name='home'),
    path('checkout/<int:ProductFree_id>/',views.checkout,name='checkout'),
]