from django.shortcuts import render, get_object_or_404

from app_autosalon.models import Mark, Auto


# Create your views here.
def index(request):
    mark = Mark.objects.all()
    return render(request, 'app_autosalon/home.html', {'mark': mark})


def get_mark_name(request, mark):
    mark_name = get_object_or_404(Mark, name=mark)
    auto = Auto.objects.all().filter(mark=mark_name)
    return render(request, 'app_autosalon/specific_mark.html', {'mark_name': mark_name, 'auto': auto})
