import sys
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
from dateutil.relativedelta import relativedelta
import textwrap

class PdfHistoriaClinica:

    def __init__(self,paciente,historial):
        #Tips Generales para PDF
		#text.setFillColorRGB(0.2,0,0.6)
		#TiposLetras->Courier,Times-Roman,helvetica
		#DimensionesCarta->(X:612.0, Y:792.0)
        path_historia = 'Recursos/Soportes/Historias/'+str(paciente['identificacion'])+'/'
        os.makedirs(path_historia,exist_ok=True)
        c = canvas.Canvas(path_historia+'Historia_Clinica.pdf', pagesize=letter)
        tipoLetra = "Times-Roman"
        fuenteLetra = 12

        for historia in historial:
            #Rectangulo general
            c.roundRect(20, 20, 575, 755, 10)

            #Logo
            paht_logo = "Recursos/img/"		
            c.drawImage(paht_logo+"logo.png", 30, 620, width=350, height=150)

            #Numero de Historia
            texto = f"N° de Historia: {str(paciente['id'])}"
            self.texto_una_linea(420,720,tipoLetra,fuenteLetra,texto,c)
   
            #Fecha del evento
            texto = f"Fecha/Hora: {str(historia['created_at'])}"
            self.texto_una_linea(420,700,tipoLetra,fuenteLetra,texto,c)

            #Titulo
            texto = "HISTORIA CLINICA INDIVIDUAL"
            text = c.beginText(170, 600)
            text.setFont(tipoLetra, 20)
            text.setFillColorRGB(0.14, 0.59, 0.74) 
            text.textLines(texto)
            c.drawText(text)

            #Nombres y apellidos
            texto = f"Apellidos/Nombres: {str(paciente['apellidos'])} {str(paciente['nombres'])}"
            self.texto_una_linea(25,580,tipoLetra,fuenteLetra,texto,c)

            #Edad
            texto = f"Edad: {self.calcuar_edad(paciente['fechaNacimiento'])}"
            self.texto_una_linea(25,560,tipoLetra,fuenteLetra,texto,c)

            #Sexo
            texto = f"Sexo: {str(paciente['sexo'])}"
            self.texto_una_linea(175,560,tipoLetra,fuenteLetra,texto,c)

            #Fecha de nacimiento
            texto = f"F/N: {str(paciente['fechaNacimiento'])}"
            self.texto_una_linea(325,560,tipoLetra,fuenteLetra,texto,c)

            #Identificacion
            texto = f"C.I: {str(paciente['identificacion'])}"
            self.texto_una_linea(475,560,tipoLetra,fuenteLetra,texto,c)

            #Dirección
            texto = f"Dirección: {str(paciente['direccion'])}"
            self.texto_una_linea(25,540,tipoLetra,fuenteLetra,texto,c)

            #Telefono
            texto = f"Telefono: {str(paciente['telefono'])}"
            self.texto_una_linea(25,520,tipoLetra,fuenteLetra,texto,c)

            #Correo
            texto = f"Correo: {str(paciente['correo'])}"
            self.texto_una_linea(175,520,tipoLetra,fuenteLetra,texto,c)

            #A.P.P
            texto = f"A.P.P: {str(paciente['app'])}"
            self.texto_una_linea(25,500,tipoLetra,fuenteLetra,texto,c)

            #A.P.F
            texto = f"A.P.F: {str(paciente['apf'])}"
            self.texto_una_linea(25,480,tipoLetra,fuenteLetra,texto,c)

            #Habitos
            texto = f"Hábitos Tóxicos: {str(paciente['habitosToxicos'])}"
            self.texto_una_linea(25,460,tipoLetra,fuenteLetra,texto,c)

            #Alergias a medicamentos
            texto = f"Alergia a Medicamentos: {str(paciente['alergiaMedicamentos'])}"
            self.texto_una_linea(25,440,tipoLetra,fuenteLetra,texto,c)

            #Transfusiones
            texto = f"Transfusiones de Sangre: {str(paciente['transfusiones'])}"
            self.texto_una_linea(25,420,tipoLetra,fuenteLetra,texto,c)

            #Vacunación
            texto = f"Vacunación: {str(paciente['vacunacion'])}"
            self.texto_una_linea(25,400,tipoLetra,fuenteLetra,texto,c)

            #Oxigenación
            texto = f"O.X.M (SpO2): {str(historia['oxigenacion'])}"
            self.texto_una_linea(25,380,tipoLetra,fuenteLetra,texto,c)

            #Temperatura
            texto = f"Temp: {str(historia['temperatura'])}"
            self.texto_una_linea(25,360,tipoLetra,fuenteLetra,texto,c)

            #Peso
            texto = f"Peso: {str(paciente['peso'])}"
            self.texto_una_linea(125,360,tipoLetra,fuenteLetra,texto,c)

            #Talla
            texto = f"Talla: {str(paciente['talla'])}"
            self.texto_una_linea(225,360,tipoLetra,fuenteLetra,texto,c)

            #T.A
            texto = f"T.A: {str(historia['tensionArterial'])}"
            self.texto_una_linea(325,360,tipoLetra,fuenteLetra,texto,c)

            #F.C
            texto = f"F.C: {str(historia['freCardiaca'])}"
            self.texto_una_linea(425,360,tipoLetra,fuenteLetra,texto,c)

            #F.R
            texto = f"F.R: {str(historia['freRespiratoria'])}"
            self.texto_una_linea(525,360,tipoLetra,fuenteLetra,texto,c)

            #Estado del paciente
            estado =  self.truncar(94,str(historia['estado']))    
            estadof = ''
            for estf in estado:	
                estadof += estf+"\n"      
            texto = f"Estado: \n{estadof}"
            self.texto_una_linea(25,340,tipoLetra,fuenteLetra,texto,c)

            #Motivo de consulta
            motivoConsulta =  self.truncar(94,str(historia['motivoConsulta']))    
            motivoConsultaf = ''
            for mc in motivoConsulta:	
                motivoConsultaf += mc+"\n"      
            texto = f"M.C: \n{motivoConsultaf}"
            self.texto_una_linea(25,280,tipoLetra,fuenteLetra,texto,c)

            #H.E.A
            historiaEnfermendad =  self.truncar(94,str(historia['hea']))    
            historiaEnfermendadf = ''
            for hea in historiaEnfermendad:	
                historiaEnfermendadf += hea+"\n"      
            texto = f"H.E.A: \n{historiaEnfermendadf}"
            self.texto_una_linea(25,220,tipoLetra,fuenteLetra,texto,c)

            #I.D.X
            impresionDiag =  self.truncar(94,str(historia['impDiagnostica']))    
            impresionDiagf = ''
            for idx in impresionDiag:	
                impresionDiagf += idx+"\n"      
            texto = f"I.D.X: \n{impresionDiagf}"
            self.texto_una_linea(25,160,tipoLetra,fuenteLetra,texto,c)

            #C.D.S
            conductaSeguir =  self.truncar(94,str(historia['conductaSeguir']))    
            conductaSeguirf = ''
            for cds in conductaSeguir:	
                conductaSeguirf += cds+"\n"      
            texto = f"C.D.S: \n{conductaSeguirf}"
            self.texto_una_linea(25,100,tipoLetra,fuenteLetra,texto,c)

            #Firma del mecdico
            texto = f"Firma del Médico:"
            self.texto_una_linea(360,30,tipoLetra,fuenteLetra,texto,c)

            c.showPage()

        c.save()

    def texto_una_linea(self,x,y,tipoLetra,fuenteLetra,texto,c):
        text = c.beginText(x, y)
        text.setFont(tipoLetra, fuenteLetra)
        text.setFillColorRGB(0, 0, 0) 
        text.textLines(texto)
        c.drawText(text)
        
    def calcuar_edad(self,fecha_nacimiento):
        if isinstance(fecha_nacimiento, str):
            calculo_edad = relativedelta(datetime.now(), datetime.strptime(fecha_nacimiento, '%Y-%m-%d'))          
        else:
            calculo_edad = relativedelta(datetime.now(), fecha_nacimiento)
        edad = f"{calculo_edad.years} años"
        if calculo_edad.years == 0 or calculo_edad.years==None:
            edad = f"{calculo_edad.months} meses"
            if calculo_edad.months == 0 or calculo_edad.months == None:
                edad = f"{calculo_edad.days} días"    
        return edad    

    def truncar(self,cantidad,cadena):	
        cadena = textwrap.wrap(cadena, width=cantidad)			
        return cadena


