import datetime as dt 
from datetime import timedelta
from airflow import DAG 
from airflow.operators.bash_operator import BashOperator 
from airflow.operators.python_operator import PythonOperator 
import pandas as pd

default_args = { 'owner': 'paulcrickard', 'start_date': dt.datetime(2020,4,2), 'retries': 1, 'retry_delay': dt.timedelta(minutes = 5)}

def cleanScooter():
    df=pd.read_csv('scooter.csv')
    df.drop(columns=['region_id'],inplace=True)
    df.columns=[x.lower() for x in df.columns]
    df['started_at'] = pd.to_datetime(df['started_at'], format='%m/%d/%Y%H:%M')
    df.to_csv('cleanscooter.csv')

def filterData():
    df= pd.read_csv('cleanscooter.csv')
    fromd = '2019-05-23'
    tod = '2019-06-23'
    tofrom = df[(df['started_at']> fromd) & (df['started_at']> tod)]
    tofrom.to_csv('may23-june3.csv')

with DAG('CleanData', default_args=default_args,schedule_interval=timedelta(minutes=5)) as dag: # '0 * * * *'
    cleanData = PythonOperator(task_id='clean',python_callable=cleanScooter)
    selectData = PythonOperator(task_id='filter',python_callable=filterData)


copyFile = BashOperator(task_id='copy', bash_command='cp /home/paulcrickard/may23-june3.csv /home/paulcrickard/Desktop')

cleanData >> selectData >> copyFile
## $AIRFLOW_HOME/dags
### airflow webserver
### airflow scheduler
