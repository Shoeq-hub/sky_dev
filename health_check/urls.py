from django.urls import path
from.import views

urlpatterns = [
    path('', views.welcome, name='home'),
    path('profile', views.profile, name='profile'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
    path('menupage/', views.menupage, name='menupage'),
    path('summaryselection/', views.summaryselection, name='summaryselection'),
    path('trendselection/', views.trendselection, name='trendselection'),
    path('linechart/', views.linechart, name='linechart'),
    path('piechart/', views.piechart, name='piechart'),

    path('overallcard/', views.overallcard, name='overallcard'),
    path('singlecard/', views.singlecard, name='singlecard'),

    path('passwordchange/', views.passwordchange, name='passwordchange'),
    
]