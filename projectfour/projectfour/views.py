from django.shortcuts import redirect, render

def login_redirect(request):
    return redirect('/home/login')
