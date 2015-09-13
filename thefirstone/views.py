from django.shortcuts import render

def default_return(request):
    return render(request,"homepage.html")

def neeraj_return(request):
    return render(request,"neeraj.html")
