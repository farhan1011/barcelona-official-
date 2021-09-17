from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from main.models import Players, Legends, Womens

@login_required
def mainpage(request):
    return render(request,'home.html')
def squad(request):
    pl_list = Players.objects.all()
    context={
        'pl_list':pl_list
    }

    return render(request,'squad.html',context)
def legend(request):
    legend_list= Legends.objects.all()
    return render(request,'legends.html',{'legend_list':legend_list})
def women(request):
    womens_list=Womens.objects.all()

    return render(request,'womens.html',{'womens_list':womens_list})