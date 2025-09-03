from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Collection, Piece
from django.views import generic
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.views.generic import View

class index(generic.ListView):
    template_name = 'genre/genretemplate.html'

    def get_queryset(self):
        return Collection.objects.all()
        
        

# def index(request):
#     all_collections = Collection.objects.all()
#     context={
#         "all_collections":all_collections
#     }
#     return render(request, "genre/genretemplate.html",context)


class details(generic.DetailView):
    model = Collection
    template_name = 'genre/detailtemplate.html'



# def details(request,genre_id):
#     collection_item = Collection.objects.get(pk=genre_id)
#     piece_item = Piece.objects.filter(collection=collection_item)
#     context = {
#         "Pitem" : piece_item
#     }
#     return render(request, "genre/detailtemplate.html",context)


class UserFormView(View):
    form_class = UserForm
    template_name = 'genre/formtemplate.html'

    def get(self, request):
        form= self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            user = form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            newuser = authenticate(username=username, password=password)

            if newuser is not None:

                if newuser.is_active:
                    login(request, newuser)
                    return redirect('/genre')
        return render(request, self.template_name, {'form': form})