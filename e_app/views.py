from re import template
from unicodedata import category
from django.shortcuts import get_object_or_404, render

from e_app.models import ProductFree, categ
from django.core.paginator import EmptyPage,InvalidPage,Paginator
from django.conf import settings
from django.http import HttpResponse, Http404
import os


# Create your views here.
def index(request,c_slug=None):
    c_page = None
    prdtF = None
    prdtP = None
    if c_slug != None:
        c_page =get_object_or_404(categ,slug=c_slug)
        prdtF = ProductFree.objects.filter(category=c_page,available=True)
        # prdtP = ProductPaid.objects.filter(category=c_page,available=True)
    else:
        prdtF = ProductFree.objects.all().filter(available = True)
        # prdtP = ProductPaid.objects.all().filter(available=True)
    cat = categ.objects.all()
    paginator = Paginator(prdtF,5)

    try:
        page = int(request.GET.get('page',1))
    except:
        page=1
    try:
        pro=paginator.page(page)
    except:
        pro = paginator.page(paginator.num_pages)

    return render(request,'index.html',{'obj':prdtF,'obj1':prdtP,'cat':cat,'pro':pro})

def product_details(request,c_slug,productF_slug):
    try:
        prductF = ProductFree.objects.get(category__slug=c_slug,slug=productF_slug)
        # prductP = ProductPaid.objects.get(category__slug=cc_slug,slug=productP_slug)
    except Exception as e:
        raise e
    return render(request,'product-details.html',{'prductF':prductF})
    


def download(path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb') as fh:
            response=HttpResponse(fh.read(),content_type="application/ProductFree")
            response=HttpResponse(fh.read(),content_type="application/ProductPaid")
            response['Content-Disposition']='inline;filename='+os.path.basename(file_path)
            return response
    raise Http404  


















# def product_detailss(request,cc_slug,productP_slug):
    
#     try:
#         prductP = ProductPaid.objects.get(category__slug=cc_slug,slug=productP_slug)
#     except Exception as e:
#         raise e
#     return render(request,'product-detailss.html',{'prductP':prductP})
