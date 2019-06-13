from django.shortcuts import render,HttpResponse
from django.urls import reverse
from django.shortcuts import redirect
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        print(request.POST.get('username'))
        print(request.POST.get('password'))
        url = reverse('index')
        return redirect(url)
    return render(request, 'login.html')
