# Módulos

## database/db.py

### Propósito
Maneja la conexión a la base de datos, soportando MySQL y SQLite.

### Funciones
- `get_db()`: Establece conexión según configuración en AppConfig.json
- `dict_factory()`: Convierte resultados SQLite a diccionarios

### Dependencias
- mysql.connector
- sqlite3
- json

### Lógica Condicional
- Si tipoDB == "mysql": conectar MySQL
- Si tipoDB == "sqlite": conectar SQLite

## database/Pacientes.py

### Propósito
Operaciones CRUD para la tabla paciente.

### Métodos
- `crear_paciente(datosPaciente)`: Inserta nuevo paciente
- `consultar_paciente(identificacion)`: Busca paciente por ID
- `actualizar_paciente(datosPaciente)`: Actualiza datos del paciente
- `consultar_listado_pacientes(nombre)`: Lista pacientes por nombre (LIKE)

### Lógica de Negocio
- Crear: Verificar no existe antes de insertar
- Actualizar: Requiere paciente existente
- Consultar: Retorna dict si existe, None si no

### Lógica Condicional
- En crear: Si paciente existe, mostrar mensaje
- En actualizar: Si no existe, error

## database/Eventos.py

### Propósito
Gestión de eventos médicos (historial).

### Métodos
- `crear_evento(datosEvento)`: Registra nuevo evento
- `consultar_historial(paciente)`: Obtiene historial ordenado por fecha

### Lógica de Negocio
- Eventos ligados a paciente por pacienteId
- Historial ordenado por created_at DESC

### Lógica Condicional
- Consultar: Si no hay historial, lista vacía

## MainWindow_Login.py

### Propósito
Ventana de autenticación.

### Funcionalidades
- Formulario login: usuario, password
- Validación básica
- Transición a ventana principal si ok

### Lógica Condicional
- Si validaciones pasan: consultar usuario
- Si usuario existe y password coincide: abrir principal
- Else: mensaje error

### Interacciones
- Carga UI desde Recursos/UI/Login.ui
- Conecta botón a login_iniciar()

## MainWindow_Principal.py

### Propósito
Ventana principal con todas las operaciones del sistema.

### Funcionalidades Principales
- Gestión de Pacientes (CRUD)
- Registro de Eventos Médicos
- Consulta de Historial
- Gestión de Soportes y Fotos
- Generación de Reportes PDF
- Consulta de Listado de Pacientes

### Lógica de Negocio
- Validaciones en cada operación usando validaciones.py
- Cálculo de edad usando dateutil
- Gestión de archivos en directorios específicos por paciente
- Limpieza de formularios
- Alertas con QMessageBox

### Lógica Condicional
- Para cada operación: validar inputs, verificar existencia, ejecutar acción, mostrar resultado
- En consultas: si no existe, mensaje info
- En creaciones: si ya existe, mostrar datos existentes

### Interdependencias
- Usa Pacientes y Eventos classes
- Llama PDF_Historia_Clinica para reportes
- Gestiona archivos con shutil y os

## validaciones.py

### Propósito
Funciones de validación básicas para inputs.

### Funciones
- `validar_usuario(usuario: str) -> bool`: Longitud entre 1-50
- `validar_password(password: str) -> bool`: Longitud entre 1-50
- `validar_identificacion(identificacion: str) -> bool`: Numérico, longitud <=50
- `validar_nombres(nombres: str) -> bool`: Longitud entre 1-100
- `validar_apellidos(apellidos: str) -> bool`: Longitud entre 1-100

### Lógica de Negocio
- Validaciones simples para UX
- Previenen inputs vacíos o demasiado largos

## PDF_Historia_Clinica.py

### Propósito
Genera reportes PDF del historial clínico usando ReportLab.

### Funcionalidades
- Crea PDF con datos del paciente
- Lista eventos médicos formateados
- Guarda archivo en directorio del paciente

### Lógica de Negocio
- Usa canvas de ReportLab
- Dibuja texto y tablas
- Formatea fechas y datos médicos

### Dependencias
- reportlab
