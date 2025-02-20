from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "out1":"Blendi"
    }
    return render(request,'index.html',context)