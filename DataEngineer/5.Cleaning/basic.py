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

###Analyzing the data
df.describe()
df['start_location_name'].describe()
df['DURATION'].value_counts(normalize=True)

df['end_location_name'].value_counts(dropna=False)

df.isnull().sum()

###Handling common data issues using pandas
df.drop(columns=['region_id'],inplace=True) #columns
df.drop(index=[3425],inplace=True) #row

df['start_location_name'][(df['start_location_name'].isnull())]

df.dropna(subset=['start_location_name'],inplace=True)

startstop = df[(df['start_location_name'].isnull())&(df['end_location_name'].isnull())]

value = {'start_location_name': 'Start St.', 'end_location_name': 'Stop St. '}

startstop.fillna(value=value)
startstop[['start_location_name','end_location_name']]


may= df[(df['month']=='May')]

df.drop(index= may.index,inplace=True)



##Creating and modifying columns
df.columns = [x.lower() for x in df.columns]

df.rename(columns={'DURATION':'duration'},inplace=True)

##Commit to change permanently conn.commit()

when = '2019-05-23'
x = df[(df['start_location_name'] > when)]
len(x)

##Enriching data
new = pd.DataFrame(df['start_location_name'].value_counts().head())
new.reset_index(inplace=True)
new.columns= ['address','count']