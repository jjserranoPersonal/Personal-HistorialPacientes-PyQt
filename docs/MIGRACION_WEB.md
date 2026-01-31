# Migración a Aplicación Web

## Análisis de Requerimientos Funcionales

### Funcionalidades del Sistema Actual (PyQt Desktop)

#### 1. Autenticación
- Login con usuario/password
- Sin roles diferenciados
- Sesión persistente hasta cerrar aplicación

#### 2. Gestión de Pacientes
- **Crear paciente**: Formulario completo con datos personales y médicos
- **Consultar paciente**: Búsqueda por identificación
- **Actualizar paciente**: Modificación de datos existentes
- **Listar pacientes**: Búsqueda por nombre con resultados en tabla HTML

#### 3. Gestión de Eventos Médicos
- **Crear evento**: Registro de consulta médica con signos vitales
- **Consultar historial**: Visualización cronológica de eventos por paciente

#### 4. Gestión de Archivos
- **Foto de paciente**: Upload y visualización
- **Soportes médicos**: Upload/download de documentos por paciente

#### 5. Reportes
- **Generar PDF**: Historial clínico completo en formato PDF

### Mapeo a Arquitectura Web

| Funcionalidad Actual | Componente Web | Tecnología |
|----------------------|----------------|------------|
| Login PyQt | Página Login React | React + JWT |
| Formularios PyQt | Componentes React | React Hook Form |
| Consultas SQL directas | API REST | FastAPI + SQLAlchemy |
| SQLite/MySQL | PostgreSQL | PostgreSQL 14+ |
| Archivos locales | Storage API | FastAPI + S3/local storage |
| ReportLab PDF | PDF API | FastAPI + ReportLab |
| QMessageBox | Notificaciones | React Toast/Modal |

## Mejoras Propuestas en la Migración

### Seguridad
- Hash de contraseñas con bcrypt
- JWT con refresh tokens
- HTTPS obligatorio
- Validación de inputs (frontend y backend)
- SQL injection prevention (SQLAlchemy ORM)
- CORS configurado correctamente

### Roles y Permisos
- **Administrador**: Gestión completa + usuarios
- **Médico**: CRUD pacientes, eventos, reportes
- **Enfermera**: Consulta pacientes, eventos básicos
- **Recepcionista**: Consulta pacientes, gestión archivos

### UX/UI
- Diseño responsive (mobile, tablet, desktop)
- Navegación intuitiva con sidebar
- Búsqueda avanzada con filtros
- Paginación de resultados
- Feedback visual inmediato
- Modo oscuro/claro

### Funcionalidades Nuevas
- Dashboard con estadísticas
- Búsqueda avanzada multi-criterio
- Exportación a Excel/CSV
- Notificaciones en tiempo real
- Historial de cambios (audit log)
- Backup automático

## Arquitectura Propuesta

### Stack Tecnológico

#### Frontend
- **React 18**: Framework UI
- **TypeScript**: Tipado estático
- **Vite**: Build tool
- **React Router**: Navegación
- **TanStack Query**: Estado servidor
- **Zustand**: Estado global
- **React Hook Form**: Formularios
- **Zod**: Validación schemas
- **Tailwind CSS**: Estilos
- **shadcn/ui**: Componentes UI
- **Axios**: HTTP client

#### Backend
- **FastAPI**: Framework web
- **Python 3.11+**: Lenguaje
- **SQLAlchemy 2.0**: ORM
- **Alembic**: Migraciones
- **Pydantic**: Validación datos
- **python-jose**: JWT
- **passlib**: Hash passwords
- **python-multipart**: File uploads
- **reportlab**: PDF generation
- **pytest**: Testing

#### Base de Datos
- **PostgreSQL 14+**: Base de datos principal
- **Redis** (opcional): Cache y sesiones

#### DevOps
- **Docker**: Contenedores
- **Docker Compose**: Orquestación local
- **Git**: Control de versiones

### Estructura de Directorios

```
historial-pacientes-web/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── endpoints/
│   │   │   │   │   ├── auth.py
│   │   │   │   │   ├── pacientes.py
│   │   │   │   │   ├── eventos.py
│   │   │   │   │   ├── archivos.py
│   │   │   │   │   └── reportes.py
│   │   │   │   └── api.py
│   │   │   └── deps.py
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── security.py
│   │   │   └── database.py
│   │   ├── models/
│   │   │   ├── paciente.py
│   │   │   ├── evento.py
│   │   │   └── usuario.py
│   │   ├── schemas/
│   │   │   ├── paciente.py
│   │   │   ├── evento.py
│   │   │   └── usuario.py
│   │   ├── services/
│   │   │   ├── paciente_service.py
│   │   │   ├── evento_service.py
│   │   │   └── pdf_service.py
│   │   └── main.py
│   ├── alembic/
│   ├── tests/
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── layout/
│   │   │   ├── pacientes/
│   │   │   ├── eventos/
│   │   │   └── common/
│   │   ├── pages/
│   │   │   ├── Login.tsx
│   │   │   ├── Dashboard.tsx
│   │   │   ├── Pacientes.tsx
│   │   │   └── Historial.tsx
│   │   ├── hooks/
│   │   ├── services/
│   │   │   └── api.ts
│   │   ├── types/
│   │   ├── utils/
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── public/
│   ├── package.json
│   ├── tsconfig.json
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Modelo de Datos PostgreSQL

### Tabla: usuarios
```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    usuario VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    nombre_completo VARCHAR(200),
    rol VARCHAR(20) NOT NULL DEFAULT 'medico',
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tabla: pacientes
```sql
CREATE TABLE pacientes (
    id SERIAL PRIMARY KEY,
    identificacion VARCHAR(50) UNIQUE NOT NULL,
    nombres VARCHAR(100) NOT NULL,
    apellidos VARCHAR(100) NOT NULL,
    direccion VARCHAR(200),
    correo VARCHAR(100),
    telefono VARCHAR(50),
    fecha_nacimiento DATE,
    sexo VARCHAR(1),
    transfusiones VARCHAR(2),
    peso VARCHAR(20),
    talla VARCHAR(20),
    habitos_toxicos TEXT,
    alergia_medicamentos TEXT,
    vacunacion TEXT,
    app TEXT,
    apf TEXT,
    nombre_acompanante VARCHAR(200),
    foto_url VARCHAR(500),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER REFERENCES usuarios(id)
);
```

### Tabla: eventos
```sql
CREATE TABLE eventos (
    id SERIAL PRIMARY KEY,
    paciente_id INTEGER NOT NULL REFERENCES pacientes(id) ON DELETE CASCADE,
    estado TEXT,
    hea TEXT,
    imp_diagnostica TEXT,
    conducta_seguir TEXT,
    motivo_consulta TEXT,
    temperatura VARCHAR(20),
    tension_arterial VARCHAR(20),
    fre_cardiaca VARCHAR(20),
    fre_respiratoria VARCHAR(20),
    oxigenacion VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER REFERENCES usuarios(id)
);
```

### Tabla: archivos
```sql
CREATE TABLE archivos (
    id SERIAL PRIMARY KEY,
    paciente_id INTEGER NOT NULL REFERENCES pacientes(id) ON DELETE CASCADE,
    nombre_archivo VARCHAR(255) NOT NULL,
    tipo_archivo VARCHAR(50),
    ruta_archivo VARCHAR(500) NOT NULL,
    tamano_bytes INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_by INTEGER REFERENCES usuarios(id)
);
```

### Tabla: audit_log (nuevo)
```sql
CREATE TABLE audit_log (
    id SERIAL PRIMARY KEY,
    usuario_id INTEGER REFERENCES usuarios(id),
    accion VARCHAR(50) NOT NULL,
    tabla VARCHAR(50) NOT NULL,
    registro_id INTEGER,
    datos_anteriores JSONB,
    datos_nuevos JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## APIs REST Propuestas

### Autenticación
- `POST /api/v1/auth/login` - Login con usuario/password
- `POST /api/v1/auth/refresh` - Refresh token
- `POST /api/v1/auth/logout` - Logout
- `GET /api/v1/auth/me` - Obtener usuario actual

### Pacientes
- `GET /api/v1/pacientes` - Listar pacientes (paginado, filtros)
- `GET /api/v1/pacientes/{id}` - Obtener paciente por ID
- `POST /api/v1/pacientes` - Crear paciente
- `PUT /api/v1/pacientes/{id}` - Actualizar paciente
- `DELETE /api/v1/pacientes/{id}` - Eliminar paciente (soft delete)
- `GET /api/v1/pacientes/buscar` - Búsqueda avanzada

### Eventos
- `GET /api/v1/eventos` - Listar eventos
- `GET /api/v1/eventos/{id}` - Obtener evento
- `POST /api/v1/eventos` - Crear evento
- `GET /api/v1/pacientes/{id}/historial` - Historial de paciente

### Archivos
- `POST /api/v1/archivos/upload` - Subir archivo
- `GET /api/v1/archivos/{id}` - Descargar archivo
- `DELETE /api/v1/archivos/{id}` - Eliminar archivo
- `GET /api/v1/pacientes/{id}/archivos` - Listar archivos de paciente

### Reportes
- `GET /api/v1/reportes/paciente/{id}/pdf` - Generar PDF historial
- `GET /api/v1/reportes/estadisticas` - Dashboard stats

### Usuarios (Admin)
- `GET /api/v1/usuarios` - Listar usuarios
- `POST /api/v1/usuarios` - Crear usuario
- `PUT /api/v1/usuarios/{id}` - Actualizar usuario
- `DELETE /api/v1/usuarios/{id}` - Desactivar usuario

## Próximos Pasos

1. Configurar entorno de desarrollo local
2. Crear estructura de proyecto
3. Implementar backend básico con FastAPI
4. Configurar PostgreSQL y migraciones
5. Implementar frontend React con componentes básicos
