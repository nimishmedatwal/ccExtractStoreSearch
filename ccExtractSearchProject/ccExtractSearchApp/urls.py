"""
ccExtractSearchApp | urls.py

Author   : Nimish Medatwal
Email    : medatwalnimish@gmail.com
Link     : https://github.com/nimishmedatwal
Linkdin  : https://www.linkedin.com/in/nimishmedatwal/

"""
from django.urls import path
from . import views


urlpatterns = [
    path('', views.UploadView.as_view(), name='file-upload'),
    path('dynamoDB', views.dynamoDB, name='dynamoDB'),
    path('search', views.search, name='search'),
    path('searchDB', views.searchDB, name='searchDB'),
]