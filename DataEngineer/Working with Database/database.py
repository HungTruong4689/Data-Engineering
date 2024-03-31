#Learn how to extraact data from relational and NoSQL databases

#Main topics:
# Inserting and extracting relationnal data in Python
# Inserting and extracting NoSQL database data in Python
# Building database pipelines in AirFlow
# Building database pipelines i Nifi

## SQL Structure Query Language

###Create a database in PostgreSQL with pgAdmin 4 take the following steps
# 1. Browse to http://localhost/pgadmin4
# 2. Expand the serever icon in the Browser pane

### Inserting data into PostgreSQL
#### pyodbc, sqlalchemy, psycopg2

# Installing psycopg2
### Command: python3 -c "import psycopg2"; print(psycopg2.__version__)


## Connecting to PostgreSQL with Python
import psycopg2 as db 
conn_string = "dbname= 'dataengineering' host='localhost' user='postgres' password='postgres'"

#Create the connection object by passing the connection string to the connect() method
conn = db.connect(conn_string)
cur = conn.cursor()


##Inserting data
query = "insert to users(id,name,street,city,zip) value({},'{}','{}','{}','{}')".format(1,'Big Bird','Sesame Street', 'Fakeville','12345')

## mogrigy: to see the query look like
cur.mogrify(query)

## Add mutile records in a single statement
query2 = "insert to users(id,name,street,city,zip) value(%s,%s,%s,%s,%s)"
data = (1,'Big Bird','Sesame Street', 'Fakeville','12345')
cur.mogrify(query2,data)
cur.execute(query2,data)
##Commit to make it permanent
conn.commit()

###Insert mutilple records
## executemany
import psycopg2 as db
from faker import Faker
fake = Faker()
data = []
i = 2
for r in range(1000):
    data.append((i,fake.name(),fake.street_address(), fake.city(), fake.zipcode()))
    i+=1

data_for_db = tuple(data)

conn_string = "dbname= 'dataengineering' host='localhost' user='postgres' password='postgres'"

#Create the connection object by passing the connection string to the connect() method
conn = db.connect(conn_string)
cur = conn.cursor()

query = "insert to users(id,name,street,city,zip) value(%s,%s,%s,%s,%s)"

print(cur.mogrify(query,data_for_db[1]))

cur.executemany(query,data_for_db)
conn.commit()

#Extracting data from PostgreSQL
import psycopg2 as db
conn_string = "dbname= 'dataengineering' host='localhost' user='postgres' password='postgres'"

#Create the connection object by passing the connection string to the connect() method
conn = db.connect(conn_string)
cur = conn.cursor()

query = "select * from users"
cur.execute(query)
## show out the record
for record in cur:
    print(record)

##Alternatively ways
cur.fetchall()
number = 3 # add number if you want to show
cur.fetchmany(number) 
cur.fetchone()
data = cur.fetchone()
print(data[0])
## get the rowcount
cur.rowcount()

## query a table and write it out to a CSV file using the copy_to() method
conn = db.connect(conn_string)
cur = conn.cursor()

f = open('fromdb.csv','w')
cur.copy_to(f, 'users',sep=',')
f.close()
## verify the results
f = open('fromdb.csv','r')
f.read()
