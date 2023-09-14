from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
GENDER =(
    ("male", "MALE"),
    ("female", "FEMALE"),
    ("don't mention", "DON'T MENTION")
)

class Registered_User(models.Model): # should we use the User class
    user_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=250, choices=GENDER)
    password = models.CharField(max_length=22)
    
    def submit_contribution():
       pass

class Admin_User(models.Model):
    user_name = models.CharField(max_length=250)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    gender = models.CharField(max_length=250, choices=GENDER)

    def upload_new_entry():
        pass
    def approve_contribution():
        #complete_approve = True
        pass
    def review_contribution():
        pass
    def update_contribution():
        pass
    def delete_contribution():
        pass
    def view_contributors():
        pass
    def view_registered_users():
        pass
    def view_reports():  #(and download?):
        pass
    def generate_reports():
        pass

class User_Contribution(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    #contribution = models.ForeignKey(Make_Contribution, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(Registered_User, on_delete=models.CASCADE, null=True) # should this be User class?
    approval_complete = models.BooleanField(default=False) #Pending, Approved, Declined

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
    contributor_name = models.ForeignKey(Registered_User, on_delete=models.SET_NULL, null=True) 
    citation = models.CharField(max_length=250)
    date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.local_name

    class Meta:
        ordering = ['local_name']

    def compute_plant_entries():
        pass


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
    contributor_name = models.ForeignKey(Registered_User, on_delete=models.SET_NULL, null=True) 
    citation = models.CharField(max_length=250)
    date_entered = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.local_name
    
    class Meta:
        ordering = ['local_name']
    
    def compute_animal_entries():
        pass


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
    contributor_name = models.ForeignKey(Registered_User, on_delete=models.CASCADE, null=True) 
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
    contributor_name = models.ForeignKey(Registered_User, on_delete=models.CASCADE, null=True) #on_delete=models.CASCADE
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
    contributor_name = models.ForeignKey(Registered_User, on_delete=models.SET_NULL, null=True) 
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
