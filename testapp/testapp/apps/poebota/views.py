from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Tovar
from .forms import SearcForm1
# Создаём логику приложения


"""def index(request):
    a = Book.objects.get(id=1)
    autor = a.book_autor
    janr = a.book_janr
    izdat = a.book_izdat
    data = {"autor": autor, "janr": janr, "izdat": izdat}
    return render(request, "index.html", context=data)"""

def index(request):
    tovar = SearcForm1.search(0)
    itog = SearcForm1.itog(0)
    print(tovar)
    return render(request, "home/search.html", {'tovar': tovar, 'itog': itog})

def create(request):
    """if request.method == "POST":
        autor = request.POST.get("autor")
        janr = request.POST.get("janr")
        izdat = request.POST.get("izdat")
        # searced = Book.objects.all().filter(book_autor=autor)
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0}</h2>".format(autor).format(janr).format(izdat))
        userform = SearcForm()
        #return render(request, "search.html", {"form": userform})
        print(autor, janr, izdat)"""

    return HttpResponseRedirect("/")


def indexzxc(request):
    return render(request, "home/home.html")

