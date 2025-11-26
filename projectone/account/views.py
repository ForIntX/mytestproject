from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login
# Create your views here.

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        # Authentication logic would go here
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)    
            return redirect("index")
        else:
            return render(request, 'account/login.html', {"error": "Invalid credentials"})
    
    return render(request, 'account/login.html')

def user_register(request):
    return render(request, 'account/register.html')

def user_logout(request):
    return redirect("index")