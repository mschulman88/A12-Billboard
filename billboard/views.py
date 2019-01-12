from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout, reverse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

# CONTEXT BELOW
def index(request):
    return render(request, 'billboard/index.html')


def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
        else:
    # Return an 'invalid credentials' error message.


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
        return HttpResponseRedirect(reverse("billboard"))
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", { "form": form })