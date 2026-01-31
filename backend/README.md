# Backend - Historial Pacientes API

API REST desarrollada con FastAPI para gestión de historiales clínicos de pacientes.

## Configuración Inicial

### 1. Crear entorno virtual e instalar dependencias

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Configurar variables de entorno

Copiar `.env.example` a `.env` y configurar:

```bash
cp .env.example .env
```

Editar `.env` con tus credenciales de PostgreSQL.

### 3. Configurar PostgreSQL

```sql
-- Crear base de datos y usuario
CREATE DATABASE historial_pacientes;
CREATE USER historial_user WITH PASSWORD 'historial_pass';
GRANT ALL PRIVILEGES ON DATABASE historial_pacientes TO historial_user;
```

### 4. Ejecutar migraciones

```bash
# Crear migración inicial
alembic revision --autogenerate -m "Initial migration"

# Aplicar migraciones
alembic upgrade head
```

### 5. Crear usuario inicial

```python
# Ejecutar script para crear usuario admin
python scripts/create_initial_user.py
```

## Ejecutar Servidor de Desarrollo

```bash
uvicorn app.main:app --reload
```

La API estará disponible en: http://localhost:8000

Documentación interactiva: http://localhost:8000/docs

## Estructura del Proyecto

```
backend/
├── app/
│   ├── api/
│   │   ├── deps.py              # Dependencias (auth, db)
│   │   └── v1/
│   │       ├── api.py           # Router principal
│   │       └── endpoints/       # Endpoints por módulo
│   │           ├── auth.py      # Autenticación
│   │           ├── pacientes.py # CRUD pacientes
│   │           └── eventos.py   # CRUD eventos
│   ├── core/
│   │   ├── config.py            # Configuración
│   │   ├── database.py          # Conexión DB
│   │   └── security.py          # JWT, passwords
│   ├── models/                  # Modelos SQLAlchemy
│   ├── schemas/                 # Schemas Pydantic
│   └── main.py                  # App FastAPI
├── alembic/                     # Migraciones
├── tests/                       # Tests
└── requirements.txt             # Dependencias
```

## Endpoints Principales

### Autenticación
- `POST /api/v1/auth/login` - Login
- `GET /api/v1/auth/me` - Usuario actual

### Pacientes
- `GET /api/v1/pacientes` - Listar pacientes
- `GET /api/v1/pacientes/{id}` - Obtener paciente
- `POST /api/v1/pacientes` - Crear paciente
- `PUT /api/v1/pacientes/{id}` - Actualizar paciente
- `DELETE /api/v1/pacientes/{id}` - Eliminar paciente

### Eventos
- `GET /api/v1/eventos` - Listar eventos
- `GET /api/v1/eventos/{id}` - Obtener evento
- `POST /api/v1/eventos` - Crear evento
- `GET /api/v1/eventos/pacientes/{id}/historial` - Historial de paciente

## Testing

```bash
pytest
```

## Próximos Pasos

1. Crear script para usuario inicial
2. Implementar endpoints de archivos
3. Implementar generación de PDF
4. Agregar tests
5. Configurar Docker
