from django.shortcuts import render
from .models import Fund

# Create your views here.
def notFound(request):
    pass

def invalid(request):
    pass

def home(request):
    user = request.user
    try:
        fund = Fund.objects.get(user=user)
    except:
        fund = Fund.objects.create(user=user, spendables=0, savings=0)

    savings_amount = round(fund.savings, 2)
    spendable_amount = round(fund.spendables, 2)

    return render(request, 'funds/index.html', {
        'spending' : spendable_amount,
        'savings' : savings_amount}
        )