from django.contrib import admin
from .models import AppointmentRequest

@admin.register(AppointmentRequest)
class AppointmentRequestAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'service', 'preferred_date', 'status', 'created_at')
    list_filter = ('status', 'service', 'created_at')
    search_fields = ('name', 'phone', 'email')
    readonly_fields = ('created_at',)
    list_editable = ('status',)
