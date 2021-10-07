from django.shortcuts import render
from django.shortcuts import redirect
from .forms import ClientForm
from .forms import Client_roadForm
from .forms import Client_contactForm


def index(request):
    error = ""
    if request.method == "POST":
        cli = ClientForm(request.POST)
        if cli.is_valid():
            cli.save()
            return redirect("home")
        else:
            error = "Форма не верно заполнена!!!"

    if request.method == "POST":
        client = Client_roadForm(request.POST)
        if client.is_valid():
            client.save()
            return redirect("home")
        else:
            error = "Форма не верно заполнена!!!"

    cli = ClientForm
    client = Client_roadForm

    dat = {
        'cli': cli,
        'error': error,
        'client': client
    }

    return render(request, "main/index.html", dat)


def about(request):
    return render(request, "main/about.html")


def contact(request):
    error = ""
    if request.method == "POST":
        cont = Client_contactForm(request.POST)
        if cont.is_valid():
            cont.save()
            return redirect("home")
        else:
            error = "Форма не верно заполнена!!!"

    cont = Client_contactForm
    date = {
        'cont': cont,
        'error': error
    }
    return render(request, "main/contact.html", date)


def services(request):
    return render(request, "main/services.html")
