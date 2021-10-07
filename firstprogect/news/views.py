from django.shortcuts import render, redirect
from .models import Onemodel
from .forms import AddCallFormForm


def news_home(request):
    news = Onemodel.objects.order_by('-date')
    return render(request, "news/news_blog.html", {"news_bl": news})


def addcall(request):
    error = ""
    if request.method == "POST":
        form = AddCallFormForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            error = "Форма была не верной"

    form = AddCallFormForm

    date = {
        'form': form,
        'error': error

    }
    return render(request, "news/addcall.html", date)
