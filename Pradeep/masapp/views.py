from django.shortcuts import render
def gst_bill(request):
    v = float(request.POST.get('price', '0'))
    s = float(request.POST.get('gst', '0'))
    bill = v + (v * s / 100) if request.method == 'POST' else 0
    print("price =",v)
    print("gst =",s)
    print("total bill =",bill)
    return render(request, 'masapp/math.html',{'v': v, 's': s, 'bill': bill})