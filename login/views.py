from django.shortcuts import render, redirect

def render_home(request):
	return render(request, 'home.html')

def render_signin(request):
	return render(request, 'signin.html')

def render_register(request):
	return render(request, 'register.html')