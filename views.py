import pymongo
from pymongo import MongoClient 
from django.http import HttpResponse


def home(request):
    
    

    #Connecting to connection string of Mongodb
    
    client = pymongo.MongoClient("mongodb+srv://paula:bdat@cluster0.7bawf.mongodb.net/BDAT1004?retryWrites=true&w=majority")
    db = client.test

    # Access database 
    mydatabase = client['BDAT1004'] 
  
    # Access collection of the database 
    mycollection=mydatabase['salesData']

    
    a=mycollection.find()
    
    return HttpResponse(a)  
    