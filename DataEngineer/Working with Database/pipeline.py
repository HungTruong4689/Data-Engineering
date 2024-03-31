import datetime as dt 
from datetime import timedelta
from airflow import DAG 
from airflow.operators.bash_operator import BashOperator 
from airflow.operators.python_operator import PythonOperator 
import pandas as pd
import psycopg2 as db
import elasticsearch as Elasticsearch

##Start time should be a day behind if you schedule the task to run daily
default_args = { 'owner': 'paulcrickard', 'start_date': dt.datetime(2020,4,2), 'retries': 1, 'retry_delay': dt.timedelta(minutes = 5)}

##PythonOperator
#1 get data from PostgreSQL
#2 insert date into ElasticSearch
with DAG('MyDBdag', default_args=default_args,schedule_interval = timedelta(minutes=5)
         # '0 * * * *' 
         ) as dag:
    getData = PythonOperator(task_id='QueryPostgreSQL', python_callable=queryPostgresql)
    insertData = PythonOperator(task_id='InsertDataElasticsearch', python_callable=insertElasticsearch)
    getData >> insertData

def queryPostgresql():
    conn_string = "dbname= 'dataengineering' host='localhost' user='postgres' password='postgres'"

    #Create the connection object by passing the connection     string to the connect() method
    conn = db.connect(conn_string)
    cur = conn.cursor()

    df = pd.read_sql("select name,city from users",conn)

    ##convert to json to watch
    df.to_csv('postgresqldata.csv')
    print('----Data Saved-----')

def insertElasticsearch():
    es = Elasticsearch()
    df = pd.read_csv('postgresqldata.csv')
    for i,r in df.iterrows():
        doc = r.to_json()
        res = es.index(index='frompostgresql',doc_type="doc", body=doc)
        print(res)

##Runing the DAG - Directed Acylic Graph two tasks combine tasls into a single function

# copy code to $AIRFLOW_HOME/dags
## coding airflow webserver
## airflow scheduler

##Handling databases with NiFi processors
## Extracting data from PostgreSQL
        