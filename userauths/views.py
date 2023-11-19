from django.shortcuts import redirect, render
from userauths.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

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
