from django.shortcuts import render

# Create your views here.

def exception_page(request):
	c={}
	return render(request,"exception/exception_page.html",c)