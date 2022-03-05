
from django.http import JsonResponse
from django.shortcuts import render,redirect
import stripe
from e_app.models import ProductFree
from cart.models import ItemsFree,Cartlist

from cart.models import ItemsFree
from cart.views import *
import json
# from django.views import View
# from django.views.generic import TemplateView
from django.conf import settings
from . models import *



# Create your views here.
def home(request,ProductFree_id):
    productt = ProductFree.objects.get(id=ProductFree_id)
    qt= Cartlist.objects.get(cart_id=c_id(request))
    qty=ItemsFree.objects.get(cart_id=qt, active=True)
    return render(request,'home.html',{'product':productt,'qty':qty})


def checkout(request,ProductFree_id):
   
    stripe.api_key = 'sk_test_51KMS5bSJPvuJDXXz7QlSseBRc06bEXBpznxCtzdP0TvBcpbGa9QJMJZPKJcWi03cfAZOdicYjUU7PoNbr1aIFknP00ZkuvMhNa'
    YOUR_DOMAIN = 'http://127.0.0.1:8000/'
 
    # productt = ProductFree.objects.get(id=ProductFree_id)
    productt = get_object_or_404(ProductFree,id=ProductFree_id)
    print(productt)
    qt= Cartlist.objects.get(cart_id=c_id(request))
    qty=ItemsFree.objects.get(cart_id=qt, active=True)
    print(qty)
    # qty= get_object_or_404(ItemsFree,id=ProductFree_id)
    checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
                    'product':productt.name,
                    'quantity':qty.quantF,
                   
                },
              
            ],

          metadata={
                "ProductFree_id":productt.id
                },

            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel/',
        )
        

    return redirect(checkout_session.url, code=303)  


# def checkout(request,product_id):
#     stripe.api_key = 'sk_test_51KMS5bSJPvuJDXXz7QlSseBRc06bEXBpznxCtzdP0TvBcpbGa9QJMJZPKJcWi03cfAZOdicYjUU7PoNbr1aIFknP00ZkuvMhNa'
#     YOUR_DOMAIN = 'http://127.0.0.1:8000/'

#     cartlist = Cartlist.objects.get(id=product_id)
#     data = ProductFree.objects.get(id=product_id)
#     unit_amount = int(data.price/100)
#     line_items = []

    
#     quantity = 1
#     print(quantity)
#     name=data.name
#     print(name)


#     line_items.append({
#     'price_data': {
#         'currency': 'usd',
#         'unit_amount': unit_amount,
#         'product_data': {
#             'name': name,
#             # 'images': ['https://i.imgur.com/EHyR2nP.png'],
#         },
#     },
#     'quantity':quantity,
# })
    
#     try:

#         checkout_session = stripe.checkout.Session.create(
#             customer_email=ProductFree.email,
#             billing_address_collection='auto',
#             payment_method_types=['card'],
#             line_items=line_items,
#             metadata={
#                 # 'order_number': body['orderID'], 
#                 # 'payment_method': body['payment_method'], 
#                 'cart_id': cartlist,
#             },

#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#         )
#         return JsonResponse({'id': checkout_session.id})
#     except Exception as e:

#         return JsonResponse(error=str(e)), 403























































# class homeView(TemplateView):
#     template_name = "home.html"

#     def get_context_data(self,**kwargs):
#         # productt = ProductFree.objects.get(name='keyboard -mouse')
#         product = ProductFree.objects.all()
#         context = super(homeView,self).get_context_data(**kwargs)
#         context.update({
#             "product": product,
#             "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
#         })
#         return context

# class checkoutView(View):
#     def post(self, request, *args, **kwargs):
#         product_id = self.kwargs["ProductFree_id"]
#         product = ProductFree.objects.get(id=product_id)
#         stripe.api_key = 'sk_test_51KMS5bSJPvuJDXXz7QlSseBRc06bEXBpznxCtzdP0TvBcpbGa9QJMJZPKJcWi03cfAZOdicYjUU7PoNbr1aIFknP00ZkuvMhNa'
#         YOUR_DOMAIN = "http://127.0.0.1:8000"
#         checkout_session = stripe.checkout.Session.create(
#             payment_method_types=['card'],
#             line_items=[
#                 {
#                     'price_data': {
#                         'currency': 'usd',
#                         'unit_amount': product.price,
#                         'product_data': {
#                             'name': product.name,
#                             # 'images': ['https://i.imgur.com/EHyR2nP.png'],
#                         },
#                     },
#                     'quantity': 1,
#                 },
#             ],
#             metadata={
#                 "product_id": product.id
#             },
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#         )
#         return JsonResponse({
#             'id': checkout_session.id
#         })




































# def checkout(request,ProductFree_id):
#     stripe.api_key = 'sk_test_51KMS5bSJPvuJDXXz7QlSseBRc06bEXBpznxCtzdP0TvBcpbGa9QJMJZPKJcWi03cfAZOdicYjUU7PoNbr1aIFknP00ZkuvMhNa'
#     YOUR_DOMAIN = 'http://127.0.0.1:8000/'
#     orderr = Order.objects.get(id=ProductFree_id)
#     print(orderr)
#     cartlist = Cartlist.objects.get(cart_id=c_id(request))
#     items = ItemsFree.objects.filter(cart_id=cartlist, active=True)
#     print(items)
#     data = ItemsFree.objects.get(productF=orderr,cart=cartlist)
#     unit_amount = int(orderr.productF.price/100)
#     line_items = []
#     for items in data:
#         quantity = items.quantF
#         print(quantity)
#         name=items.productF.name
#         print(name)


#         line_items.append({
#         'price_data': {
#             'currency': 'usd',
#             'unit_amount': unit_amount,
#             'product_data': {
#                 'name': name,
#                 # 'images': ['https://i.imgur.com/EHyR2nP.png'],
#             },
#         },
#         'quantity':quantity,
#     })
    
#     try:

#         checkout_session = stripe.checkout.Session.create(
#             customer_email=orderr.email,
#             billing_address_collection='auto',
#             payment_method_types=['card'],
#             line_items=line_items,
#             metadata={
#                 # 'order_number': body['orderID'], 
#                 # 'payment_method': body['payment_method'], 
#                 'cart_id': cartlist,
#             },
#             mode='payment',
#             success_url=YOUR_DOMAIN + '/success/',
#             cancel_url=YOUR_DOMAIN + '/cancel/',
#         )
#         return JsonResponse({'id': checkout_session.id})
#     except Exception as e:
#         return JsonResponse(error=str(e)), 403
















        # checkout_session = stripe.checkout.Session.create(
        #     customer_email=order.email,
        #     billing_address_collection='auto',
        #     payment_method_types=['card'],

        #     line_items.append({
        #         'price_data': {
        #             'currency': 'usd',
        #             'unit_amount': unit_amount,

        #         'product_data': {
        #             'name': name,
        #             # 'images': ['https://i.imgur.com/EHyR2nP.png'],
        #             },

        #         },

        #         'quantity': quantity,

        #         }
        #         ),

    #         metadata={
    #             # 'order_number': body['orderID'], 
    #             # 'payment_method': body['payment_method'], 
    #             'cart_id': cartlist,
    #         },
    #         mode='payment',
    #         success_url=YOUR_DOMAIN + '/success/',
    #         cancel_url=YOUR_DOMAIN + '/cancel/',
    #     )

    #     return JsonResponse({'id': checkout_session.id})
    # except Exception as e:
    #     return JsonResponse(error=str(e)), 403

































    # checkout_session = stripe.checkout.Session.create(
    #         line_items=[
    #             {
    #                 # Provide the exact Price ID (for example, pr_1234) of the product you want to sell
    #                 'price': price,
    #                 'quantity': 1,
    #                 'name':name,
    #             },
              
    #         ],
    #         mode='payment',
    #         success_url=YOUR_DOMAIN + '/success.html',
    #         cancel_url=YOUR_DOMAIN + '/cancel.html',
    #     )

    # return redirect(checkout_session.url, code=303)   