from django.urls import path
from . import views

urlpatterns = [
path('',views.index),
path('delet/<int:id>',views.delet),
path('update/<int:id>',views.update)
]