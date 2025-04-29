from django.shortcuts import render

# Create your views here.
def DepSeniormenupage(request):
    return render(request, 'departmentAndSenior_menu_page.html')
