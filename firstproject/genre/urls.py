from django.urls import path
from . import views

urlpatterns = [
    #/genre/
    path('',views.index.as_view(),name='index'),

    #/genre/1/
    path('<int:pk>/',views.details.as_view(),name='details'),

    # register/
    path('register/', views.UserFormView.as_view(), name='userform'),
    

]
