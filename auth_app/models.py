from django.db import models
from django.contrib.auth.models import User

GENDER =(
    ("male", "MALE"),
    ("female", "FEMALE"),
    ("don't mention", "DON'T MENTION")
)

class Contributer(models.Model): # should we use the User class
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  
    def submit_contribution():
       pass

class Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True) 
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) # should this be User class?
    approval_complete = models.BooleanField(default=False) #Pending, Approved, Declined