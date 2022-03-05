from django.urls import path,include
from . import views

urlpatterns = [

    path('cart_details', views.cart_details, name='cart_details'),
    path('add/<int:ProductFree_id>/', views.add_cart, name='addcart'),
    path('minus/<int:ProductFree_id>/',views.minus_cart, name='minuscart'),
    path('delete/<int:ProductFree_id>/',views.delete_cart, name='deletecart'),
]

  