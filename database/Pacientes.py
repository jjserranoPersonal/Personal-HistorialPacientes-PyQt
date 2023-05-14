import sys
import os
from database.db import get_db

class Pacientes:

    def __init__(self):
        self.db,self.cursor = get_db() 
     
    def crear_paciente(self, datosPaciente):   
        values = f'''('{datosPaciente['identificacion']}','{datosPaciente['nombres']}',
                  '{datosPaciente['apellidos']}','{datosPaciente['direccion']}',
                  '{datosPaciente['correo']}','{datosPaciente['telefono']}',
                  '{datosPaciente['fechaNacimiento']}','{datosPaciente['sexo']}',
                  '{datosPaciente['transfusiones']}','{datosPaciente['peso']}',
                  '{datosPaciente['talla']}','{datosPaciente['habitosToxicos']}',
                  '{datosPaciente['alergiaMedicamentos']}','{datosPaciente['vacunacion']}',
                  '{datosPaciente['app']}','{datosPaciente['apf']}',
                  '{datosPaciente['nombreAcompanante']}')'''    
        sql = f'''insert into paciente (identificacion, nombres, apellidos, direccion, correo, telefono, 
                fechaNacimiento, sexo, transfusiones, peso, talla, habitosToxicos, alergiaMedicamentos, vacunacion, 
                app, apf, nombreAcompanante) 
                values{values}'''
             
        self.cursor.execute (sql) 
        self.db.commit()

    def consultar_paciente(self, identificacion):
        sql = f"select * from paciente where identificacion='{identificacion}'"
        #values = (identificacion,)
        self.cursor.execute (sql) 
        paciente = self.cursor.fetchone()   
        return paciente
    
    def actualizar_paciente(self, datosPaciente):
        id = f"'{datosPaciente['identificacion']}'"
        sql = f'''update paciente set 
                    identificacion='{datosPaciente['identificacion']}', nombres='{datosPaciente['nombres']}', 
                    apellidos='{datosPaciente['apellidos']}', direccion='{datosPaciente['direccion']}', 
                    correo='{datosPaciente['correo']}', telefono='{datosPaciente['telefono']}', 
                    fechaNacimiento='{datosPaciente['fechaNacimiento']}', sexo='{datosPaciente['sexo']}', 
                    transfusiones='{datosPaciente['transfusiones']}', peso='{datosPaciente['peso']}', 
                    talla='{datosPaciente['talla']}', habitosToxicos='{datosPaciente['habitosToxicos']}', 
                    alergiaMedicamentos='{datosPaciente['alergiaMedicamentos']}', vacunacion='{datosPaciente['vacunacion']}', 
                    app='{datosPaciente['app']}', apf='{datosPaciente['apf']}', 
                    nombreAcompanante='{datosPaciente['nombreAcompanante']}'
                    where identificacion={id}'''
        self.cursor.execute (sql) 
        self.db.commit() 