from django.db import models
from Reporter.models import *
# Create your models here.
class tbl_newsupdatesr(models.Model):
    newsupdatesr_remarks=models.CharField(max_length=50)
    news=models.ForeignKey(tbl_news,on_delete=models.CASCADE,null=True)
    editor=models.ForeignKey(tbl_editor,on_delete=models.CASCADE)