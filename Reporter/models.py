from django.db import models
from Admin.models import *
from Guest.models import *
# Create your models here.
class tbl_news(models.Model): 
    news_title=models.CharField(max_length=50)
    news_content=models.CharField(max_length=50)
    news_image=models.FileField(upload_to="Assets/news/")
    news_date=models.DateField(auto_now_add=True)
    news_status=models.IntegerField(default=0)
    subcategory=models.ForeignKey(tbl_subcategory,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    reporter=models.ForeignKey(tbl_reporter,on_delete=models.CASCADE,null=True)
    verifier=models.ForeignKey(tbl_verifier,on_delete=models.CASCADE,null=True)

class tbl_uploadfiles(models.Model):
    upload_files=models.FileField(upload_to="Assets/news/")
    news=models.ForeignKey(tbl_news,on_delete=models.CASCADE)  