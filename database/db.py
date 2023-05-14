import mysql.connector
import json
import sqlite3

def get_db():

    #Se obtienen variables generales del appConfig
    with open("Recursos/Config/AppConfig.json", encoding="utf-8") as archivo:
        datosAppConfig = json.load(archivo)

    if datosAppConfig['tipoDB'] == "mysql":
        db = mysql.connector.connect(
                host=datosAppConfig['Db']['Host'],
                user=datosAppConfig['Db']['User'],
                password=datosAppConfig['Db']['Password'],
                database=datosAppConfig['Db']['Database'])
        cursor = db.cursor(dictionary=True)

        return db,cursor
    
    if datosAppConfig['tipoDB'] == "sqlite":
        try:
            db = sqlite3.connect(datosAppConfig['DatabaseSQLite'])
            db.row_factory = dict_factory
            cursor = db.cursor()
            return db,cursor
        except Exception as ex:
            print(ex)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d    