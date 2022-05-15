"""
ccExtractSearchProject | urls.py

Author   : Nimish Medatwal
Email    : medatwalnimish@gmail.com
Link     : https://github.com/nimishmedatwal
Linkdin  : https://www.linkedin.com/in/nimishmedatwal/

"""
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ccExtractSearchApp.urls')),
]
