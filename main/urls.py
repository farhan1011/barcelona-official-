
from django.urls import path
from . import views

urlpatterns = [
    path('',views.mainpage,name='mainpage'),
    path('squad/',views.squad,name='squad'),
    path('legends/',views.legend,name='legends'),
    path('womens/',views.women, name='women')

]
