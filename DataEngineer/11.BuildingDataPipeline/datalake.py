## Hadoop Distributed File System (HDFS)

from faker import Faker 
import json
import os

os.chdir("/home/paulcrickard/datalake")
fake = Faker()
userid = 1

for i in range(1000):
    name= fake.name()
    fname = name.replace("","-") + '.json'
    data = {"userid": userid,"name":name, "age": fake.random_int(min=19,max=101,step=1), "street": fake.street_address(), "city": fake.city(), "state": fake.state(), "zip": fake.zipcode()}
    datajson = json.dumps(data)
    output = open(fname, "w")
    userid+= 1
    output.write(datajson)
    output.close()

##Building a production data pipeline

### Read files from the data lake
### Insert the files into staging
### Validate the staging data
### Move staging to be warehouse
    
## Reading the data lake

### GetFile
    ### /home/paulcrickard/datalake
    ## regex pattern ^.*\.([jJ][sS][oO][nN]??)$

##EvaluateJSONPath
### UpdateCounter
    
##Querying the staging database
    
### ExecuteSQLRecord
    ## Select count(*) from ${table}

