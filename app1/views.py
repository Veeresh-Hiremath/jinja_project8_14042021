from django.shortcuts import render
def samp(request):
    return render(request,"sample1.html", context= {'email':"veereshnj126@GMAIL.COM",'name':"veeresh"})
def if_demo(request):
    login=True
    return render(request,"if_demo.html", context={'login':login})
def if_else_demo(request):
    login=True
    return render(request,"if_else_demo.html", context={'login':login,'name':"veeresh",'age':22})
def for_demo(request):
    return render(request,"for_demo.html", context={'items':['apple','cat','ball'],'profile':{'name':"veeresh",'age':22,'sal':15000}})
# Create your views here.
