# Especificaciones de API REST

## Información General

- **Base URL**: `http://localhost:8000/api/v1`
- **Formato**: JSON
- **Autenticación**: JWT Bearer Token
- **Versionado**: v1 en URL

## Autenticación

### POST /auth/login
Autenticar usuario y obtener token JWT.

**Request:**
```json
{
  "usuario": "string",
  "password": "string"
}
```

**Response 200:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "usuario": "jserrano",
    "email": "jserrano@example.com",
    "nombre_completo": "Juan Serrano",
    "rol": "medico"
  }
}
```

**Response 401:**
```json
{
  "detail": "Usuario o contraseña incorrectos"
}
```

### POST /auth/refresh
Renovar token de acceso.

**Headers:**
```
Authorization: Bearer {refresh_token}
```

**Response 200:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### GET /auth/me
Obtener información del usuario autenticado.

**Headers:**
```
Authorization: Bearer {access_token}
```

**Response 200:**
```json
{
  "id": 1,
  "usuario": "jserrano",
  "email": "jserrano@example.com",
  "nombre_completo": "Juan Serrano",
  "rol": "medico",
  "activo": true
}
```

## Pacientes

### GET /pacientes
Listar pacientes con paginación y filtros.

**Query Parameters:**
- `skip` (int): Offset para paginación (default: 0)
- `limit` (int): Límite de resultados (default: 20, max: 100)
- `nombre` (string): Filtrar por nombre
- `identificacion` (string): Filtrar por identificación

**Response 200:**
```json
{
  "total": 150,
  "items": [
    {
      "id": 1,
      "identificacion": "1234567890",
      "nombres": "Juan",
      "apellidos": "Pérez",
      "fecha_nacimiento": "1990-05-15",
      "sexo": "M",
      "telefono": "555-1234",
      "correo": "juan@example.com",
      "created_at": "2024-01-15T10:30:00"
    }
  ]
}
```

### GET /pacientes/{id}
Obtener paciente por ID.

**Response 200:**
```json
{
  "id": 1,
  "identificacion": "1234567890",
  "nombres": "Juan",
  "apellidos": "Pérez",
  "direccion": "Calle 123",
  "correo": "juan@example.com",
  "telefono": "555-1234",
  "fecha_nacimiento": "1990-05-15",
  "sexo": "M",
  "transfusiones": "NO",
  "peso": "75",
  "talla": "175",
  "habitos_toxicos": "Ninguno",
  "alergia_medicamentos": "Penicilina",
  "vacunacion": "Completa",
  "app": "Hipertensión",
  "apf": "Diabetes familiar",
  "nombre_acompanante": "María Pérez",
  "foto_url": "/uploads/fotos/1234567890.jpg",
  "created_at": "2024-01-15T10:30:00",
  "updated_at": "2024-01-20T14:20:00"
}
```

**Response 404:**
```json
{
  "detail": "Paciente no encontrado"
}
```

### POST /pacientes
Crear nuevo paciente.

**Request:**
```json
{
  "identificacion": "1234567890",
  "nombres": "Juan",
  "apellidos": "Pérez",
  "direccion": "Calle 123",
  "correo": "juan@example.com",
  "telefono": "555-1234",
  "fecha_nacimiento": "1990-05-15",
  "sexo": "M",
  "transfusiones": "NO",
  "peso": "75",
  "talla": "175",
  "habitos_toxicos": "Ninguno",
  "alergia_medicamentos": "Penicilina",
  "vacunacion": "Completa",
  "app": "Hipertensión",
  "apf": "Diabetes familiar",
  "nombre_acompanante": "María Pérez"
}
```

**Response 201:**
```json
{
  "id": 1,
  "identificacion": "1234567890",
  "nombres": "Juan",
  "apellidos": "Pérez",
  ...
}
```

**Response 400:**
```json
{
  "detail": "Paciente con esta identificación ya existe"
}
```

### PUT /pacientes/{id}
Actualizar paciente existente.

**Request:** (mismo formato que POST)

**Response 200:** (paciente actualizado)

**Response 404:**
```json
{
  "detail": "Paciente no encontrado"
}
```

### DELETE /pacientes/{id}
Eliminar paciente (soft delete).

**Response 204:** No Content

**Response 404:**
```json
{
  "detail": "Paciente no encontrado"
}
```

## Eventos Médicos

### GET /eventos
Listar eventos con paginación.

**Query Parameters:**
- `skip` (int): Offset
- `limit` (int): Límite
- `paciente_id` (int): Filtrar por paciente

**Response 200:**
```json
{
  "total": 50,
  "items": [
    {
      "id": 1,
      "paciente_id": 1,
      "estado": "Estable",
      "hea": "Dolor abdominal de 2 días de evolución",
      "imp_diagnostica": "Gastritis aguda",
      "conducta_seguir": "Omeprazol 20mg cada 12h",
      "motivo_consulta": "Dolor abdominal",
      "temperatura": "36.5",
      "tension_arterial": "120/80",
      "fre_cardiaca": "72",
      "fre_respiratoria": "16",
      "oxigenacion": "98",
      "created_at": "2024-01-20T09:15:00"
    }
  ]
}
```

### GET /eventos/{id}
Obtener evento por ID.

**Response 200:** (evento completo)

### POST /eventos
Crear nuevo evento médico.

**Request:**
```json
{
  "paciente_id": 1,
  "estado": "Estable",
  "hea": "Dolor abdominal de 2 días de evolución",
  "imp_diagnostica": "Gastritis aguda",
  "conducta_seguir": "Omeprazol 20mg cada 12h",
  "motivo_consulta": "Dolor abdominal",
  "temperatura": "36.5",
  "tension_arterial": "120/80",
  "fre_cardiaca": "72",
  "fre_respiratoria": "16",
  "oxigenacion": "98"
}
```

**Response 201:** (evento creado)

### GET /pacientes/{id}/historial
Obtener historial completo de un paciente.

**Response 200:**
```json
{
  "paciente": {
    "id": 1,
    "nombres": "Juan",
    "apellidos": "Pérez",
    ...
  },
  "eventos": [
    {
      "id": 5,
      "estado": "Estable",
      "created_at": "2024-01-20T09:15:00",
      ...
    },
    {
      "id": 3,
      "estado": "Mejorado",
      "created_at": "2024-01-15T14:30:00",
      ...
    }
  ]
}
```

## Archivos

### POST /archivos/upload
Subir archivo para un paciente.

**Request:** (multipart/form-data)
```
file: File
paciente_id: int
tipo_archivo: string (opcional: "soporte" | "foto")
```

**Response 201:**
```json
{
  "id": 1,
  "paciente_id": 1,
  "nombre_archivo": "radiografia.jpg",
  "tipo_archivo": "soporte",
  "ruta_archivo": "/uploads/soportes/1/radiografia.jpg",
  "tamano_bytes": 2048576,
  "created_at": "2024-01-20T10:00:00"
}
```

**Response 400:**
```json
{
  "detail": "Archivo demasiado grande. Máximo 10MB"
}
```

### GET /archivos/{id}
Descargar archivo.

**Response 200:** (archivo binario)

**Headers:**
```
Content-Type: application/octet-stream
Content-Disposition: attachment; filename="radiografia.jpg"
```

### GET /pacientes/{id}/archivos
Listar archivos de un paciente.

**Response 200:**
```json
{
  "total": 5,
  "items": [
    {
      "id": 1,
      "nombre_archivo": "radiografia.jpg",
      "tipo_archivo": "soporte",
      "tamano_bytes": 2048576,
      "created_at": "2024-01-20T10:00:00"
    }
  ]
}
```

### DELETE /archivos/{id}
Eliminar archivo.

**Response 204:** No Content

## Reportes

### GET /reportes/paciente/{id}/pdf
Generar y descargar PDF del historial clínico.

**Response 200:** (PDF binario)

**Headers:**
```
Content-Type: application/pdf
Content-Disposition: attachment; filename="historial_1234567890.pdf"
```

### GET /reportes/estadisticas
Obtener estadísticas del dashboard.

**Response 200:**
```json
{
  "total_pacientes": 150,
  "total_eventos_mes": 45,
  "pacientes_nuevos_mes": 12,
  "eventos_por_dia": [
    {"fecha": "2024-01-20", "cantidad": 5},
    {"fecha": "2024-01-21", "cantidad": 8}
  ]
}
```

## Usuarios (Solo Admin)

### GET /usuarios
Listar usuarios.

**Response 200:**
```json
{
  "total": 10,
  "items": [
    {
      "id": 1,
      "usuario": "jserrano",
      "email": "jserrano@example.com",
      "nombre_completo": "Juan Serrano",
      "rol": "medico",
      "activo": true,
      "created_at": "2024-01-01T00:00:00"
    }
  ]
}
```

### POST /usuarios
Crear nuevo usuario.

**Request:**
```json
{
  "usuario": "nuevo_usuario",
  "email": "nuevo@example.com",
  "password": "password123",
  "nombre_completo": "Nuevo Usuario",
  "rol": "medico"
}
```

**Response 201:** (usuario creado)

### PUT /usuarios/{id}
Actualizar usuario.

**Response 200:** (usuario actualizado)

### DELETE /usuarios/{id}
Desactivar usuario.

**Response 204:** No Content

## Códigos de Estado HTTP

- `200 OK`: Solicitud exitosa
- `201 Created`: Recurso creado exitosamente
- `204 No Content`: Operación exitosa sin contenido
- `400 Bad Request`: Error en validación de datos
- `401 Unauthorized`: No autenticado
- `403 Forbidden`: No autorizado (sin permisos)
- `404 Not Found`: Recurso no encontrado
- `422 Unprocessable Entity`: Error de validación Pydantic
- `500 Internal Server Error`: Error del servidor

## Manejo de Errores

Formato estándar de error:
```json
{
  "detail": "Mensaje de error descriptivo"
}
```

Para errores de validación (422):
```json
{
  "detail": [
    {
      "loc": ["body", "nombres"],
      "msg": "field required",
      "type": "value_error.missing"
    }
  ]
}
```
