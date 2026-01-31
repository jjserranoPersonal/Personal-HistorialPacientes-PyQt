# Flujo de Datos

## Diagrama General de Arquitectura

```
[Usuario] --> [Interfaz PyQt] --> [Lógica Python] --> [Base de Datos]
     ^                                                       |
     |                                                       |
     +------------------- [Respuesta] <-----------------------+
```

## Flujo de Autenticación

1. Usuario ingresa usuario/password en Login.ui
2. MainWindow_Login.login_iniciar()
3. Valida inputs con validaciones.py
4. Consulta db: SELECT * FROM usuarios WHERE usuario='{usuario}'
5. Si existe y password coincide: abre MainWindow_Principal
6. Else: mensaje error

## Flujo CRUD Paciente

### Crear Paciente
1. Usuario llena formulario en tab Pacientes
2. Click btnCrear
3. p_crear_paciente(): valida inputs
4. Pacientes.consultar_paciente(): verifica no existe
5. Si no existe: Pacientes.crear_paciente()
6. Commit DB
7. Mensaje éxito

### Consultar Paciente
1. Usuario ingresa ID, click btnConsultarDatos
2. p_consultar_paciente(): valida ID
3. Pacientes.consultar_paciente()
4. Si existe: p_asignar_datos_front(), p_calcuar_edad(), p_obtener_foto()
5. Else: mensaje error

## Flujo de Eventos

1. Usuario selecciona tab Eventos
2. Llena campos, click btnCrearEvento
3. p_crear_evento(): valida ID paciente
4. Pacientes.consultar_paciente(): verifica existe
5. Eventos.crear_evento()
6. Commit DB

## Flujo de Historial

1. Usuario ingresa ID, click btnConsultarHistorial
2. p_consultar_historial(): valida ID
3. Pacientes.consultar_paciente()
4. Eventos.consultar_historial()
5. Formatea HTML
6. Muestra en text_InformacionHistorial

## Flujo de Archivos

### Subir Soporte
1. Usuario ingresa ID, click btnSubirSoporte
2. p_subir_soportes(): valida paciente
3. QFileDialog para seleccionar archivo
4. shutil.copy() a Recursos/Soportes/Historias/{id}/

### Cargar Foto
1. Similar, copia a Recursos/Soportes/Foto/{id}

## Flujo de PDF

1. Usuario click btnDescargarHistorial
2. p_descargar_Historial(): obtiene paciente y historial
3. PdfHistoriaClinica(paciente, historial)
4. Genera PDF con ReportLab
5. Guarda en directorio paciente

## Estructura de Datos

### Paciente (dict)
```python
{
    'id': int,
    'identificacion': str,
    'nombres': str,
    'apellidos': str,
    'direccion': str,
    'correo': str,
    'telefono': str,
    'fechaNacimiento': str,
    'sexo': str,
    'transfusiones': str,
    'peso': str,
    'talla': str,
    'habitosToxicos': str,
    'alergiaMedicamentos': str,
    'vacunacion': str,
    'app': str,
    'apf': str,
    'nombreAcompanante': str,
    'created_at': str
}
```

### Evento (dict)
```python
{
    'id': int,
    'estado': str,
    'hea': str,
    'impDiagnostica': str,
    'conductaSeguir': str,
    'motivoConsulta': str,
    'temperatura': str,
    'tensionArterial': str,
    'freCardiaca': str,
    'freRespiratoria': str,
    'oxigenacion': str,
    'created_at': str
}
```
