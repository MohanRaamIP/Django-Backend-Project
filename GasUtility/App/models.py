from django.db import models

# Create your models here.
class service(models.Model):
    name = models.CharField(max_length=20)
    service_request = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20)
