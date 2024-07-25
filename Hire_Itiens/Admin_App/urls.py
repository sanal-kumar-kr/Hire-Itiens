from django.urls import path
from . import views

urlpatterns = [
    path('usersreq/<int:ut>/', views.view_users, name='view_users'),
    path('users/<int:ut>/', views.view_app_users, name='view_app_users'),
    path('approve/<int:id>/', views.approve, name='approve'),
    path('reject/<int:id>/', views.reject, name='reject'),
    path('collegeedit/<int:id>/', views.Editcollege, name='Editcollege'),
    path('companyedit/<int:id>/', views.Editcompany, name='Editcompany'),
    path('jobseakeredit/<int:id>/', views.EditJobSeakers, name='EditJobSeakers'),
    path('Deleteuser/<int:id>/', views.Deleteuser, name='Deleteuser'),
    path('userreq_int/', views.usersreq_int, name='usersreq_int'),
    path('user_int/', views.users_int, name='users_int'),

]

handler404 = 'Admin_App.views.custom_404'
