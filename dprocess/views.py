from django.shortcuts import render

# Create your views here.


def home(request):
	template_name = 'index.html'
	return render(request, template_name)


def dashboard(request):
	template_name = 'accounts/base.html'
	return render(request, template_name)


def profile(request):
	template_name = 'dashboard/profile_setting.html'
	return render(request, template_name)