from django.db import models 

# Create your models here.
class tbl_district(models.Model):
    district_name=models.CharField(max_length=50)

class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=50)
    admin_email=models.CharField(max_length=50)
    admin_photo=models.FileField(upload_to="Assets/UserDocs/",null=True)
    admin_password=models.CharField(max_length=50) 

class tbl_category(models.Model):
    category_name=models.CharField(max_length=50)  

class tbl_place(models.Model):
    place_name=models.CharField(max_length=50)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=50)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

class tbl_freelancertype(models.Model):
    freelancer_type=models.CharField(max_length=50)  

class tbl_skilltype(models.Model):
    skill_type=models.CharField(max_length=50)    
    freelancer_type=models.ForeignKey(tbl_freelancertype,on_delete=models.CASCADE)

class tbl_editor(models.Model):
    editor_name=models.CharField(max_length=50)
    editor_email=models.CharField(max_length=50)
    editor_contact=models.CharField(max_length=50)    
    editor_photo=models.FileField(upload_to="Assets/UserDocs/")
    editor_proof=models.FileField(upload_to="Assets/UserDocs/")
    editor_password=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE)
    
class tbl_verifier(models.Model):
    verifier_name=models.CharField(max_length=50)
    verifier_email=models.CharField(max_length=50)
    verifier_contact=models.CharField(max_length=50)
    verifier_photo=models.FileField(upload_to="Assets/UserDocs/")
    verifier_proof=models.FileField(upload_to="Assets/UserDocs/")
    verifier_password=models.CharField(max_length=50)
    place=models.ForeignKey(tbl_place,on_delete=models.CASCADE) 
    
class tbl_plan(models.Model):
    plan_name=models.CharField(max_length=50)
    plan_duration=models.CharField(max_length=50)
    plan_amount=models.CharField(max_length=50)