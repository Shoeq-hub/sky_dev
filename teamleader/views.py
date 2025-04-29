from django.shortcuts import render

# Create your views here.

def adddeleteuser(request):
    return render(request, 'add_delete_user.html')

def cardselectadmin(request):
    return render(request, 'card_select_admin.html')

def cardselecttrend(request):
    return render(request, 'card_select_trend.html')

def overallcardmanager(request):
    return render(request, 'overall_card_trend_manager.html')

def singlecardmanager(request):
    return render(request, 'single_card_trend_manager.html')

def leadermenupage(request):
    return render(request, 'teamleader_menu_page.html')


#from project template folder
def navbar(request):
    return render (request, 'navbar.html')
