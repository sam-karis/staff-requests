from django.db import models

from staffs.apps.authentication.models import User


class RequestsCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class StaffRequest(models.Model):
    REQUEST_STATUS_CHOICES = [
        ('pending', 'pending'),
        ('lm_stage', 'lm_approved'),
        ('approve', 'approved'),
        ('disapprove', 'disapproved'),
    ]
    request = models.ForeignKey(
        RequestsCategory, max_length=255, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    employee = models.ForeignKey(
        User, related_name='staff_requests', on_delete=models.CASCADE)
    status = models.CharField(
        max_length=25, choices=REQUEST_STATUS_CHOICES, default='default')
    amount = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.employee} ==> {self.request} ==> {self.amount}'
