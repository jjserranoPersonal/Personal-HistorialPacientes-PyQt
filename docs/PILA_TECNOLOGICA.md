# Pila Tecnológica

## Lenguajes de Programación

- **Python**: 3.x (no especificado, pero compatible con PyQt5)

## Frameworks y Librerías

### Interfaz Gráfica
- **PyQt5**: 5.15.9 - Framework principal para UI
- **PyQt5-Qt5**: 5.15.2 - Backend Qt
- **PyQt5-sip**: 12.12.1 - Binding entre Python y Qt

### Base de Datos
- **mysql-connector-python**: 8.0.32 - Conector MySQL
- **sqlite3**: Módulo estándar de Python para SQLite

### Generación de PDFs
- **reportlab**: 3.6.12 - Librería para crear PDFs

### Utilidades
- **Pillow**: 9.4.0 - Procesamiento de imágenes
- **python-dateutil**: 2.8.2 - Manipulación de fechas
- **six**: 1.16.0 - Compatibilidad Python 2/3
- **protobuf**: 3.20.3 - Serialización (dependencia de mysql-connector)
- **altgraph**: 0.17.3 - Análisis de dependencias (para PyInstaller)
- **pefile**: 2023.2.7 - Análisis de archivos PE (para PyInstaller)
- **pyinstaller-hooks-contrib**: 2023.3 - Hooks para PyInstaller
- **pywin32-ctypes**: 0.2.0 - Interfaces Windows

## Herramientas de Desarrollo

- **Qt Designer**: Para diseño de interfaces UI (.ui files)
- **PyInstaller**: Para empaquetado de aplicaciones (implicado por hooks-contrib)

## Sistema de Base de Datos

- **MySQL**: Versiones compatibles con mysql-connector-python 8.0.32
- **SQLite**: 3.x (incluido en Python)

## Infraestructura de Despliegue

- **Aplicación de Escritorio**: Ejecutable standalone
- **Empaquetado**: PyInstaller para distribución

## Sistema Operativo

- **Windows**: Principal (pywin32-ctypes indica soporte Windows)
- **Potencialmente multiplataforma**: PyQt5 soporta Windows, macOS, Linux
