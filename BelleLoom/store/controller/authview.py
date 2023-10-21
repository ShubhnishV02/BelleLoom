from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from store.forms import CustomUserForm

def register(request):
    form = CustomUserForm()
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Register Successfully! Login to Continue")
            return redirect("/login")
    data = {'form' : form}
    return render(request, "auth/register.html" , data)


def loginpage(request):
    if request.user.is_authenticated:
        messages.warning(request, "You are already logged in")
        return redirect("/")
    else:

        if request.method == "POST":
            name = request.POST.get("username")
            passwrd = request.POST.get("password")

            user = authenticate(request, username=name, password=passwrd)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully !")
                return redirect("/")
            else:
                messages.error(request, "Invalid Username or Password")
                return redirect("/login/")

        return render(request, "auth/login.html")
    

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, "Logged Out Successfully")
    return redirect("/")
