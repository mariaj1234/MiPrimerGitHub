#Codigo para insertar 1000 tuplas en una tabla:
import pymysql #1. pip3 install --upgrade pip 2. pip3 install pymysql
import pandas as pd
import numpy as np
import collections
import itertools
from datetime import date, datetime, timedelta
import random

################ MySQL ###################
database = 'mibd'
username = 'root'
password = '1234'
db = pymysql.connect(host="127.0.0.1", user=username, passwd=password, database=database)
cursor = db.cursor()# prepare a cursor object using cursor() method


def generar_fecha_aleat():
    inicio = datetime(1940, 1, 1)
    final = datetime(2023, 1, 1)
    random_date = inicio + (final - inicio) * random.random()
    return random_date



db.autocommit(True)
# prepare a cursor object using cursor() method
cursorMySQL = db.cursor()


cursorMySQL.execute("CREATE DATABASE  IF NOT EXISTS musica")
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

lista1= ["Paula", "Caudia", "Disgunting", "Hating", "Making", "Moving", "Catastrophic", "Drinking", "Running", "Driving", "Killing", "Changing", "Printing", "Calling", "Building", "Changing", "Spending", "Talking", "Eating", "Eighteen", "Breaking", "Breaching"]
lista2= ["Pacos", "Tormenta", "Bodega", "Pulpos",  "Talibanes", "Mercenarios", "Cerdos", "Zombies", "Caballos", "Pijamas", "Payasos",  "Piratas", "Bermudas", "Bichos", "Falling", "Calamares", "Carros", "Corsarios", "Vigo", "Zopenco", "Uruguayos", "Átomos", "Ineptos", "Alguaciles", "Ejecutivos"]
rol = ["vocalista", "pianista", "bajo", "vocalista", "batería", "violonchelista", "sasofonista"]
for i in range(1000):
    parte1 = random.choice (lista1)
    parte2= random.choice (lista2)
    nombre_grupo = parte1+" "+parte2
    print (nombre_grupo)
   
    rol = random.choice (rol_musicales)
   
   
    cursor.execute("INSERT INTO artista (id, nombre, fecha_nacimiento, rol, id_grupo) VALUES (%s,%s,%s,%s,%s);",(i, nombre_grupo, random.randint(2, 10), generar_fecha_aleat(), genero))
   
   
   
   
   
db.close() # desconecta del servidor local

print("Fin del programa...")