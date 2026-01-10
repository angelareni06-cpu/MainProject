from django.db import models
from Admin.models import *
# Create your models here.
class tbl_user(models.Model):
    user_name=models.CharField(max_length=50)
    user_email=models.CharField(max_length=50)
    user_contact=models.CharField(max_length=50)
    user_gender=models.CharField(max_length=50)
    user_dob=models.CharField(max_length=50)
    user_address=models.CharField(max_length=80)
    user_photo=models.FileField(upload_to="Assets/UserDocs/")
    user_proof=models.FileField(upload_to="Assets/UserDocs/")
    user_work=models.FileField(upload_to="Assets/UserDocs/")
    skill_type=models.ForeignKey(tbl_skilltype,on_delete=models.CASCADE)
    user_level=models.CharField(max_length=50)
    user_bio=models.CharField(max_length=50)
    user_social=models.CharField(max_length=50)
    user_password=models.CharField(max_length=50)
    user_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)

class tbl_reporter(models.Model):
    reporter_name=models.CharField(max_length=50)
    reporter_email=models.CharField(max_length=50) 
    reporter_contact=models.CharField(max_length=50)  
    reporter_gender=models.CharField(max_length=50)
    reporter_dob=models.CharField(max_length=50)
    reporter_address=models.CharField(max_length=50, null=True, blank=True)
    reporter_password=models.CharField(max_length=50)
    reporter_photo=models.FileField(upload_to="Assets/UserDocs/")
    reporter_proof=models.FileField(upload_to="Assets/UserDocs/")
    reporter_status=models.IntegerField(default=0)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
