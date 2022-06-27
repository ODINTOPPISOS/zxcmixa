from django import forms
from .models import Tovar

class SearcForm(forms.Form):
    autor = forms.CharField()
    janr = forms.CharField()
    izdat = forms.CharField()

class SearcForm1(forms.Form):
    def search(self):
        tovar = Tovar.objects.all()
        return tovar
    def itog(self):
        itogo = 0
        tovar = Tovar.objects.all()
        for i in tovar:
            itogo += int(i.tovar_price)
        return itogo

"""list_book = {'autor': (), 'janr': (), 'izdat': (), 'name': ()}
        for i in books:
            if autor == i.book_autor or janr == i.book_janr or izdat == i.book_izdat:
                autors.append(i.book_autor)
                janrs.append(i.book_janr)
                izdats.append(i.book_izdat)
                name.append(i.book_name)
                list_book['autor'] = autors
                list_book['janr'] = janrs
                list_book['izdat'] = izdats
                list_book['name'] = name
                print(list_book['name'])"""