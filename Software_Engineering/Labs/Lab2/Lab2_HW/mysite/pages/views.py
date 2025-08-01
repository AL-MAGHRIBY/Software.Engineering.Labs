from django.shortcuts import render

# Create your views here.
# from django.http import HttpResponse   حينما كانت رسالة ترحيبية

# def index(request):
#     return HttpResponse('<h1>Hello from Pages App</h1>')

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
