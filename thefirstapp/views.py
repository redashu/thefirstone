from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from .models import Appnames

def default_return(request):
#   return HttpResponse(', '.join(str(name) for name in Appnames.objects.all()))
    names_to_return=Appnames.objects.all()
    return render(request,'thefirstapp/app_frontend.html',{'name_of_apps': names_to_return})

def user_view(request,pk):
    app_details=Appnames.objects.get(pk=pk)
    return render(request,'thefirstapp/detailedview.html',{'appvar': app_details})