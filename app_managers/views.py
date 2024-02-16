from django.shortcuts import render

from app_managers.models import Manager


# Create your views here.
def get_managers(request):
    managers = Manager.objects.all()
    return render(request,
                  'app_managers/managers_page.html',
                  {"managers": managers})
