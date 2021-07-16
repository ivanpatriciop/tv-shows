from os import error
from django.db import models
from django.db.models.base import Model
from datetime import date, datetime 

# Create your models here.


class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        titles_in_db = Show.objects.filter(title =postData['title'])
        if len(titles_in_db) >=1:
            errors["duplicate"]= "El título ingresado ya existe, por favor ingrese otro título."
        if len(postData['title']) < 2:
            errors["title"] = "El título debe contener más de 2 caracteres."
        if int((postData['network_dropdown'])) == -1:
            errors["network"] = "Debe seleccionar una opción válida para network."
        if len(postData["release_date"])< 1:
            errors["release_date"] ="Por favor seleccione una fecha de lanzamiento."
        if datetime.strptime(postData["release_date"], '%Y-%m-%d') > datetime.now():
            errors["wrong_date"] = "La fecha seleccionada no puede ser mayor que le fecha actual."
        if len(postData["description"]) > 0 and len(postData["description"]) < 10:
            errors["description"] = "La descripción es opcional , pero en caso de ingresarla debe contener al menos 10 caracteres."
        return errors


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
    objects = ShowManager()
    
