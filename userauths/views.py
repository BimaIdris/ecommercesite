from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings

User=settings.AUTH_USER_MODEL

# Create your views here.
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            new_user=form.save()
            username=form.cleaned_data.get("username")
            messages.success(request, f"Hello {username}, Welcome")
            new_user=authenticate(username=form.cleaned_data["email"],
                                password=form.cleaned_data["password1"]
            )
            login(request, new_user)
            return redirect("coreurls:index")
    else:
        form = UserRegisterForm()
    context={
        'form': form,
    }
    return render(request, 'userauths/register.html',context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('coreurls:index') #if user logged in they are redirected
    
    if request.method == 'POST':
        email=request.POST.get('email')
        password=request.POST.get('password')

        try:
            user= User.objects.get(email=email, password=password)
        except:
            messages.warning(request, f"User with email: {email} does not exist")

        user = authenticate(request, email=email,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"You are logged in")
            return redirect('coreurls:index')
        else:
            messages.warning(request, f"User does not exist, create an account")
       
    return render(request, "userauths/sign-in.html")

def logout_view(request):
    logout(request)
    messages.success(request, f"You are now logged out")
    return redirect("userauths:sign-in")