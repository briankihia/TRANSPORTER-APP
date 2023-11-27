from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Orders(models.Model):
    goods_value=models.IntegerField()
    deliver_before=models.DateField(null=True)
    distance_to=models.IntegerField()
    transport_fee=models.IntegerField()
    service_fee=models.IntegerField()


