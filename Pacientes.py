import sys
import os
from db import get_db

class Pacientes:

    def __init__(self):
        self.db,self.cursor = get_db() 
     
    def crear_paciente(self, datosPaciente):       
        sql = '''insert into paciente (identificacion, nombres, apellidos, direccion, correo, telefono, 
                fechaNacimiento, sexo, transfusiones, peso, talla, habitosToxicos, alergiaMedicamentos, vacunacion, 
                app, apf, nombreAcompanante) 
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        values = (datosPaciente['identificacion'],datosPaciente['nombres'],
                  datosPaciente['apellidos'],datosPaciente['direccion'],
                  datosPaciente['correo'],datosPaciente['telefono'],
                  datosPaciente['fechaNacimiento'],datosPaciente['sexo'],
                  datosPaciente['transfusiones'],datosPaciente['peso'],
                  datosPaciente['talla'],datosPaciente['habitosToxicos'],
                  datosPaciente['alergiaMedicamentos'],datosPaciente['vacunacion'],
                  datosPaciente['app'],datosPaciente['apf'],
                  datosPaciente['nombreAcompanante'])
        self.cursor.execute (sql,values) 
        self.db.commit()

    def consultar_paciente(self, identificacion):
        sql = '''select * from paciente where identificacion=%s'''
        values = (identificacion,)
        self.cursor.execute (sql,values) 
        paciente = self.cursor.fetchone()   
        return paciente
    
    def actualizar_paciente(self, datosPaciente):
        sql = '''update paciente set identificacion=%s, nombres=%s, apellidos=%s, direccion=%s, correo=%s, 
                telefono=%s, fechaNacimiento=%s, sexo=%s, transfusiones=%s, peso=%s, talla=%s, habitosToxicos=%s, 
                alergiaMedicamentos=%s, vacunacion=%s, app=%s, apf=%s, nombreAcompanante=%s
                where identificacion=%s'''
        values = (datosPaciente['identificacion'],datosPaciente['nombres'],
                  datosPaciente['apellidos'],datosPaciente['direccion'],
                  datosPaciente['correo'],datosPaciente['telefono'],
                  datosPaciente['fechaNacimiento'],datosPaciente['sexo'],
                  datosPaciente['transfusiones'],datosPaciente['peso'],
                  datosPaciente['talla'],datosPaciente['habitosToxicos'],
                  datosPaciente['alergiaMedicamentos'],datosPaciente['vacunacion'],
                  datosPaciente['app'],datosPaciente['apf'],
                  datosPaciente['nombreAcompanante'],datosPaciente['identificacion'])
        self.cursor.execute (sql,values) 
        self.db.commit() 