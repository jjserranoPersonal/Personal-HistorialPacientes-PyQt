import sys
import os
from PyQt5.QtWidgets  import QApplication, QWidget, QMainWindow, QMessageBox, QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore  import Qt
from PyQt5 import uic
from datetime import datetime
import shutil
from database.Pacientes import Pacientes
from database.Eventos import Eventos
from dateutil.relativedelta import relativedelta
from validaciones import *
from PDF_Historia_Clinica import PdfHistoriaClinica
import webbrowser
import json

class Principal(QMainWindow):

    def __init__(self, usuario):
        super().__init__()
        uic.loadUi("Recursos/UI/HistorialPacientes.ui", self)
        self.label_3.setText(usuario)

        self.btnConsultarDatos.clicked.connect(self.p_consultar_paciente)
        self.btnCrear.clicked.connect(self.p_crear_paciente)  
        self.btnActualizar.clicked.connect(self.p_actulizar_paciente)     
        self.btnCrearEvento.clicked.connect(self.p_crear_evento)    
        self.btnConsultarHistorial.clicked.connect(self.p_consultar_historial) 
        self.btnCargarFoto.clicked.connect(self.p_cargar_foto)  
        self.btnLimpiar.clicked.connect(self.p_limpiar_front)  
        self.btnLimpiar_2.clicked.connect(self.p_limpiar_front_eventos) 
        self.btnLimpiar_3.clicked.connect(self.p_limpiar_front_historial) 
        self.btnDescargarHistorial.clicked.connect(self.p_descargar_Historial) 
        self.btnSubirSoporte.clicked.connect(self.p_subir_soportes) 
        self.btnConsultarSoportes.clicked.connect(self.p_consultar_soportes) 

        #Se obtienen variables generales del appConfig
        with open("Recursos/Config/AppConfig.json", encoding="utf-8") as archivo:
            self.datosAppConfig = json.load(archivo)
 
    def p_consultar_paciente(self):
        try:
            pacientes = Pacientes()  
            identificacion = self.text_identificacion.text()
            #Validaciones y acciones
            if validar_identificacion(identificacion):
                paciente = pacientes.consultar_paciente(identificacion)
                if paciente is None: 
                    self.p_alerta("Error","Paciente no existe!!!")
                else:
                    self.p_alerta("Exito","Paciente consultado con exito!!!")
                    self.p_asignar_datos_front(paciente)
                    self.btnActualizar.setEnabled(True)
                    self.text_identificacion_2.setText(identificacion)    
                    self.text_identificacion_3.setText(identificacion)
                    self.p_calcuar_edad(paciente['fechaNacimiento'])  
                    self.p_obtener_foto(identificacion)         
            else:
                self.p_alerta("Error","Datos no superaron las validaciones mínimas!!!")

        except Exception as e:
            self.p_alerta("Excepción",str(e))
    
    def p_crear_paciente(self):
        try:
            pacientes = Pacientes()           
            datosPaciente = self.p_obtener_datos_front()               
            #Validaciones y acciones
            if validar_identificacion(datosPaciente['identificacion']) and validar_nombres(datosPaciente['nombres']) and validar_apellidos(datosPaciente['apellidos']):
                paciente = pacientes.consultar_paciente(datosPaciente['identificacion'])
                if paciente is None: 
                    pacientes.crear_paciente(datosPaciente)
                    self.p_alerta("Exito","Paciente creado de manera exitosa!!!") 
                    self.p_calcuar_edad(datetime.strptime(datosPaciente['fechaNacimiento'], '%Y-%m-%d'))                 
                else:
                    self.p_alerta("Info","Paciente ya existe!!!")
                    self.p_calcuar_edad(paciente['fechaNacimiento']) 
                    self.p_asignar_datos_front(paciente)

                self.btnActualizar.setEnabled(True)
                self.text_identificacion_2.setText(datosPaciente['identificacion']) 
                self.text_identificacion_3.setText(datosPaciente['identificacion'])                      
                self.p_obtener_foto(datosPaciente['identificacion']) 
            else:
                self.p_alerta("Error","Datos no superaron las validaciones mínimas!!!")
    
        except Exception as e:
            self.p_alerta("Excepción",str(e))
            
    def p_actulizar_paciente(self):
        try:
            pacientes = Pacientes()           
            datosPaciente = self.p_obtener_datos_front()
            #Validaciones y acciones
            if validar_identificacion(datosPaciente['identificacion']) and validar_nombres(datosPaciente['nombres']) and validar_apellidos(datosPaciente['apellidos']):
                paciente = pacientes.consultar_paciente(datosPaciente['identificacion'])
                if paciente is None: 
                    self.p_alerta("Error","Identificacion del Paciente no existe para actualizar!!!")
                else:
                    pacientes.actualizar_paciente(datosPaciente)
                    self.p_alerta("Exito","Paciente actulizado de manera exitosa!!!")
                    self.btnActualizar.setEnabled(False) 
                    self.text_identificacion_2.setText(datosPaciente['identificacion']) 
                    self.text_identificacion_3.setText(datosPaciente['identificacion'])           
                    self.p_calcuar_edad(datetime.strptime(datosPaciente['fechaNacimiento'], '%Y-%m-%d'))  
                    self.p_obtener_foto(datosPaciente['identificacion'])                   
            else:
                self.p_alerta("Error","Datos no superaron las validaciones mínimas!!!")

        except Exception as e:
            self.p_alerta("Excepción",str(e))       

    def p_crear_evento(self):
        try:
            pacientes = Pacientes() 
            eventos = Eventos()           
            identificacion = self.text_identificacion_2.text()           
            #Validaciones y acciones
            if validar_identificacion(identificacion):
                paciente = pacientes.consultar_paciente(identificacion)
                if paciente is None: 
                    self.p_alerta("Error","Paciente no existe!!!")
                else:
                    datosEvento= {'pacienteId': paciente['id'],
                        'estado': self.text_Estado.toPlainText(),
                        'hea': self.text_hea.toPlainText(),
                        'impDiagnostica': self.text_impDiagnostica.toPlainText(),
                        'conductaSeguir': self.text_conductaSeguir.toPlainText(),
                        'motivoConsulta': self.text_motivoConsulta.toPlainText(),
                        'temperatura': self.text_temperatura.text(),
                        'tensionArterial': self.text_tensionArterial.text(),
                        'freCardiaca': self.text_freCardiaca.text(),
                        'freRespiratoria': self.text_freRespiratoria.text(),
                        'oxigenacion': self.text_oxigenacion.text()
                        }
                    eventos.crear_evento(datosEvento)
                    self.p_alerta("Exito","Evento creado de manera exitosa!!!")
            else:
                self.p_alerta("Error","Datos no superaron las validaciones mínimas!!!")

        except Exception as e:
            self.p_alerta("Excepción",str(e))
    
    def p_consultar_historial(self):
        try:
            pacientes = Pacientes()  
            eventos = Eventos() 
            identificacion = self.text_identificacion_3.text()
            self.text_InformacionHistorial.setText('')

            #Validaciones y acciones
            if validar_identificacion(identificacion):
                paciente = pacientes.consultar_paciente(identificacion)
                if paciente is None: 
                    self.p_alerta("Info","Paciente no existe!!!")
                else:
                    historial = eventos.consultar_historial(paciente['id'])
                    if historial is None or historial == []:
                        self.p_alerta("Info","Paciente no posee historial de eventos realizados!!!")
                    else:    
                        salidaEvento = ''
                        for historia in historial:
                            created_at_evento = f"<b>Fecha del evento:</b> {historia['created_at']}"
                            estado = f"<b>Estado:</b> {historia['estado']}"
                            hea = f"<b>H.E.A:</b> {historia['hea']}"
                            impDiagnostica = f"<b>Impresión Diagnóstica:</b> {historia['impDiagnostica']}"
                            conductaSeguir = f"<b>Conducta a Seguir:</b> {historia['conductaSeguir']}"
                            temperatura = f"<b>Temperatura:</b> {historia['temperatura']}"
                            tensionArterial = f"<b>Tensión Arterial:</b> {historia['tensionArterial']}"
                            freCardiaca = f"<b>Frecuencia Cardiaca:</b> {historia['freCardiaca']}"
                            freRespiratoria = f"<b>Frecuencia Respiratoria:</b> {historia['freRespiratoria']}"
                            oxigenacion = f"<b>Oxigenación:</b> {historia['oxigenacion']}"
                            motivoConsulta = f"<b>Motivo de Consulta:</b> {historia['motivoConsulta']}"
                            separadorEvento = '<b>----------------------------------------------------------------------------------------------------------------------------------------------------------------</b>'
                            salidaEvento += '<html>'+created_at_evento+'<br>'+estado+'<br>'+hea+'<br>'+impDiagnostica+'<br>'+conductaSeguir+'<br>'+temperatura+'<br>'+tensionArterial+'<br>'+freCardiaca+'<br>'+freRespiratoria+'<br>'+oxigenacion+'<br>'+motivoConsulta+'<br>'+separadorEvento+'<br>'+'</html>'
                        self.text_InformacionHistorial.setText(salidaEvento)                             
            else:
                self.p_alerta("Error","Datos no superaron las validaciones mínimas!!!")

        except Exception as e:
            self.p_alerta("Excepción",str(e))

    def p_descargar_Historial(self):
        try:
            pacientes = Pacientes()  
            eventos = Eventos() 
            identificacion = self.text_identificacion_3.text()
            self.text_InformacionHistorial.setText('')

            #Validaciones y acciones
            if validar_identificacion(identificacion):
                paciente = pacientes.consultar_paciente(identificacion)
                if paciente is None: 
                    self.p_alerta("Info","Paciente no existe!!!")
                else:
                    historial = eventos.consultar_historial(paciente['id'])
                    if historial is None or historial == []:
                        self.p_alerta("Info","Paciente no posee historial de eventos realizados!!!")
                    else:   
                        PdfHistoriaClinica(paciente,historial)    
                        self.p_alerta("Exito","Historial de eventos generado de manera exitosa!!!")                       
            else:
                self.p_alerta("Error","Datos no superaron las validaciones mínimas!!!")

        except Exception as e:
           self.p_alerta("Excepción",str(e))                     

    def p_consultar_soportes(self):
        try:
            pacientes = Pacientes()  
            identificacion = self.text_identificacion_3.text()
            self.text_InformacionHistorial.setText('')
            #Validaciones y acciones
            if validar_identificacion(identificacion):
                paciente = pacientes.consultar_paciente(identificacion)
                if paciente is None:
                    self.p_alerta("Info","Paciente no existe!!!")
                else:
                    path_base = self.datosAppConfig['PathBase']
                    path_Soportes = f"Recursos/Soportes/Historias/{str(paciente['identificacion'])}"
                    os.makedirs(path_Soportes,exist_ok=True)
                    
                    file_path = ''
                    file_dialog = QFileDialog()
                    file_dialog.setFileMode(QFileDialog.ExistingFile)
                    file_dialog.setDirectory(f"{path_base}/{path_Soportes}/") 
                    file_dialog.exec_()
                    file_paths = file_dialog.selectedFiles()
                    if len(file_paths)>0:
                        file_path = file_paths[0]

                    if file_path == '':
                        pass
                    else:             
                        webbrowser.open_new(file_path)    
            else:
                self.p_alerta("Error","Datos no superaron las validaciones mínimas!!!")

        except Exception as e:
           self.p_alerta("Excepción",str(e))                

    def p_subir_soportes(self):
        try:
            pacientes = Pacientes()  
            identificacion = self.text_identificacion_3.text()
            self.text_InformacionHistorial.setText('')
            #Validaciones y acciones
            if validar_identificacion(identificacion):
                paciente = pacientes.consultar_paciente(identificacion)
                if paciente is None:
                    self.p_alerta("Info","Paciente no existe!!!")
                else:
                    path_base = self.datosAppConfig['PathBase']
                    path_Soportes = f"Recursos/Soportes/Historias/{str(paciente['identificacion'])}"
                    os.makedirs(path_Soportes,exist_ok=True)

                    file_path = '' 
                    file_dialog = QFileDialog()
                    file_dialog.setFileMode(QFileDialog.ExistingFile)
                    file_dialog.setDirectory(f"{path_base}") 
                    file_dialog.exec_()
                    file_paths = file_dialog.selectedFiles()
                    if len(file_paths)>0:
                        file_path = file_paths[0]

                    if file_path == '':
                        pass
                    else:             
                        shutil.copy(file_path, path_Soportes)   
                        self.p_alerta("Exito","Soporte/Archivo almacenado correctamente!!!")  
            else:
                self.p_alerta("Error","Datos no superaron las validaciones mínimas!!!")

        except Exception as e:
           self.p_alerta("Excepción",str(e))                
    
    def p_obtener_datos_front(self):
        datosPaciente= {'identificacion': self.text_identificacion.text(),
                        'nombres': self.text_nombres.text(),
                        'apellidos': self.text_apellidos.text(),
                        'direccion': self.text_direccion.text(),
                        'correo': self.text_email.text(),
                        'telefono': self.text_telefono.text(),
                        'fechaNacimiento': self.date_FechaNacimiento.text(),
                        'peso': self.text_peso.text(),
                        'talla': self.text_talla.text(),
                        'habitosToxicos': self.text_habitos.toPlainText(),
                        'alergiaMedicamentos': self.text_alergias.toPlainText(),
                        'vacunacion': self.text_vacunacion.toPlainText(),
                        'app': self.text_app.toPlainText(),
                        'apf': self.text_apf.toPlainText(),
                        'nombreAcompanante': self.text_acompanante.text()
                        }
        if self.radiobutton_sexo.isChecked():
            datosPaciente['sexo'] = 'M'
        elif self.radiobutton_sexo_2.isChecked():
            datosPaciente['sexo'] = 'F'
        else:
            datosPaciente['sexo'] = '' 

        if self.radiobutton_transfusiones.isChecked():
            datosPaciente['transfusiones'] = 'SI'
        elif self.radiobutton_transfusiones_2.isChecked():
            datosPaciente['transfusiones'] = 'NO'
        else:
            datosPaciente['transfusiones'] = 'NO'     

        return datosPaciente
    
    def p_asignar_datos_front(self, paciente):
        self.text_identificacion.setText(paciente['identificacion'])
        self.text_nombres.setText(paciente['nombres'])
        self.text_apellidos.setText(paciente['apellidos'])
        self.text_direccion.setText(paciente['direccion'])
        self.text_email.setText(paciente['correo'])
        self.text_telefono.setText(paciente['telefono'])
        if isinstance(paciente['fechaNacimiento'], str):
            self.date_FechaNacimiento.setDate(datetime.strptime(paciente['fechaNacimiento'], '%Y-%m-%d'))
        else:
            self.date_FechaNacimiento.setDate(paciente['fechaNacimiento'])    
        self.text_peso.setText(paciente['peso'])
        self.text_talla.setText(paciente['talla'])
        self.text_habitos.setText(paciente['habitosToxicos'])
        self.text_alergias.setText(paciente['alergiaMedicamentos'])
        self.text_vacunacion.setText(paciente['vacunacion'])
        self.text_app.setText(paciente['app'])
        self.text_apf.setText(paciente['apf'])
        self.text_acompanante.setText(paciente['nombreAcompanante'])
        self.label_historia.setText("N° Historia: "+str(paciente['id']))  

        if paciente['sexo'] == 'M':
            self.radiobutton_sexo.setChecked(True)
        elif paciente['sexo'] == 'F':
            self.radiobutton_sexo_2.setChecked(True)
        else:
            self.radiobutton_sexo.setChecked(False)
            self.radiobutton_sexo_2.setChecked(False)
        if paciente['transfusiones'] == 'SI':
            self.radiobutton_transfusiones.setChecked(True)
        elif paciente['transfusiones'] == 'NO':
            self.radiobutton_transfusiones_2.setChecked(True)
        else:
            self.radiobutton_transfusiones.setChecked(False)
            self.radiobutton_transfusiones_2.setChecked(False)   

    def p_alerta(self,titulo,mensaje):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(titulo)
        dlg.setText(mensaje)
        dlg.exec()
        #if button == QMessageBox.StandardButton.Ok:
        #    print("OK!")

    def p_calcuar_edad(self,fecha_nacimiento):
        if isinstance(fecha_nacimiento, str):
            edad = relativedelta(datetime.now(), datetime.strptime(fecha_nacimiento, '%Y-%m-%d'))          
        else:
            edad = relativedelta(datetime.now(), fecha_nacimiento)
        self.label_edad.setText(f"{edad.years} años")
        if edad.years == 0 or edad.years == None:
            self.label_edad.setText(f"{edad.months} meses")
            if edad.months == 0 or edad.months == None:
                self.label_edad.setText(f"{edad.days} días")    

    def p_obtener_foto(self,identificacion):
        try:
            os.makedirs(f"Recursos/Soportes/Foto/",exist_ok=True)
            rutaFoto = f"Recursos/Soportes/Foto/{identificacion}"
            self.foto.setPixmap(QPixmap(rutaFoto))
        except:
            self.foto.setPixmap(QPixmap(None))
            pass        

    def p_cargar_foto(self):
        try:
            identificacion = self.text_identificacion.text()
            if identificacion == '':
                self.p_alerta("Error","Debe indicar una identificación!!!")           
            if validar_identificacion(identificacion):
                pacientes = Pacientes()  
                paciente = pacientes.consultar_paciente(identificacion)
                if paciente is None: 
                    self.p_alerta("Error","Paciente no existe!!!")
                else:
                    path_base = self.datosAppConfig['PathBase']
                    os.makedirs(f"Recursos/Soportes/Foto/",exist_ok=True)
                    rutaFoto = f"Recursos/Soportes/Foto/{identificacion}"

                    file_path = '' 
                    file_dialog = QFileDialog()
                    file_dialog.setFileMode(QFileDialog.ExistingFile)
                    file_dialog.setDirectory(f"{path_base}") 
                    file_dialog.exec_()
                    file_paths = file_dialog.selectedFiles()
                    if len(file_paths)>0:
                        file_path = file_paths[0]

                    if file_path == '':
                        pass
                    else:
                        shutil.copy(file_path, rutaFoto)
                        self.foto.setPixmap(QPixmap(rutaFoto))               
        except:
            self.foto.setPixmap(QPixmap(None))
            pass     

    def p_limpiar_front(self):
        self.text_identificacion.setText('')
        self.text_nombres.setText('')
        self.text_apellidos.setText('')
        self.text_direccion.setText('')
        self.text_email.setText('')
        self.text_telefono.setText('')          
        self.date_FechaNacimiento.setDate(datetime.strptime('1900-01-01', '%Y-%m-%d'))
        self.text_peso.setText('')     
        self.text_talla.setText('')     
        self.text_habitos.setText('')     
        self.text_alergias.setText('')     
        self.text_vacunacion.setText('')  
        self.text_app.setText('') 
        self.text_apf.setText('') 
        self.text_acompanante.setText('')           
        self.label_edad.setText('')  
        self.label_historia.setText('')  
        self.btnActualizar.setEnabled(False)
        self.foto.setPixmap(QPixmap(None))   
        self.text_identificacion_2.setText('')
        self.text_identificacion_3.setText('')   
        self.text_Estado.setText('')
        self.text_hea.setText('')
        self.text_impDiagnostica.setText('')
        self.text_conductaSeguir.setText('')
        self.text_motivoConsulta.setText('')
        self.text_temperatura.setText('')
        self.text_tensionArterial.setText('')
        self.text_freCardiaca.setText('')
        self.text_freRespiratoria.setText('')
        self.text_oxigenacion.setText('')
        self.text_InformacionHistorial.setText('')

    def p_limpiar_front_eventos(self):
        self.text_Estado.setText('')
        self.text_hea.setText('')
        self.text_impDiagnostica.setText('')
        self.text_conductaSeguir.setText('')
        self.text_motivoConsulta.setText('')
        self.text_temperatura.setText('')
        self.text_tensionArterial.setText('')
        self.text_freCardiaca.setText('')
        self.text_freRespiratoria.setText('')
        self.text_oxigenacion.setText('')

    def p_limpiar_front_historial(self):
        self.text_InformacionHistorial.setText('') 


        
