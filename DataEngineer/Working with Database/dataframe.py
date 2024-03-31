#Extract data with DataFrames
import psycopg2 as db 
import pandas as pd 


conn_string = "dbname= 'dataengineering' host='localhost' user='postgres' password='postgres'"

#Create the connection object by passing the connection string to the connect() method
conn = db.connect(conn_string)
cur = conn.cursor()

df = pd.read_sql("select * from users",conn)

##convert to json to watch
df.to_json(orient='records')