from django.urls import path
from.import views

urlpatterns = [
    path('adduserinfo', views.adduserinfo, name='adduserinfo'),

    path('adminmainpage', views.adminmainpage, name='adminmainpage'),

    path('addteam', views.addteam, name='addteam'),

    path('adddepartment', views.adddepartment, name='adddepartment'),

    path('adddeleteuser', views.adddeleteuser, name='adddeleteuser'),

    path('adddeleteteam', views.adddeleteteam, name='adddeleteteam'),

    path('adddeletedepartment', views.adddeletedepartment, name='adddeletedepartment'),

    path('adddeletecard', views.adddeletecard, name='adddeletecard'),

    path('addcard', views.addcard, name='addcard'),
]