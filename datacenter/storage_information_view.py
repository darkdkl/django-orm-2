from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils import timezone
from datacenter.utilites import get_duration
from datacenter.utilites import is_visit_long
import datetime


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visit in visits:

        visiter = {}
        visiter["who_entered"] = visit.passcard.owner_name
        visiter["entered_at"] = str(visit.entered_at)
        visiter["duration"] = get_duration(visit)
        visiter["is_strange"] = is_visit_long(get_duration(visit))

        non_closed_visits.append(visiter)

    context = {
        "non_closed_visits": non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
