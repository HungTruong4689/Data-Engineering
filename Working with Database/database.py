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

