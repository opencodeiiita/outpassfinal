from django.conf import settings
from django.db import models
from django.utils import timezone


class Request(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE , null=True)
    subject= models.CharField(max_length=200)
    description = models.TextField()
    parent_email = models.CharField(max_length=200 , verbose_name="Parent's Email" , null=True)
    roll = models.CharField(max_length=10,null=True)
    date = models.DateField(verbose_name="Date" , default=timezone.now().date() , null=True)
    end_date = models.DateField(verbose_name="End Date", blank=True , null=True)
    time = models.TimeField(verbose_name="Time" , default=timezone.now().time() , null=True)
    end_time = models.TimeField(verbose_name="End Time", blank=True , null=True)
    venue = models.CharField(max_length=512, verbose_name="Venue", blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    perm = models.BooleanField(default=False, verbose_name="Permission Granted")

    def approve(self):
        self.perm = True
        self.save()

    def __str__(self):
        return self.subject
