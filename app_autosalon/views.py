from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from app_autosalon.models import Mark, Auto


# Create your views here.
def index(request):
    mark = cache.get('cache_marks')
    if not mark:
        mark = Mark.objects.all()
        cache.set('cache_marks', mark)
    return render(request, 'app_autosalon/home.html', {'mark': mark})


def get_mark_name(request, mark):
    mark_name = get_object_or_404(Mark, name=mark)
    auto = Auto.objects.all().filter(mark=mark_name)
    return render(request, 'app_autosalon/specific_mark.html', {'mark_name': mark_name, 'auto': auto})


def mark(request):
    mark = Mark.objects.all()
    return render(request, 'app_autosalon/mark.html', {'mark': mark})
