from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name = 'home'),
    path('register/', register, name = 'register'),
    path('option/<str:username>/', optionPage, name = 'option'),
    path('update/<str:username>/', updateFunc, name = 'update'),
    path('profile/<str:username>/', deleteFunc, name = 'delete')
]