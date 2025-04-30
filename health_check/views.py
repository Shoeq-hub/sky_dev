from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import DeliveringValueForm
from .models import DeliveringValue
from django.contrib.auth.decorators import login_required

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

@login_required
def delivering_value_view(request):
    if request.method == 'POST':
        form = DeliveringValueForm(request.POST)
        if form.is_valid():
            dv = form.save(commit=False)
            dv.user = request.user  # Assign the current logged-in user
            dv.save()
            request.session['submitted'] = True  # Set the session variable
            return redirect('confirm_submission')
    else:
        form = DeliveringValueForm()

    return render(request, 'health_check/userhealthcheck.html', {'form': form})

def confirm_submission(request):
    return render(request, 'health_check/confirm.html')


def view_submission(request):
    if request.session.get('submitted', False):
        data = DeliveringValue.objects.latest('submitted_at')
        return render(request, 'health_check/view_submission.html', {'data': data})
    return redirect('delivering_value')


