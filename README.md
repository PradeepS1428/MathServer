# Ex.03 Design a Website for Server Side Processing
## Date:11.11.2026

## AIM:
To create a web page to calculate Churn Rate using server-side scripts.

## FORMULA:
Churn Rate = (CustLost / InitCust) * 100
<br> InitCust --> Initial Customers Count
<br> CustLost --> Customers Lost Count

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create a HTML file to implement form based input and output.

### Step 5:
Create python programs for views and urls to perform server side processing.

### Step 6:
Receive input values from the form using request.POST.get().

### Step 7:
Calculate the Result using the given formula.

### Step 8:
Display the calculated result in the server console.

### Step 9:
Render the result to the HTML template.

### Step 10:
Publish the website in Localhost.

## PROGRAM:
```
<html>
<body>

<h2>GST BILL CALCULATOR</h2>

<form method="POST">
    {% csrf_token %}

    Enter Price:
    <input type="number" name="price" step="any">

    <br><br>

    Enter GST:
    <input type="number" name="gst" step="any">

    <br><br>

    <button type="submit">Calculate</button>
</form>

<h3>Price: {{ v }}</h3>
<h3>GST: {{ s }}%</h3>
<h3>Total Bill: {{ bill }}</h3>

</body>
</html>

views.py

from django.shortcuts import render
def gst_bill(request):
    v = float(request.POST.get('price', '0'))
    s = float(request.POST.get('gst', '0'))
    bill = v + (v * s / 100) if request.method == 'POST' else 0
    print("price =",v)
    print("gst =",s)
    print("total bill =",bill)
    return render(request, 'masapp/math.html',{'v': v, 's': s, 'bill': bill})

urls.py

from django.contrib import admin
from django.urls import path
from masapp import views

urlpatterns = [path('', views.gst_bill, name='gst_bill'),]
```
## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (71).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (70).png>)

## RESULT:
The the web page to calculate Churn Rate using server-side scripts is created successfully.
