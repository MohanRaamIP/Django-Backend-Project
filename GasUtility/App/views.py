from django.shortcuts import render, get_object_or_404, redirect
from .models import service
from .forms import ServiceRequestForm

def service_request_list(request):
    service_requests = service.objects.all()
    return render(request, 'App/service_request_list.html', {'service_requests': service_requests})

def service_request_detail(request, pk):
    service_request = get_object_or_404(service, pk=pk)
    return render(request, 'App/service_request_detail.html', {'service_request': service_request})

def service_request_create(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm()
    return render(request, 'App/service_request_form.html', {'form': form})

def service_request_update(request, pk):
    service_request = get_object_or_404(service, pk=pk)
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, instance=service_request)
        if form.is_valid():
            form.save()
            return redirect('service_request_list')
    else:
        form = ServiceRequestForm(instance=service_request)
    return render(request, 'App/service_request_form.html', {'form': form})

def service_request_delete(request, pk):
    service_request = get_object_or_404(service, pk=pk)
    if request.method == 'POST':
        service_request.delete()
        return redirect('service_request_list')
    return render(request, 'App/service_request_confirm_delete.html', {'service_request': service_request})
