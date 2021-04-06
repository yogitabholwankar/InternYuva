from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# from django.views.decorators.csrf import csrf_exempt
# from .models import Orders, UpdateOrder
from Paytm import Checksum
from classroom.models import Ratings
import random





def home(request):
    template_name = 'index.html'
    return render(request, template_name)


def dashboard(request):
    template_name = 'accounts/base.html'
    return render(request, template_name)


def profile(request):
    template_name = 'dashboard/profile_setting.html'
    return render(request, template_name)


def course_purchage(request):
    rating = Ratings.objects.all().count() 
    return render(request, 'course/course_purchage.html', {'rating':rating})


# def checkout(request):
#     if request.method == 'POST':
#         course = request.POST.get('course')
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         mobile = request.POST.get('mobile')
#         amount = request.POST.get('amount')

#         order = Transaction(item_json=course, name=name, email=email,  mobile=mobile, amount=amount)
#         order.save()

#         orderid=random.randrange(11111,99999)
#         # update = UpdateOrder(order_id=order.order_id, update_desc="Order placed")
#         # update.save()
#         # thank = True
#         # ids = order.order_id
#         # return render(request, 'dashboard/checkout.html', {'thank':thank, 'ids':ids})
#         param_dict = {
#             'MID': 'XouRsh60629205732669',
#             'ORDER_ID': str(orderid),
#             'TXN_AMOUNT': str(amount),
#             'CUST_ID': email,
#             'INDUSTRY_TYPE_ID': 'Retail',
#             'WEBSITE': 'WEBSTAGING',
#             'CHANNEL_ID': 'WEB',
#             'CALLBACK_URL': 'http://127.0.0.1:8000/dashboard/handlerequest/',
#         }
#         print(param_dict)
#         param_dict['CHECKSUMHASH'] = Checksum.generate_checksum(param_dict, MERCHANT_KEY)
#         return render(request, 'dashboard/paytm.html', {'param_dict': param_dict})

#     return render(request, 'dashboard/checkout.html')


# @csrf_exempt
# def handlerequest(request):
#     print("hello")
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]
#     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             print('order Successfull')
#         else:
#             print('Something went wrong' + response_dict['RESPMSG'])
#     return render(request, 'dashboard/paytm_payment_status.html', {'response_dict':response_dict})
