from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect

from e_app.models import ProductFree
from . models import *


# Create your views here.
def c_id(request):
    ct_id = request.session.session_key
    
    if not ct_id:
        ct_id = request.session.create()
    return ct_id

def cart_details(request,tot=0,count=0,ct_items=None):
    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))
        ct_items = ItemsFree.objects.filter(cart_id=ct, active=True)
       
        for i in ct_items:
            tot+=(i.productF.price*i.quantF)
            count+=i.quantF
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', {'crt':ct_items,'tot':tot,'count':count})


def add_cart(request,ProductFree_id):
    prod = ProductFree.objects.get(id=ProductFree_id)
    try:
        ct = Cartlist.objects.get(cart_id=c_id(request))
    except Cartlist.DoesNotExist:
        ct = Cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=ItemsFree.objects.get(productF=prod,cart=ct)
        if c_items.quantF < c_items.productF.stock:
            c_items.quantF+=1
            c_items.save()
    except ItemsFree.DoesNotExist:
        c_items=ItemsFree.objects.create(productF=prod,quantF=1,cart=ct)
        c_items.save()
    return redirect('cart_details')

def minus_cart(request,ProductFree_id):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    prdt = get_object_or_404(ProductFree, id=ProductFree_id)
    c_items = ItemsFree.objects.get(productF=prdt,cart=ct)
    if c_items.quantF > 1:
        c_items.quantF-=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cart_details')

def delete_cart(request,ProductFree_id):
    ct = Cartlist.objects.get(cart_id=c_id(request))
    prdt = get_object_or_404(ProductFree, id=ProductFree_id)
    c_items =ItemsFree.objects.get(productF=prdt,cart=ct)
    c_items.delete()
    return redirect('cart_details')