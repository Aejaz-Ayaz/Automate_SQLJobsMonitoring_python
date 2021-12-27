'''
This code gives the list of all failed SQL agents jobs for today's date, within the given SQL server instance
'''

import pandas as pd
from sqlalchemy import create_engine
import urllib
from datetime import datetime

driver = '{SQL Server}'
server = '**add your server name**'
user = '**add user id**'
password = '**add password**'
database = 'msdb'                   # this should always be msdb since the SQL jobs related data/SPs resides within this database

params = urllib.parse.quote_plus(r'DRIVER={};SERVER={};DATABASE={};UID={};PWD={}'.format(driver, server, database, user, password))
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)
conn = create_engine(conn_str)


# alert on failure
def alert(job_name, last_run):
    
    print('{} failed at {}'.format(job_name, last_run))
    
def sql_monitoring():
    
    # read from existing function on msdb
    df = pd.read_sql('EXEC msdb.dbo.sp_help_jobactivity;', conn)

    # order by last_executed_step_date
    df['last_executed_step_date'] = pd.to_datetime(df['last_executed_step_date']).apply(lambda x: x.date())
    df['last_executed_step_date'] = df['last_executed_step_date'].astype(str)

    # create a dataframe that contains jobs executed today
    df_today = df[df['last_executed_step_date'] == datetime.today().strftime("%Y-%m-%d")]

    # create a dataframe that contains the jobs that have failed
    df_failed = df_today[df_today['run_status'] == 0]

    if len(df_failed) > 0:

        for index, element in df_failed.iterrows():

            alert(element['job_name'], element['last_executed_step_date'])
            
sql_monitoring()
