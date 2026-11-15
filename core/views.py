from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils.dateparse import parse_date
from .models import AppointmentRequest

SERVICES = [
    {'number':'01', 'title':'Medical Laboratory', 'copy':'Laboratory investigations to support clinical assessment, screening and ongoing health monitoring.', 'icon':'microscope'},
    {'number':'02', 'title':'Diagnostic Imaging', 'copy':'Imaging services and scans to support clearer clinical insight and informed care decisions.', 'icon':'scan'},
    {'number':'03', 'title':'Patient Support', 'copy':'A welcoming team to guide you through enquiries, preparation information and your visit.', 'icon':'heart'},
]

def home(request):
    return render(request, 'core/home.html', {'services': SERVICES[:3]})

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html', {'services': SERVICES})

def contact(request):
    return render(request, 'core/contact.html')

def appointment(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        phone = request.POST.get('phone', '').strip()
        service = request.POST.get('service', 'General enquiry')
        if not name or not phone:
            messages.error(request, 'Please provide your name and phone number.')
        else:
            AppointmentRequest.objects.create(
                name=name, phone=phone, email=request.POST.get('email', '').strip(),
                service=service, preferred_date=parse_date(request.POST.get('preferred_date', '')),
                message=request.POST.get('message', '').strip(),
            )
            messages.success(request, 'Thank you. Your request has been received. Our team will contact you to confirm the details.')
            return redirect('appointment')
    return render(request, 'core/appointment.html')

def healthz(request):
    return HttpResponse('ok', content_type='text/plain')
