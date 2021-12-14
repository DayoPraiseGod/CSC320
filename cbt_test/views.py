from django.shortcuts import render

def login_page(request):
	return render(request, 'cbt_test/login_page.html')
