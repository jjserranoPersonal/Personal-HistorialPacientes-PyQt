import sys
import os
from database.db import get_db

class Eventos:

    def __init__(self):
        self.db,self.cursor = get_db() 
     
    def crear_evento(self, datosEvento):
        values = f'''('{datosEvento['pacienteId']}','{datosEvento['estado']}','{datosEvento['hea']}',
                  '{datosEvento['impDiagnostica']}','{datosEvento['conductaSeguir']}','{datosEvento['motivoConsulta']}',
                  '{datosEvento['temperatura']}','{datosEvento['tensionArterial']}','{datosEvento['freCardiaca']}',
                  '{datosEvento['freRespiratoria']}','{datosEvento['oxigenacion']}')'''      
        sql = f'''insert into historial (pacienteId, estado, hea, impDiagnostica, conductaSeguir, motivoConsulta, temperatura, 
                tensionArterial, freCardiaca, freRespiratoria, oxigenacion) 
                values{values}'''
        self.cursor.execute (sql) 
        self.db.commit()

    def consultar_historial(self, paciente):
        sql = f'''select h.id, h.estado, h.hea, h.impDiagnostica, h.conductaSeguir, h.motivoConsulta, h.temperatura, 
                h.tensionArterial, h.freCardiaca, h.freRespiratoria, h.oxigenacion, h.created_at 
                from paciente p join historial h on p.id = h.pacienteId
                where p.id='{paciente}'
                order by h.created_at desc'''
        #values = (paciente,)
        self.cursor.execute (sql) 
        historial = self.cursor.fetchall()  
        return historial