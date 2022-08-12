from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "blogapp/index.html")

def cancer1(request):
    return render(request, "blogapp/cancer1.html")
