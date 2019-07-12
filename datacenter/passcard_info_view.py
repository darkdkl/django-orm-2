from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.utilites import get_duration
from datacenter.utilites import is_visit_long
import datetime




def passcard_info_view(request, passcode):
    
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    user_visits = Visit.objects.filter(passcard=passcard)
    this_passcard_visits=[]
    for visit in user_visits:
      visiter={}
      visiter["entered_at"]=visit.entered_at
      visiter["duration"] = str(get_duration(visit))
      visiter["is_strange"] =is_visit_long(get_duration(visit))
      this_passcard_visits.append(visiter)
    





    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
