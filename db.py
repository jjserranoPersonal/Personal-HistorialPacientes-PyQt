import mysql.connector
import json

def get_db():

    #Se obtienen variables generales del appConfig
    with open("Recursos/Config/AppConfig.json", encoding="utf-8") as archivo:
        datosAppConfig = json.load(archivo)

    db = mysql.connector.connect(
            host=datosAppConfig['Db']['Host'],
            user=datosAppConfig['Db']['User'],
            password=datosAppConfig['Db']['Password'],
            database=datosAppConfig['Db']['Database'])
    cursor = db.cursor(dictionary=True)

    return db,cursor