from django.shortcuts import render

# Create your views here.
def adduserinfo(request):
    return render(request, 'add_user_information_page.html')

def adminmainpage(request):
    return render(request, 'admin_main_page.html')

def addteam(request):
    return render(request, 'add_team_page.html')

def adddepartment(request):
    return render(request, 'add_department_page.html')

def adddeleteuser(request):
    return render(request, 'add_delete_users_table.html')

def adddeleteteam(request):
    return render(request, 'add_delete_teams_table.html')

def adddeletedepartment(request):
    return render(request, 'add_delete_department_table.html')

def adddeletecard(request):
    return render(request, 'add_delete_card_table.html')

def addcard(request):
    return render(request, 'add_card_page.html')

