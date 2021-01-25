from django.urls import path
from accounts import views

urlpatterns = [
    path('accounts/', views.accounts, name="accounts"),
    # url(r'^accounts/change/password/$', changepassword, name='changepassword'),
    # url(r'^accounts/forgot/password/$', forgotpassword, name='forgotpassword'),
]
