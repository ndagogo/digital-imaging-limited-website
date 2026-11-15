from django.db import models

class AppointmentRequest(models.Model):
    SERVICE_CHOICES = [
        ('Laboratory investigation', 'Laboratory investigation'),
        ('Medical imaging / scan', 'Medical imaging / scan'),
        ('General enquiry', 'General enquiry'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    service = models.CharField(max_length=80, choices=SERVICE_CHOICES)
    preferred_date = models.DateField(null=True, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[('New','New'),('Contacted','Contacted'),('Closed','Closed')], default='New')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.service} ({self.created_at:%d %b %Y})'
