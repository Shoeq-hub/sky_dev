from django.urls import path
from.import views

urlpatterns = [
    path('adddeleteuser', views.adddeleteuser, name='adddeleteuser'),
    path('cardselectadmin', views.cardselectadmin, name='cardselectadmin'),
    path('cardselecttrend', views.cardselecttrend, name='cardselecttrend'),
    path('overallcardmanager', views.overallcardmanager, name='overallcardmanager'),
    path('singlecardmanager', views.singlecardmanager, name='singlecardmanager'),
    path('leadermenupage', views.leadermenupage, name='leadermenupage'),
    

]