from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Medicinal_Use(models.Model):
    health_issue = models.CharField(max_length=250)
    dosage_and_formulation = models.CharField(max_length=250)
    part_used = models.CharField(max_length=250)


class Plant(models.Model):
    local_name = models.CharField(max_length=250)
    english_name = models.CharField(max_length=250)
    scientific_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    areas_in_Uganda = models.CharField(max_length=250)
    life_form = models.CharField(max_length=250)
    climate_impact = models.CharField(max_length=250)
    economic_value = models.CharField(max_length=250)
    medicinal_use = models.ForeignKey(Medicinal_Use, on_delete=models.SET_NULL, null=True)
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

    def compute_plant_entries():
        pass
