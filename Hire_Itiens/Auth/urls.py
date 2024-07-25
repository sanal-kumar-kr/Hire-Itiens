from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('Register',views.Register_page),
    path('userareg/<int:ut>',views.userareg),
    path('register',views.Register_page),

    path('login',views.login),
    path('Logout',views.Logout),

   
]
handler404 = 'Auth.views.custom_404'
