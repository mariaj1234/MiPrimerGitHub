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
######cursor = db.cursor()# prepare a cursor object using cursor() method



db.autocommit(True)
# prepare a cursor object using cursor() method
cursorMySQL = db.cursor()


cursorMySQL.execute("CREATE DATABASE if not exists Musica")
cursorMySQL.execute("select @@version")
output = cursorMySQL .fetchall()
print(output)

cursorMySQL.execute("USE musica")

cursorMySQL.execute(
   " CREATE TABLE  IF NOT EXISTS grupo( "\
      " id int NOT NULL, "\
      " nombre varchar(45) DEFAULT NULL, "\
      " numero_miembros INT DEFAULT NULL, "\
      " fecha_fundacion DATE DEFAULT NULL, "\
      " genero varchar(45) DEFAULT NULL, "\
      " PRIMARY KEY (id) "\
   " ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci "
)

cursorMySQL.execute(
   " CREATE TABLE  IF NOT EXISTS artista( "\
      " id int NOT NULL, "\
      " nombre varchar(45) DEFAULT NULL, "\
      " fecha_nacimiento DATE DEFAULT NULL, "\
      " rol varchar(45) DEFAULT NULL, "\
      " id_grupo INT,  "\
      " PRIMARY KEY (id), "\
      " FOREIGN KEY (id_grupo) REFERENCES grupo(id)"\
   " ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci "
)

cursorMySQL. execute(
    "INSERT INTO grupo (id, nombre, numero_mienbros, fecha_fundacion, genero) VALUES (%s, %s, %s, %s, %s)",\
  ('1', 'Aerosmith', '5', '1970', 'Had Rock'),\
  ('2', 'Nirvana' '3', '1989', 'Had Rock'),\
  ('3', 'Iron Maiden' '6', '1980', 'Had Rock'),\
  ('4', 'Mago de Oz' '8', '1988', 'Had Rock'),\
  ('5', 'AC/DC' '5', '1973', 'Had Rock'),\
 )   
    
db.close() # desconecta del servidor local

print("Fin del programa...")

