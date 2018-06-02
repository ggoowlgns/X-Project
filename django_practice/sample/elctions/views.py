from django.shortcuts import render
from django.http import HttpResponse
from .models import Candidate

# Create your views here.

def index(request):
    candidates = Candidate.objects.all() #해당 table의 모든 정보를 가져옴
    no1 = Candidate.objects.filter(party_number = 1) #select party_number 한것만 가져옴
    str = ''
    for candidate in no1:
        str += "{} 기호 {}번({})<br>".format(candidate.name,candidate.party_number,candidate.area)
        str += candidate.introduction+"</p>"

    #############context만들어서 html로 보내기########
    context = {'candidates': candidates}


    return render(request, 'elctions/index.html',context)

def areas(request , area):
    return HttpResponse(area)