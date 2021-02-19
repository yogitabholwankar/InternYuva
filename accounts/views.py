from django.conf import settings
from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login, authenticate, logout
from accounts.forms import RegistrationForm, AccountAuthenticationForm,NumberForm
from django.contrib.auth.decorators import login_required
from .otp_service import *
# from .models import Account


Account=settings.AUTH_USER_MODEL
# Django Admin
# Email: desh2@gmail.com 
# Username: desh1
# Password: 12345

def accounts(request):
	pass

def index(request):
    return render(request,'accounts/home.html')


def generate_opt():
    n=random.randrange(1000,9999)
    return n

# otp=1234



def registration_view(request):
    context = {}
    if request.POST:

        form = RegistrationForm(request.POST)
        if form.is_valid():

            customer_number = form.cleaned_data.get('mobile')
            print(customer_number)
            user_otp = form.cleaned_data.get('otp')
            print(user_otp)
            send_otp(account_sid , auth_token , customer_number)
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('otp_verification')
        else:
            context['registration_form'] = form

    else: #GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'accounts/register.html', context)

@login_required
def verification(request):
    # current_user=Account
    current_user=request.user
    if current_user.is_verify:
        messages.warning(request,'Your Number is already verified...!')
        return redirect('dashboard')

    # current_otp = generate_opt()
    current_otp = 1234
    send_otp(current_user.phone_number, current_otp)

    otp_input=NumberForm()
    if request.method=="POST":
        otp_input=NumberForm(request.POST or None)
        if otp_input.is_valid():
            number=otp_input.cleaned_data['number']
            if number == current_otp:
                current_user.is_verify=True
                current_user.save()
                messages.warning(request, 'You Have Successfully Verify Your Number .!')
                print("'You Have Successfully Verify Your Number .!", current_otp)
                return redirect('dashboard')
            else:
                messages.warning(request, 'Your Input OTP is invalid')
                print("INVALID OTP",current_otp)
                return redirect('otp_verification')
    context={
        'form':otp_input,
        'object':current_user
    }
    return render(request,'accounts/otp_verification.html',context)

@login_required
def logout_view(request):
    logout(request)
    return redirect('homepage')



def login_view(request):
    context={}

    user=request.user
    if user.is_authenticated:
        return redirect('dashboard')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("dashboard")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    # print(form)
    return render(request, "accounts/login.html", context)
