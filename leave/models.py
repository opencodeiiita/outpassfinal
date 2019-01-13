from django.conf import settings
from django.db import models
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


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

@receiver(post_save, sender=Request)
def update_request(sender, instance, created, **kwargs):
    obj= kwargs[instance]
    requests = get_object_or_404(Request, pk=obj.pk)
    if requests.perm:
        send_mail(requests.subject, requests.description, settings.EMAIL_HOST_USER,
        [requests.roll+'@iiita.ac.in'], fail_silently=False)
    instance.profile.save()
