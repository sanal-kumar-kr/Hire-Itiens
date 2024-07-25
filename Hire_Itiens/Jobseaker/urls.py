from django.urls import path,include
from .import views
urlpatterns=[
    # path('',views.)
    path('sendrequests/<int:id>',views.sendrequests),
    path('Applyjob/<int:id>',views.Applyjobs),
    path('applications',views.applications),
    path('savejob/<int:id>',views.savejob),
    path('viewsaved',views.viewsaved),
    path('deletesavejob/<int:id>',views.deletesavejob),
    path('cancelreq/<int:id>',views.cancelreq),


]