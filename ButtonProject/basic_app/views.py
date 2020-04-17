from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from basic_app.models import SystemStatus
from django.views.generic import View
from django.utils.decorators import method_decorator

#every view is a different function, like:
def index(request):
    return render(request,'basic_app/index.html')


def system_status(request):
    date_list = SystemStatus.objects.order_by('id')
    date_list = date_list.reverse()
    status_dict = {
        'system_status':date_list,
        'last_system_status': date_list.first()
    }
    return render(request, 'basic_app/system_status.html', context=status_dict)

def change_system_status(request, system_status_id):
    if request.method == 'POST':
        previous_system_status = get_object_or_404(SystemStatus, pk=system_status_id)

        new_system_status = SystemStatus()
        new_system_status.status = not previous_system_status.status
        new_system_status.save()

        return HttpResponseRedirect(reverse('system_status'))
    else:
        return HttpResponse("Request method is not a GET")
