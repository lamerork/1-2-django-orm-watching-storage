from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render

def storage_information_view(request):

    non_closed_visits = []

    visits = Visit.objects.filter(leaved_at=None)

    for visit in visits:
        non_closed_visits.append({"who_entered": visit.passcard, "entered_at": visit.entered_at, "duration": visit.format_duration(), "is_strange": visit.is_long()})

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
