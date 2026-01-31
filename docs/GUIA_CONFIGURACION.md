# Guía de Configuración

## Entorno de Desarrollo

### Prerrequisitos

- Python 3.8 o superior
- Git (opcional, para control de versiones)
- MySQL o SQLite

### Instalación de Python

1. Descargar Python desde python.org
2. Instalar con opción "Add to PATH"
3. Verificar: `python --version`

### Clonación del Proyecto

```bash
git clone <url_del_repositorio>
cd Personal-HistorialPacientes-PyQt
```

### Instalación de Dependencias

```bash
pip install -r requirements.txt
```

### Configuración de Base de Datos

#### Opción SQLite (Recomendado para desarrollo)

1. El proyecto incluye script inicial: database/Scripts/Inicial_000/SQLite_Script_DB_Historial_Pacientes.sql
2. Configurado por defecto en Recursos/Config/AppConfig.json:
   - "tipoDB": "sqlite"
   - "DatabaseSQLite": "Recursos/database/historial_pacientes.sqlite3"

#### Opción MySQL

1. Instalar MySQL Server
2. Crear base de datos: `CREATE DATABASE historial_pacientes;`
3. Crear usuario: `CREATE USER 'usuario'@'localhost' IDENTIFIED BY 'password';`
4. Dar permisos: `GRANT ALL PRIVILEGES ON historial_pacientes.* TO 'usuario'@'localhost';`
5. Ejecutar script: database/Scripts/Inicial_000/MySQL_Script_DB_Historial_Pacientes.sql
6. Modificar AppConfig.json:
   - "tipoDB": "mysql"
   - "Db.Host": "localhost"
   - "Db.User": "usuario"
   - "Db.Password": "password"
   - "Db.Database": "historial_pacientes"

### Configuración de Directorios

Los directorios se crean automáticamente:

- Recursos/Soportes/Foto/
- Recursos/Soportes/Historias/

### Ejecución

```bash
python MainWindow_Login.py
```

### Usuario por Defecto

- Usuario: jserrano
- Password: 123456

### Verificación

1. Ejecutar aplicación
2. Login con credenciales por defecto
3. Crear un paciente de prueba
4. Registrar un evento
5. Generar PDF
