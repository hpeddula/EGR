from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Company,User
from .forms import NameForm
# Create your views here.
def index(request):
    return render(request,template_name='index.html')

def c1(request):
    company1 = Company.objects.get(id=1);
    user1 = User.objects.filter(company_id=company1.id);
    return render(request,template_name='c1.html',context={'company1':company1,'user1':user1})

def c2(request):
    company2 = Company.objects.get(id=3);
    user2 = User.objects.filter(company_id=company2.id);
    return render(request,template_name='c2.html',context={'company2':company2,'user2':user2})

def c3(request):
    company3 = Company.objects.filter(id=3);
    return render(request,template_name='c3.html',context={'company3':company3})

def c4(request):
    company4 = Company.objects.filter(id=4);
    return render(request,template_name='c4.html',context={'company4':company4})

def c5(request):
    company5 = Company.objects.filter(id=5);
    return render(request,template_name='c5.html',context={'company5':company5})

def c6(request):
    company6 = Company.objects.filter(id=6);
    return render(request,template_name='c6.html',context={'company6':company6})


def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = NameForm()
        return render(request,'name.html',{'form':form})
