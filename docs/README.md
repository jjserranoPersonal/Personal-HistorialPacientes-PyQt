# Historial Pacientes PyQt

## Descripción General

Sistema de gestión de historiales clínicos de pacientes desarrollado en Python con interfaz gráfica PyQt5. Permite administrar información de pacientes, registrar eventos médicos y generar reportes en PDF.

## Propósito

Facilitar la gestión de información médica de pacientes en entornos clínicos, permitiendo a los profesionales de la salud mantener registros completos de antecedentes, tratamientos y evoluciones.

## Funcionalidades Principales

- Gestión de pacientes (CRUD)
- Registro de eventos médicos
- Consulta de historial clínico
- Generación de reportes PDF
- Gestión de soportes y fotografías
- Sistema de autenticación

## Inicio Rápido

### Prerrequisitos

- Python 3.x
- PyQt5
- MySQL o SQLite
- Dependencias listadas en requirements.txt

### Instalación

1. Clonar el repositorio
2. Instalar dependencias: `pip install -r requirements.txt`
3. Configurar base de datos en Recursos/Config/AppConfig.json
4. Ejecutar: `python MainWindow_Login.py`

### Configuración

Editar Recursos/Config/AppConfig.json para configurar la base de datos.

## Arquitectura del Sistema

- **Frontend**: PyQt5 con archivos UI diseñados en Qt Designer
- **Backend**: Python puro con acceso directo a base de datos
- **Base de Datos**: Soporte para MySQL y SQLite
- **Reportes**: Generación de PDFs con ReportLab

## Estructura del Proyecto

- `MainWindow_Login.py`: Ventana de autenticación
- `MainWindow_Principal.py`: Ventana principal con todas las funcionalidades
- `database/`: Módulos de acceso a datos
- `Recursos/`: Archivos estáticos (UI, imágenes, configuración)
- `validaciones.py`: Funciones de validación
- `PDF_Historia_Clinica.py`: Generador de reportes PDF

## Contribución

Para contribuir al proyecto:

1. Crear rama feature desde main
2. Implementar cambios
3. Crear PR con descripción detallada siguiendo el template

## Licencia

[Especificar licencia si aplica]
