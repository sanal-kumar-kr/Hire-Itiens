from django.urls import path,include
from .import views
urlpatterns=[
    path('postjobs',views.postjobs),
    path('viewjobs',views.viewjobs),
    path('AddIntervies',views.AddIntervies),
    path('ViewInterviews',views.ViewIntervies),
    path('requests_int',views.request_int),

    path('addprograms/<int:t>',views.addprograms),
    path('viewprograms/<int:t>',views.viewprograms),
    path('jobvisits',views.jobvisits),
    path('collegereq',views.collegereq),
    path('editprogram/<int:id>',views.editprogram),
    path('interviewedit/<int:id>',views.interviewedit),
    path('vaccancieedit/<int:id>',views.vaccancieedit),
    path('chat/<int:id>', views.message, name='dg'),
    path('view_com',views.viewcompany),
    path('viewchatusers',views.viewchatusers),
    path('viewchatreq',views.viewchatreq),
    path('acceptchatrequest/<int:id>',views.acceptchatrequest),

    path('sendchatrequest/<int:cid>',views.sendchatrequest),
    path('deleteprogram/<int:id>',views.deleteprogram),
    path('deleteinterview/<int:id>',views.deleteinterview),
    path('deletevaccancie/<int:id>',views.deletevaccancie),

]
handler404 = 'Company.views.custom_404'
