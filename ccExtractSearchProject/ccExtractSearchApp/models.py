"""
ccExtractSearchApp | models.py

Author   : Nimish Medatwal
Email    : medatwalnimish@gmail.com
Link     : https://github.com/nimishmedatwal
Linkdin  : https://www.linkedin.com/in/nimishmedatwal/

"""
from django.db import models


class Upload(models.Model):
    file = models.FileField(upload_to='uploaded_files')
    table_name = models.CharField(default="table", max_length=100)
    upload_time = models.DateTimeField(auto_now_add=True)


class Search(models.Model):
    search = models.CharField(default="table", max_length=100)