import pandas as pd 
df = pd.read_csv('scooter.csv')

df.columnsIndex(['month','trip_id','region_id','vehicle_id','started_at','ended_at','DURATION','start_location_name','end_location_name','user_id','trip_ledger_id'], dtype='objects')

df.dtypes

pd.set_option('display.max_columns',500)

user = df.where(df['user_id']==8417864)

one = df['user_id'] == 8417864
two = df['trip_ledger_id'] == 1488838 
df.where(one & two)
df[(one)& (two)]