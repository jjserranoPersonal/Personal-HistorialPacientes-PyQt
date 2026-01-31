# Pantallas

## Pantalla de Login

### Nombre y Ruta
- **Nombre**: Login
- **Archivo UI**: Recursos/UI/Login.ui
- **Clase**: MainWindow_Login.py

### Propósito
Autenticar usuarios para acceder al sistema.

### Roles con Acceso
Todos los usuarios registrados.

### Elementos de UI
- Campo de texto: usuario
- Campo de texto: password (tipo password)
- Botón: Iniciar

### Campos y Controles
- **usuario**: Text input, obligatorio
- **password**: Password input, obligatorio

### Acciones Disponibles
- Iniciar: Valida credenciales y abre ventana principal

### Flujo de Interacción
1. Usuario ingresa usuario y password
2. Click "Iniciar"
3. Si válido: abre MainWindow_Principal
4. Si inválido: mensaje "Usuario ó Contraseña Invalidos!!!"

### Validaciones Cliente
- Usuario: longitud 1-50 caracteres
- Password: longitud 1-50 caracteres

### Llamadas al Backend
- Consulta tabla usuarios: SELECT * FROM usuarios WHERE usuario='{usuario}'

### Condicionales de UI
- No hay elementos condicionales

### Mensajes y Notificaciones
- Error: "Usuario ó Contraseña Invalidos!!!"
- Error: "Usuario ó Contraseña no tienen el formarto correcto!!!"

## Pantalla Principal - Tab Pacientes

### Nombre y Ruta
- **Nombre**: Gestión de Pacientes
- **Tab**: Pacientes en MainWindow_Principal.py

### Propósito
Administrar información básica de pacientes (CRUD).

### Roles con Acceso
Todos los usuarios autenticados.

### Elementos de UI
- Campos de texto: text_identificacion, text_nombres, text_apellidos, text_direccion, text_email, text_telefono, text_peso, text_talla, text_acompanante
- Date picker: date_FechaNacimiento
- Radio buttons: radiobutton_sexo (M/F), radiobutton_transfusiones (SI/NO)
- Text areas: text_habitos, text_alergias, text_vacunacion, text_app, text_apf
- Labels: label_edad, label_historia
- QLabel: foto (para mostrar imagen)
- Botones: btnConsultarDatos, btnCrear, btnActualizar, btnCargarFoto, btnLimpiar

### Campos Obligatorios
- text_identificacion, text_nombres, text_apellidos

### Campos Opcionales
- Todos los demás

### Valores por Defecto
- date_FechaNacimiento: 1900-01-01
- Radio buttons: no seleccionado inicialmente

### Reglas de Negocio Aplicadas
- Identificación debe ser única
- Sexo: M o F
- Transfusiones: SI o NO

### Acciones Disponibles
- **Consultar Datos**: Busca paciente por ID, llena formulario, calcula edad, muestra foto
- **Crear**: Valida y crea nuevo paciente
- **Actualizar**: Valida y actualiza paciente existente
- **Cargar Foto**: Selecciona archivo imagen y lo asigna al paciente
- **Limpiar**: Resetea todos los campos

### Flujo de Interacción
1. Ingresar identificación
2. Click "Consultar Datos": si existe, llena campos; si no, error
3. Modificar campos
4. Click "Crear": valida, inserta si no existe
5. Click "Actualizar": valida, actualiza si existe

### Validaciones Cliente
- Identificación: numérica, <=50 caracteres
- Nombres: 1-100 caracteres
- Apellidos: 1-100 caracteres

### Llamadas al Backend
- Pacientes.consultar_paciente(identificacion)
- Pacientes.crear_paciente(datos)
- Pacientes.actualizar_paciente(datos)

### Condicionales de UI
- btnActualizar enabled solo después de consultar paciente existente
- Foto se muestra si existe archivo

### Mensajes y Notificaciones
- Exito: "Paciente consultado/ creado/ actualizado de manera exitosa!!!"
- Error: "Paciente no existe!!!"
- Error: "Paciente ya existe!!!"
- Error: "Datos no superaron las validaciones mínimas!!!"

## Pantalla Principal - Tab Eventos

### Nombre y Ruta
- **Nombre**: Registro de Eventos Médicos
- **Tab**: Eventos

### Propósito
Registrar nuevos eventos en el historial médico del paciente.

### Roles con Acceso
Todos los usuarios autenticados.

### Elementos de UI
- Campo: text_identificacion_2
- Text areas: text_Estado, text_hea, text_impDiagnostica, text_conductaSeguir, text_motivoConsulta
- Campos: text_temperatura, text_tensionArterial, text_freCardiaca, text_freRespiratoria, text_oxigenacion
- Botón: btnCrearEvento, btnLimpiar_2

### Campos Obligatorios
- text_identificacion_2

### Reglas de Negocio Aplicadas
- Paciente debe existir
- Todos los campos son opcionales pero recomendados

### Acciones Disponibles
- **Crear Evento**: Registra nuevo evento para el paciente
- **Limpiar**: Resetea campos de evento

### Flujo de Interacción
1. Ingresar identificación paciente
2. Llenar campos del evento
3. Click "Crear Evento": valida paciente, inserta evento

### Validaciones Cliente
- Identificación: válida según validaciones

### Llamadas al Backend
- Pacientes.consultar_paciente(identificacion)
- Eventos.crear_evento(datosEvento)

### Mensajes
- Exito: "Evento creado de manera exitosa!!!"
- Error: "Paciente no existe!!!"

## Pantalla Principal - Tab Historial

### Nombre y Ruta
- **Nombre**: Consulta de Historial Médico
- **Tab**: Historial

### Propósito
Visualizar el historial completo de eventos médicos del paciente.

### Elementos de UI
- Campo: text_identificacion_3
- Text area: text_InformacionHistorial
- Botones: btnConsultarHistorial, btnDescargarHistorial, btnLimpiar_3

### Acciones Disponibles
- **Consultar Historial**: Muestra eventos en formato HTML
- **Descargar Historial**: Genera PDF con historial
- **Limpiar**: Resetea campo identificación y area de texto

### Flujo de Interacción
1. Ingresar identificación
2. Click "Consultar Historial": muestra eventos ordenados por fecha
3. Click "Descargar Historial": genera PDF

### Llamadas al Backend
- Eventos.consultar_historial(paciente_id)
- PDF_Historia_Clinica(paciente, historial)

### Mensajes
- Info: "Paciente no posee historial de eventos realizados!!!"

## Pantalla Principal - Tab Soportes

### Nombre y Ruta
- **Nombre**: Gestión de Soportes
- **Tab**: Soportes

### Propósito
Administrar archivos adjuntos (fotos y documentos) del paciente.

### Elementos de UI
- Campo: text_identificacion_3 (compartido con historial)
- Botones: btnCargarFoto, btnSubirSoporte, btnConsultarSoportes

### Acciones Disponibles
- **Cargar Foto**: Selecciona imagen y la asigna como foto del paciente
- **Subir Soporte**: Selecciona archivo y lo guarda en directorio paciente
- **Consultar Soportes**: Abre diálogo para ver archivos del paciente

### Flujo de Interacción
1. Ingresar identificación
2. Seleccionar acción: subir archivo o consultar existentes

### Llamadas al Backend
- Copia archivos con shutil
- Abre archivos con webbrowser

## Pantalla Principal - Tab Listado Pacientes

### Nombre y Ruta
- **Nombre**: Listado General de Pacientes
- **Tab**: Listado Pacientes

### Propósito
Visualizar lista de todos los pacientes con filtro por nombre.

### Elementos de UI
- Campo: text_identificacion_4 (usado como filtro nombre)
- Text area: text_ListadoPacientes
- Botón: btnConsultarListadoPacientes

### Acciones Disponibles
- **Consultar Listado Pacientes**: Muestra tabla HTML con pacientes

### Flujo de Interacción
1. Opcional: ingresar nombre para filtrar
2. Click botón: muestra lista en tabla

### Llamadas al Backend
- Pacientes.consultar_listado_pacientes(nombre)

### Mensajes
- Info: "No hay pacientes registrados!!!"
