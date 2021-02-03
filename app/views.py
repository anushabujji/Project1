from django.shortcuts import render,redirect
from django.contrib import messages
def showindex(request):
    return render(request,"index.html")
def Adminlogin(request):
    return render(request,"adminlogin.html")
def Login(request):
    un=request.POST.get("t1")
    up=request.POST.get("t2")
    if un=="anusha" and up=="anusha123":
        return render(request,"adminwelcome.html")
    else:
        messages.error("invalid user")
        return render("adminlogin")
# def Adminwelcome(request):
#     return render(request,"adminwelcome.html")
