

# Create your views here.
from django.shortcuts import render

def churn_rate(request):
    v = float(request.POST.get('InitCust', '0'))
    s = float(request.POST.get('CustLost', '0'))

    churn = (s / v * 100) if request.method == 'POST' and v != 0 else 0

    print("Initial Customers =", v)
    print("Customers Lost =", s)
    print("Churn Rate =", churn)

    return render(request, 'masapp/math.html', {
        'v': v,
        's': s,
        'churn': churn
    })