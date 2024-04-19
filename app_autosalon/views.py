from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.cache import cache
from app_autosalon.models import Mark, Auto
from app_profile.forms import BookingForm
from app_profile.models import BookingModel
from app_profile.tasks import send_booking_email


# Create your views here.
def get_all_marks(request) -> HttpResponse:
    mark = cache.get('cache_marks')
    # mark = None
    if not mark:
        mark = Mark.objects.all()
        cache.set('cache_marks', mark, timeout=None)

    return render(request, 'app_autosalon/home.html', {'mark': mark})


def get_mark(request, mark) -> HttpResponse:
    mark_name = get_object_or_404(Mark, name=mark)
    autos = Auto.objects.filter(mark=mark_name)
    count = autos.count()
    return render(request, 'app_autosalon/specific_mark.html', {'mark_name': mark_name, 'autos': autos, 'count': count})


def get_auto(request, id: int) -> HttpResponse:
    auto_name = get_object_or_404(Auto, id=id)
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            contact = BookingModel(first_name=form.cleaned_data['first_name'],
                                   last_name=form.cleaned_data['last_name'],
                                   number_phone=form.cleaned_data['number_phone'],
                                   email=form.cleaned_data['email'],
                                   interesting_car=auto_name.id)

            contact.save()
            send_booking_email.delay(
                contact.id,
                auto_name.id,
                contact.first_name,
                contact.last_name,
                contact.number_phone
            )
    else:
        form = BookingForm()

    return render(request,
                  'app_autosalon/auto.html',
                  {'auto': auto_name, 'form': form})
