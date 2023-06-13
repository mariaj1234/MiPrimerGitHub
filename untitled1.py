import pymysql #1. pip3 install --upgrade pip 2. pip3 install pymysql

import pandas as pd
import numpy as np
import collections
import itertools
from datetime import date, datetime, timedelta


################ MySQL ###################
database = 'mibd'
username = 'root'
password = '1234'
db = pymysql.connect(host="127.0.0.1", user=username, passwd=password, database=database)
cursor = db.cursor()# prepare a cursor object using cursor() method

def consulta_emp():
    consulta = " SELECT * from empleado "
    print("consulta:", consulta)
    cursor.execute(consulta)
    df = pd.read_sql_query(consulta, db)
    print('type(df)=', type(df))
    print("df.info()=",df.info())
    print("df.describe()=",df.describe())
    print("df.head(10)=",df.head(10))
    print("df.tail(10)=",df.tail(10))
    print("df.sample(20)=",df.sample(20))
    
consulta_emp()

def consulta_dept():
    consulta ='SELECT * from departamento'
    print('consulta:', consulta)
    cursor.execute(consulta)
    df = pd.read_sql_query(consulta, db)
    print('type(df)=', type(df))
    print("df.info()=",df.info())
    print("df.describe()=",df.describe())
    print("df.head(3)=",df.head(3))
    print("df.tail(3)=",df.tail(3))
    print("df.sample(6)=",df.sample(6))

consulta_dept()
 

