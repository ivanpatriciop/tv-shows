from django.db import models
from django.db.models.base import Model

# Create your models here.


class Network(models.Model):
    name = models.CharField(max_length=50)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
class Show(models.Model):
    title = models.CharField(max_length= 50)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    modified_at = models.DateTimeField(auto_now= True)
    network = models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    

    
