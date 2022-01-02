from django.shortcuts import render
from .models import Transaction
from funds.models import Fund
from django.http import HttpResponseRedirect
import datetime

# Create your views here.
def transactions(request):
    transactions = Transaction.objects.filter(user=request.user)
    all_transactions = []
    for transaction in transactions:
        all_transactions.append(transaction)

    return render(request, 'transactions/tansaction.html', {'transactions' : all_transactions})

def add(request, val):
    amount = float(val)
    date = datetime.date.today()
    time = datetime.datetime.now().strftime("%H:%M:%S")

    transaction = Transaction.objects.create(user=request.user, amount=amount, reason="", date=date, time=time)
    try:
        fund = Fund.objects.get(user = request.user)
    except:
        fund = Fund.objects.create(request.user, 0, 0)

    savings = amount*.2
    fund.savings += savings
    fund.spendables += (amount - savings)
    fund.save()

    return HttpResponseRedirect('/')

def withdraw(request):
    pass

def transfer(request):
    pass