import uuid
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2085)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    
class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=250)
    discount = models.FloatField()
    
    
