import sys
import os
from PyQt6.QtWidgets  import QApplication, QWidget, QMainWindow, QMessageBox
from PyQt6 import uic
from db import get_db
from validaciones import *
from MainWindow_Principal import Principal

class Login(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi("Recursos/UI/Login.ui", self)       
        self.mostarPrincipal = None
        self.btnIniciar.clicked.connect(self.login_iniciar)       

    def login_iniciar(self):
        try:
            self.db,self.cursor = get_db() 
            usuario = self.text_usuario.text()
            password = self.text_password.text()           
            #Validaciones y acciones
            if validar_usuario(usuario) and validar_password(password):
                sql = '''select * from usuarios where usuario=%s'''
                values = (usuario,)
                self.cursor.execute (sql,values) 
                usuarioExiste = self.cursor.fetchone() 
                if usuarioExiste is None:
                        self.p_alerta("Error","Usuario ó Contraseña Invalidos!!!") 
                else:
                    if password != usuarioExiste['password']:
                        self.p_alerta("Error","Usuario ó Contraseña Invalidos!!!") 
                    else:
                        if self.mostarPrincipal is None:
                            self.mostarPrincipal = Principal(usuarioExiste['usuario'])
                            self.mostarPrincipal.show()
                            login.close()
            else:
                self.p_alerta("Error","Usuario ó Contraseña no tienen el formarto correcto!!!")

        except Exception as e:
            self.p_alerta("Excepción",str(e))

    def p_alerta(self,titulo,mensaje):
        dlg = QMessageBox(self)
        dlg.setWindowTitle(titulo)
        dlg.setText(mensaje)
        button = dlg.exec()
        #if button == QMessageBox.StandardButton.Ok:
        #    print("OK!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    login = Login()
    login.show()
    app.exec()