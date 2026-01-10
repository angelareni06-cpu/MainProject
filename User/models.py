from django.db import models
from Guest.models import *
from Reporter.models import *
# Create your models here.
class tbl_complaint(models.Model):
    complaint_title=models.CharField(max_length=50)
    complaint_content=models.CharField(max_length=50)
    complaint_date=models.DateField(auto_now_add=True)
    complaint_reply=models.CharField(max_length=50,null=True)
    complaint_status=models.IntegerField(default=0)
    user_id=models.ForeignKey(tbl_user,on_delete=models.CASCADE,null=True)
    reporter_id=models.ForeignKey(tbl_reporter,on_delete=models.CASCADE,null=True)

class tbl_payment(models.Model):
    payment_date=models.DateField(auto_now_add=True)
    payment_status=models.IntegerField(default=0)
    payment_amount=models.CharField(max_length=50)
    news=models.ForeignKey(tbl_news,on_delete=models.CASCADE)


class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from",null=True)
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)
    editor_to = models.ForeignKey(tbl_editor,on_delete=models.CASCADE,related_name="editor_to",null=True)
    editor_from = models.ForeignKey(tbl_editor,on_delete=models.CASCADE,related_name="editor_from",null=True)
    reporter_to = models.ForeignKey(tbl_reporter,on_delete=models.CASCADE,related_name="reporter_to",null=True)
    reporter_from = models.ForeignKey(tbl_reporter,on_delete=models.CASCADE,related_name="reporter_from",null=True)