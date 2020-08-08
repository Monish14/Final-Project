import pandas as pd
import pymongo
from pymongo import MongoClient 

data=pd.read_csv(r'C:\Users\DELL\Desktop\Monish\Data Programming\product.csv',encoding= 'unicode_escape')

client = pymongo.MongoClient("mongodb+srv://paula:bdat@cluster0.7bawf.mongodb.net/BDAT1004?retryWrites=true&w=majority")
db = client.test

# Access database 
mydatabase = client['BDAT1004'] 
  
# Access collection of the database 
mycollection=mydatabase['salesData']


rec2={}
for i in range(len(data.columns)):
    rec2[data.columns[i]]=data[data.columns[i]].values[i]

records = mydatabase.myTable.insert(rec2)

#time.sleep(86400) #sleep for 24 hours
#	else:
#		exit()