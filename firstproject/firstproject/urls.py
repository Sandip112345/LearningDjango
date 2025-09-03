
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('genre/',include('genre.urls')),
    path('polls/',include('polls.urls')),
    path('admin/', admin.site.urls),
]
