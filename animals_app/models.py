from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Animal_Classification(models.Model): # Kingdom
    kingdom_name = models.CharField(max_length=250)
    species = models.CharField(max_length=250)
    number_of_species = models.IntegerField(default=1, null=True)
    animal_class = models.CharField(max_length=250)
    order = models.CharField(max_length=250)

class Animal(models.Model):
    local_name = models.CharField(max_length=250)
    english_name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    area_in_Uganda = models.CharField(max_length=250)
    animal_classification = models.ForeignKey(Animal_Classification, on_delete=models.SET_NULL, null=True)
    economic_value = models.CharField(max_length=250)
    threats = models.CharField(max_length=250)
    habitat = models.CharField(max_length=250)
    notes = models.CharField(max_length=250)
    images = models.ImageField(null=True, blank=True)
    videos = models.FileField(upload_to='media_files', null=True, blank=True)
    audio = models.FileField(upload_to='media_files', null=True, blank=True)
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    citation = models.CharField(max_length=250)
    date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.local_name
    
    class Meta:
        ordering = ['local_name']
    
    def compute_animal_entries():
        pass