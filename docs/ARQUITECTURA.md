# Arquitectura del Sistema

## Visión General

El sistema Historial Pacientes PyQt es una aplicación de escritorio desarrollada siguiendo una arquitectura de capas simple, con separación clara entre la interfaz de usuario, la lógica de negocio y el acceso a datos.

## Componentes Principales

### 1. Interfaz de Usuario (UI Layer)
- **MainWindow_Login.py**: Maneja la autenticación de usuarios
- **MainWindow_Principal.py**: Ventana principal con todas las funcionalidades
- Archivos UI diseñados en Qt Designer (.ui)

### 2. Lógica de Negocio (Business Logic Layer)
- **validaciones.py**: Funciones de validación de datos
- **PDF_Historia_Clinica.py**: Generación de reportes PDF

### 3. Acceso a Datos (Data Access Layer)
- **database/db.py**: Conexión a base de datos (MySQL/SQLite)
- **database/Pacientes.py**: Operaciones CRUD para pacientes
- **database/Eventos.py**: Gestión de historial médico

### 4. Recursos y Configuración
- **Recursos/Config/AppConfig.json**: Configuración de la aplicación
- **Recursos/UI/**: Archivos de interfaz
- **Recursos/img/**: Imágenes y recursos estáticos

## Arquitectura de Datos

### Base de Datos
- Soporte para MySQL y SQLite
- Esquema relacional simple con 3 tablas principales
- Relación paciente -> historial (1:N)

### Almacenamiento de Archivos
- Fotografías de pacientes: Recursos/Soportes/Foto/
- Soportes médicos: Recursos/Soportes/Historias/

## Flujo de la Aplicación

1. Inicio: MainWindow_Login.py autentica usuario
2. Principal: MainWindow_Principal.py carga interfaz completa
3. Operaciones: Usuario interactúa con formularios
4. Validación: validaciones.py verifica datos
5. Persistencia: database/ guarda en BD
6. Reportes: PDF_Historia_Clinica.py genera PDFs

## Decisiones de Diseño

- **Arquitectura Simple**: Sin frameworks complejos para mantener simplicidad
- **Acceso Directo a BD**: SQL directo sin ORM para control total
- **UI Declarativa**: Qt Designer para separación de lógica y presentación
- **Multi-BD**: Soporte para MySQL y SQLite para flexibilidad
- **Validaciones Básicas**: Enfoque en UX con validaciones client-side

## Limitaciones Arquitecturales

- No hay separación de responsabilidades estricta (MVC parcial)
- SQL injection potencial (uso de f-strings en queries)
- No hay manejo de transacciones complejas
- UI hardcoded sin internacionalización

## Escalabilidad

La arquitectura actual es adecuada para uso individual/departamental. Para escalar:

- Implementar ORM (SQLAlchemy)
- Separar en microservicios
- Agregar API REST
- Implementar autenticación robusta (JWT, roles)
