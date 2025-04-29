from django.shortcuts import render

# Create your views here.

def welcome(request):
    return render(request, 'health_check/welcome_to_healthcheck_page.html')

def profile(request):
    return render(request, 'health_check/edit_details_page.html')

def logoutmessage(request):
    return render(request, 'health_check/log_out_message_page.html')

def menupage(request):
    return render(request, 'health_check/user_menu_page.html')

def summaryselection(request):
    return render(request, 'health_check/user_summary_selection_page.html')

def trendselection(request):
    return render(request, 'health_check/view_trends_page.html')

def linechart(request):
    return render(request, 'health_check/user_linechart.html')

def piechart(request):
    return render(request, 'health_check/user_piechart.html')

def overallcard(request):
    return render(request, 'health_check/overall_cards_trend.html')

def singlecard(request):
    return render(request, 'health_check/single_card_trends.html')

def passwordchange(request):
    return render(request, 'health_check/password_change_page.html')
#from project template folder
def navbar(request):
    return render (request, 'navbar.html')
