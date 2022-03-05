from django.urls import path,include,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django . views.static import serve

urlpatterns = [

    path('', views.index, name='index'),
    re_path(r"^download/(?P<path>.*)$",serve,{"document_root":settings.MEDIA_ROOT}),
    path('<slug:c_slug>/',views.index,name='prdt_by_cat'),
    path('<slug:c_slug>/<slug:productF_slug>/',views.product_details, name='details',),
   
  
]