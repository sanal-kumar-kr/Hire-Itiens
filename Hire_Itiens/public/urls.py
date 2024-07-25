from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('about',views.about),
    path('contact',views.contact),
    path('service',views.services),

]
handler404 = 'public.views.custom_404'
