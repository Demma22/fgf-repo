from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Clan(models.Model):
    clan_name = models.CharField(max_length=250)
    description = models.CharField(max_length=250)
    clan_seat = models.CharField(max_length=250)
    clan_history = models.CharField(max_length=250)
    clan_leader_title = models.CharField(max_length=250)
    clan_leader_name = models.CharField(max_length=250)
    cultural_sites = models.CharField(max_length=250)
    totem = models.CharField(max_length=250)
    secondary_totem = models.CharField(max_length=250)
    common_male_names = models.CharField(max_length=250) #male_names_meaning = models.CharField(max_length=250)
    common_female_names = models.CharField(max_length=250) #female_name_meaning = models.CharField(max_length=250) 
    special_names  = models.CharField(max_length=250) #Meaning  = models.CharField(max_length=250) 
    taboos = models.CharField(max_length=250) 
    spirituality  = models.CharField(max_length=250)  
    known_headgod = models.CharField(max_length=250) #should we add a model for this?
    known_deities = models.CharField(max_length=250) #roles  = models.CharField(max_length=250) 
    images = models.ImageField(null=True, blank=True)
    videos = models.FileField(upload_to='media_files', null=True, blank=True)
    audio = models.FileField(upload_to='media_files', null=True, blank=True)
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    citation = models.CharField(max_length=250)
    date_entered = models.DateTimeField(auto_now_add=True)


class Cultural_Kingdom(models.Model):
    tribe_name = models.CharField(max_length=250)   
    title_of_leader = models.CharField(max_length=250)
    current_king = models.CharField(max_length=250)
    current_chief_name = models.CharField(max_length=250)
    images = models.ImageField(null=True, blank=True)
    videos = models.FileField(upload_to='media_files', null=True, blank=True)
    audio = models.FileField(upload_to='media_files', null=True, blank=True)
    number_of_clans = models.IntegerField(default=1, null=True)
    clan_name = models.ForeignKey(Clan, on_delete=models.SET_NULL, null=True)    

class Tribe(models.Model):
    tribe_name = models.CharField(primary_key=True, max_length=250) 
    region_in_Uganda = models.CharField(max_length=250) 
    language = models.CharField(max_length=250)
    food = models.CharField(max_length=250)
    staple_food = models.CharField(max_length=250)
    cuisine = models.CharField(max_length=250)
    cashcrop = models.CharField(max_length=250)
    economic_activity = models.CharField(max_length=250)
    universal_worship = models.CharField(max_length=250)
    denominations = models.CharField(max_length=250)
    universal_rituals = models.CharField(max_length=250)
    ceremonies = models.CharField(max_length=250)
    kingdom = models.ForeignKey(Cultural_Kingdom, on_delete=models.SET_NULL, null=True)
    chiefdom = models.CharField(max_length=250)
    images = models.ImageField(null=True, blank=True)
    videos = models.FileField(upload_to='media_files', null=True, blank=True)
    audio = models.FileField(upload_to='media_files', null=True, blank=True)
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    citation = models.CharField(max_length=250)
    date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.tribe_name

class Cultural_Identity(models.Model):
    ethnic_group = models.CharField(max_length=250) # to be deleted
    tribe_name = models.ForeignKey(Tribe, on_delete=models.SET_NULL, null=True)  #--> if identity is by tribe and not ethnic group
    notes = models.CharField(max_length=250)
    contributor_name = models.CharField(max_length=250)
    citation = models.CharField(max_length=250)
    images = models.ImageField(null=True, blank=True)
    videos = models.FileField(upload_to='media_files', null=True, blank=True)
    audio = models.FileField(upload_to='media_files', null=True, blank=True)
    contributor_name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
    citation = models.CharField(max_length=250)
    #date_entered = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.ethnic_group
    
    class Meta:
        ordering = ['ethnic_group']

class Ethnic_Group(models.Model):
    ethnical_group_name = models.CharField(max_length=250)
    region_in_Uganda = models.CharField(max_length=250)
    number_of_tribes = models.IntegerField(default=1, null=True)
    number_of_languages = models.IntegerField(default=1, null=True)
    number_of_kingdoms = models.IntegerField(default=1, null=True)
    tribe_name = models.CharField(max_length=250)

    def compute_cultural_entries():
        pass
