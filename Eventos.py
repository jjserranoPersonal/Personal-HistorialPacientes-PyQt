import sys
import os
from db import get_db

class Eventos:

    def __init__(self):
        self.db,self.cursor = get_db() 
     
    def crear_evento(self, datosEvento):       
        sql = '''insert into historial (pacienteId, estado, hea, impDiagnostica, conductaSeguir, motivoConsulta, temperatura, 
                tensionArterial, freCardiaca, freRespiratoria, oxigenacion) 
                values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        values = (datosEvento['pacienteId'],datosEvento['estado'],datosEvento['hea'],
                  datosEvento['impDiagnostica'],datosEvento['conductaSeguir'],datosEvento['motivoConsulta'],
                  datosEvento['temperatura'],datosEvento['tensionArterial'],datosEvento['freCardiaca'],
                  datosEvento['freRespiratoria'],datosEvento['oxigenacion'])
        self.cursor.execute (sql,values) 
        self.db.commit()

    def consultar_historial(self, paciente):
        sql = '''select h.id, h.estado, h.hea, h.impDiagnostica, h.conductaSeguir, h.motivoConsulta, h.temperatura, 
                h.tensionArterial, h.freCardiaca, h.freRespiratoria, h.oxigenacion, h.created_at 
                from paciente p join historial h on p.id = h.pacienteId
                where p.id=%s
                order by h.created_at desc'''
        values = (paciente,)
        self.cursor.execute (sql,values) 
        historial = self.cursor.fetchall()  
        return historial