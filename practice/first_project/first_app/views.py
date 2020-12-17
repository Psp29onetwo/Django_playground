from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# def index(request):
#     return HttpResponse("<h1>Hello Django!</h1>")
def index(request):
    context = {'insert_me': 'Hello i m PSP'}
    return render(request, 'first_app/index.html', context=context)
