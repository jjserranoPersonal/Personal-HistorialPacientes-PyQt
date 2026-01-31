# Guía de Pruebas del Backend

## Paso 1: Configuración Inicial

### 1.1 Instalar Dependencias

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 1.2 Configurar PostgreSQL

**Opción A: Instalación Local**

Abrir pgAdmin o psql y ejecutar:

```sql
CREATE DATABASE historial_pacientes;
CREATE USER historial_user WITH PASSWORD 'historial_pass';
GRANT ALL PRIVILEGES ON DATABASE historial_pacientes TO historial_user;
```

**Opción B: Docker**

```bash
docker run --name postgres-historial ^
  -e POSTGRES_DB=historial_pacientes ^
  -e POSTGRES_USER=historial_user ^
  -e POSTGRES_PASSWORD=historial_pass ^
  -p 5432:5432 ^
  -d postgres:14
```

### 1.3 Verificar Archivo .env

El archivo `.env` ya está creado. Verificar que las credenciales coincidan con tu configuración de PostgreSQL.

## Paso 2: Ejecutar Migraciones

```bash
# Crear migración inicial
alembic revision --autogenerate -m "Initial migration"

# Aplicar migraciones
alembic upgrade head
```

**Nota:** Si alembic no está disponible, instalar primero las dependencias.

## Paso 3: Crear Usuarios Iniciales

```bash
python scripts/create_initial_user.py
```

Esto creará dos usuarios:
- **admin** / admin123 (rol: admin)
- **jserrano** / 123456 (rol: medico)

## Paso 4: Ejecutar Servidor

```bash
uvicorn app.main:app --reload
```

El servidor estará disponible en: http://localhost:8000

Documentación interactiva: http://localhost:8000/docs

## Paso 5: Probar Endpoints

### 5.1 Health Check

```bash
curl http://localhost:8000/health
```

**Respuesta esperada:**
```json
{"status": "healthy"}
```

### 5.2 Login

```bash
curl -X POST "http://localhost:8000/api/v1/auth/login" ^
  -H "Content-Type: application/x-www-form-urlencoded" ^
  -d "username=jserrano&password=123456"
```

**Respuesta esperada:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

**Guardar el token** para usarlo en las siguientes peticiones.

### 5.3 Obtener Usuario Actual

```bash
curl -X GET "http://localhost:8000/api/v1/auth/me" ^
  -H "Authorization: Bearer TU_TOKEN_AQUI"
```

### 5.4 Crear Paciente

```bash
curl -X POST "http://localhost:8000/api/v1/pacientes" ^
  -H "Authorization: Bearer TU_TOKEN_AQUI" ^
  -H "Content-Type: application/json" ^
  -d "{\"identificacion\":\"1234567890\",\"nombres\":\"Juan\",\"apellidos\":\"Perez\",\"fecha_nacimiento\":\"1990-05-15\",\"sexo\":\"M\",\"telefono\":\"555-1234\",\"correo\":\"juan@example.com\"}"
```

### 5.5 Listar Pacientes

```bash
curl -X GET "http://localhost:8000/api/v1/pacientes" ^
  -H "Authorization: Bearer TU_TOKEN_AQUI"
```

### 5.6 Obtener Paciente por ID

```bash
curl -X GET "http://localhost:8000/api/v1/pacientes/1" ^
  -H "Authorization: Bearer TU_TOKEN_AQUI"
```

### 5.7 Crear Evento Médico

```bash
curl -X POST "http://localhost:8000/api/v1/eventos" ^
  -H "Authorization: Bearer TU_TOKEN_AQUI" ^
  -H "Content-Type: application/json" ^
  -d "{\"paciente_id\":1,\"estado\":\"Estable\",\"motivo_consulta\":\"Dolor abdominal\",\"imp_diagnostica\":\"Gastritis aguda\",\"temperatura\":\"36.5\",\"tension_arterial\":\"120/80\"}"
```

### 5.8 Obtener Historial de Paciente

```bash
curl -X GET "http://localhost:8000/api/v1/eventos/pacientes/1/historial" ^
  -H "Authorization: Bearer TU_TOKEN_AQUI"
```

## Paso 6: Usar Swagger UI (Recomendado)

La forma más fácil de probar la API es usando la documentación interactiva:

1. Abrir: http://localhost:8000/docs
2. Click en "Authorize" (botón con candado)
3. Hacer login en `/api/v1/auth/login` para obtener token
4. Copiar el token (sin "Bearer")
5. Pegar en el campo "Value" del diálogo de autorización
6. Probar todos los endpoints desde la interfaz

## Paso 7: Verificar Base de Datos

Conectar a PostgreSQL y verificar las tablas:

```sql
\c historial_pacientes

-- Ver tablas
\dt

-- Ver usuarios
SELECT * FROM usuarios;

-- Ver pacientes
SELECT * FROM pacientes;

-- Ver eventos
SELECT * FROM eventos;
```

## Solución de Problemas

### Error: "alembic: command not found"

```bash
pip install alembic
```

### Error: "could not connect to server"

Verificar que PostgreSQL esté corriendo:

```bash
# Windows
Get-Service postgresql*

# Docker
docker ps
```

### Error: "relation does not exist"

Ejecutar migraciones:

```bash
alembic upgrade head
```

### Error: "401 Unauthorized"

El token expiró o es inválido. Hacer login nuevamente.

## Próximos Pasos

Una vez que el backend funcione correctamente:

1. ✅ Todos los endpoints responden correctamente
2. ✅ La autenticación funciona
3. ✅ Se pueden crear y consultar pacientes
4. ✅ Se pueden crear y consultar eventos

Entonces podemos continuar con:
- **Fase 3:** Implementar frontend React
- **Fase 4:** Integrar frontend con backend
- **Fase 5:** Agregar funcionalidades avanzadas (archivos, PDFs, etc.)
