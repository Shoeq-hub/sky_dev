from django.urls import path
from.import views

urlpatterns = [
    path('', views.home, name="health_check_home"),
    path('vote/', views.vote, name='health_check_vote'),
    path('userSele/', views.userSelect, name='health_check_userSele'),
]