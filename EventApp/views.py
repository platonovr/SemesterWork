from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from EventApp.forms import LoginForm, PlaceForm, TypeForm
from EventApp.models import Event, Place, Type


class PlaceListView(ListView):
    model = Place
    template_name = "EventApp/places.html"
    context_object_name = "places"

    def get_queryset(self):
        qs = Place.objects.all()
        return qs

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(PlaceListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PlaceListView, self).get_context_data(**kwargs)
        return context


class TypeListView(ListView):
    model = Type
    template_name = "EventApp/types.html"
    context_object_name = "types"

    def get_queryset(self):
        qs = Type.objects.all()
        return qs

    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(TypeListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(TypeListView, self).get_context_data(**kwargs)
        return context


def no_auth_please(v):
    def wrapper(request, *a, **k):
        user = request.user
        if user.is_authenticated():
            return HttpResponseRedirect(reverse("menu"))
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
        place_id = request.POST.get('place', False)
        place = Place.objects.get(id=place_id)
        type_id = request.POST.get('type', False)
        eventtype = Type.objects.get(id=type_id)
        event = Event(time=time, description=description, payment=payment, place=place, type=eventtype)
        event.save()
        return HttpResponseRedirect(reverse('events'))
    elif request.method == "GET":
        places = Place.objects.all()
        types = Type.objects.all()
        return render(request, "EventApp/event_create.html", {"places": places, "types": types})


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
                if not request.POST.get('remember_me', None):
                    request.session.set_expiry(0)
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


@login_required(login_url=reverse_lazy("sign_in"))
def create_place(request):
    if request.method == "POST":
        form = PlaceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("places"))
    else:
        form = PlaceForm()
        return render(request, 'EventApp/create_place.html', {"form": form})


@login_required(login_url=reverse_lazy("sign_in"))
def create_type(request):
    if request.method == "POST":
        form = TypeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse("types"))
    else:
        form = TypeForm()
        return render(request, 'EventApp/create_type.html', {"form": form})


@login_required(login_url=reverse_lazy("sign_in"))
def go(request, event_id):
    if request.method == "POST":
        event = Event.objects.get(id=event_id)
        user = request.user
        event.user.add(user)
        event.save()
        return HttpResponseRedirect(reverse("events"))


@no_auth_please
def registration(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            new_user = form.save()
            return HttpResponseRedirect(reverse("sign_in"))
    else:
        form = UserCreationForm()
        return render_to_response('EventApp/registration.html', {'form': form},
                                  context_instance=RequestContext(request))


@login_required(login_url=reverse_lazy("sign_in"))
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse("menu"))
    else:
        form = PasswordChangeForm(user=request.user)
        return render_to_response('EventApp/change_password.html', {'form': form},
                                  context_instance=RequestContext(request))