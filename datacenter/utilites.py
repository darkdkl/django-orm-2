from django.utils import timezone
import datetime


def is_visit_long(duration, minutes=60):
    
    return duration > datetime.timedelta(minutes=minutes)


def get_duration(visit):
    if visit.leaved_at:
        duration = visit.leaved_at - visit.entered_at
    else:
        duration = timezone.now().replace(microsecond=0) - visit.entered_at
    return datetime.timedelta(seconds=duration.total_seconds())
