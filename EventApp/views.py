from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from EventApp.forms import LoginForm
from EventApp.models import Event, Place


def no_auth_please(v):
    def wrapper(request, *a, **k):
        user = request.user
        if user.is_authenticated():
            return HttpResponseRedirect(reverse("index"))
        else:
            return v(request, *a, **k)

    return wrapper


@login_required(login_url=reverse_lazy("sign_in"))
def menu(request):
    return render(request, "EventApp/menu.html", {"user": request.user.username})


@login_required(login_url=reverse_lazy("sign_in"))
def events(request):
    current_events = Event.objects.all()
    return render(request, "EventApp/events.html", {"events": current_events})


@login_required(login_url=reverse_lazy("sign_in"))
def create_event(request):
    if request.method == "POST":
        time = request.POST["time"]
        description = request.POST["description"]
        payment = request.POST["payment"]
        place = Place(coordinates="123", description="123")
        event = Event(time=time, description=description, payment=payment, place=place)
        event.save()
        return HttpResponseRedirect(reverse('events'))
    elif request.method == "GET":
        return render(request, "EventApp/event_create.html")


@login_required(login_url=reverse_lazy("sign_in"))
def settings(request):
    if request.method == "GET":
        return render(request, "EventApp/settings.html")


@no_auth_please
def sign_in(request):
    if request.POST:
        f = LoginForm(request.POST)
        if f.is_valid():
            user = authenticate(username=f.cleaned_data["username"], password=f.cleaned_data["password"])
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('menu'))
            else:
                return HttpResponseRedirect(reverse('sign_in'))
    else:
        f = LoginForm()
        context = {"f": f}
        return render(request, "EventApp/login.html", context)


@login_required
def exit(request):
    logout(request)
    return HttpResponseRedirect(reverse("sign_in"))