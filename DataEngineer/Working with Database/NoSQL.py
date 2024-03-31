## Inserting and extracting NoSQL databasee in Python
#### Elasticsearch
## install elasticsearch pip3 install elasticsearch

import elasticsearch
elasticsearch.__version__
import pandas as pd 

## Insert data into ElasticSearch
from elasticsearch import Elasticsearch
from faker import Faker
fake = Faker()

es = Elasticsearch()
## install on localhost
es = Elasticsearch({'127.0.0.1'})

doc = {"name": fake.name(), "street": fake.street_address, "city": fake.city(), "zip": fake.zipcode()}
res = es.index(index = "users", doc_type="doc", body=doc)
print(res['result']) # created

## inserting data using helpers
from elasticsearch import helpers

df = pd.read_sql("select * from users",conn)

actions = [{ "_index": "users", "_type": "doc", "_source": {"name": fake.name(), "street": fake.street_address(), "city": fake.city(), "zip": fake.zipcode()}} for x in range(998) for i,r in df.iterrows()]

res = helpers.bulk(es,actions)
print(res['result'])

## Query Elasticsearch
## Insert data into ElasticSearch
from elasticsearch import Elasticsearch
from faker import Faker
fake = Faker()

es = Elasticsearch()
doc = {"query": {"match_all": {}}}

res = es.search(index="users",body=doc,size=10)
print(res['hits']['hits'])
# iterate through grabbing _source only
for doc in res['hits']['hits']:
    print(doc['_source'])


##normalize the data
from pandas.io.json import json_normalize
df = json_normalize(res['hits']['hits'])
doc = {"query": {"match": {"name": "Ronald Goodman"}}}
res = es.search(index="users",body=doc,size=10)
print(res['hits']['hits'][0]['_source'])

#Lucene syntax

res = es.search(index="users",q="name:Ronald Goodman",size=10)
print(res['hits']['hits'][0]['_source'])

##filter
doc = {"query": {"bool":{ "must": {"match": {"city": "Jamesberg"}}, "filter":{"term": {"zip": "63792"}}}}}
res = es.search(index="users",body=doc,size=10)
print(res['hits']['hits'])

##Scroll method