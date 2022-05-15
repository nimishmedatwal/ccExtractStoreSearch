"""
ccExtractSearchApp | views.py

Author   : Nimish Medatwal
Email    : medatwalnimish@gmail.com
Link     : https://github.com/nimishmedatwal
Linkdin  : https://www.linkedin.com/in/nimishmedatwal/

"""

from django.views.generic import CreateView
from django.shortcuts import render
import subprocess
from .models import Upload
import boto3
import boto3.dynamodb.conditions as cond
import re
import time
import os

s3 = boto3.resource('s3', verify=False)

dynamodb = boto3.resource('dynamodb', region_name='ap-south-1',aws_access_key_id='AKIAYFEE5XXYQTCNNGHH',aws_secret_access_key='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')
client = boto3.client('dynamodb', region_name='ap-south-1',aws_access_key_id='AKIAYFEE5XXYQTCNNGHH',aws_secret_access_key='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')


class UploadView(CreateView):
    model = Upload
    fields = ["file"]
    template_name = 'files/upload.html'
    success_url = "/"



def dynamoDB(request):
    table_name ="Captions"
    existing_tables = client.list_tables()['TableNames']

    if table_name not in existing_tables:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                },
                
            ],
            
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        time.sleep(5)

    table = dynamodb.Table("Captions")

     

    name_with_extension = request.FILES['file'].name.split('.')
    file_name = name_with_extension[0]

    if len(name_with_extension) > 1:
        file_extension = name_with_extension[1]
    else:
        file_extension = "no extension"

    captionstr = getSRTfileContent(request)
    

    table.put_item(
        Item={
                'name': file_name,
                'extension': file_extension,
                'size': request.FILES['file'].size,
                'captions': str(captionstr),
                'upload date and time': time.ctime()
            }
    )
    
    return UploadView.as_view()(request,{ "result":'SUCCESS'})


def search(request):
    return render(request, "files/file_search.html", { "results":""},)
    
def searchDB(request):
    search_keyword=request.POST.get("search", "")
    table = dynamodb.Table("Captions")
    
    results=table.scan(
                FilterExpression=cond.Attr("captions").contains(search_keyword)

    )
    return_lst= []
    dict_key =1 
    for key,sublst in results.items():
        
        if key == 'Items':  
            for x in range(len(sublst)):
                dict_inner = {} 
                dict_inner['File name']=sublst[x]['name'] + '.' + sublst[x]['extension']
                dict_inner['upload date and time']=sublst[x]['upload date and time']
                dict_inner['captions']=getFilteredCaption(search_keyword,sublst[x]['captions'])
                return_lst.append(dict_inner)
                dict_key=dict_key+1

    return render(request, "files/file_search.html", { "results":return_lst},)

def getSRTfileContent(request):
    # Write bytes to file
    
    captionstring=""
    file=request.FILES['file']
    name_without_extension = file.name.split('.')[0]

    with open('W:/temp/'+file.name, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
            
      
    process = subprocess.Popen(
        ['ccextractorwinfull', '-quiet', 'W:/temp/'+file.name]

    ) 
    time.sleep(10)
    out, err = process.communicate()
    f = open('W:\\temp\\'+name_without_extension+'.srt', 'r')
    captionstring= f.read()
    f.close()
    os.remove('W:\\temp\\'+name_without_extension+'.srt')
    os.remove('W:\\temp\\'+file.name)
    return captionstring.lower()
    
def getFilteredCaption(searchtext,captionstring):
    search_list =[]
    res = captionstring.split()
    substr1=""
    for element in res:
        substr1 = substr1 + element + ' ' 
        if element.isdigit():
            if re.search(searchtext, substr1, re.IGNORECASE):
                search_list.append(substr1)
            
            substr1=""
    return search_list