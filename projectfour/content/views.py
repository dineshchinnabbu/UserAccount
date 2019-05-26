from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request,'content/homepage.html')

def shoppage(request):
    return render(request,'content/shop.html')
