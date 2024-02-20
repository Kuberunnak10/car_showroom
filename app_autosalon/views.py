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


def get_mark(request, mark):
    mark_name = get_object_or_404(Mark, name=mark)
    autos = Auto.objects.filter(mark=mark_name)
    return render(request, 'app_autosalon/specific_mark.html', {'mark_name': mark_name, 'autos': autos})


def get_auto(request, id):
    auto_name = get_object_or_404(Auto, id=id)

    return render(request, 'app_autosalon/auto.html', {'auto': auto_name})

