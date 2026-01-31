# Guía de Configuración del Entorno de Desarrollo Local

## Prerrequisitos

### Software Requerido

1. **Python 3.11+**
   - Descargar desde: https://www.python.org/downloads/
   - Verificar instalación: `python --version`

2. **Node.js 18+ y npm**
   - Descargar desde: https://nodejs.org/
   - Verificar instalación: `node --version` y `npm --version`

3. **PostgreSQL 14+**
   - Descargar desde: https://www.postgresql.org/download/
   - O usar Docker: `docker run --name postgres -e POSTGRES_PASSWORD=postgres -p 5432:5432 -d postgres:14`

4. **Git**
   - Descargar desde: https://git-scm.com/downloads
   - Verificar instalación: `git --version`

5. **Docker y Docker Compose** (Opcional pero recomendado)
   - Descargar desde: https://www.docker.com/products/docker-desktop

6. **Editor de Código**
   - Visual Studio Code (recomendado)
   - Extensiones recomendadas: Python, ESLint, Prettier, Tailwind CSS IntelliSense

## Configuración Paso a Paso

### 1. Crear Estructura del Proyecto

```bash
# Crear directorio principal
mkdir historial-pacientes-web
cd historial-pacientes-web

# Inicializar Git
git init

# Crear estructura de directorios
mkdir backend frontend
```

### 2. Configurar Backend (FastAPI)

```bash
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Crear requirements.txt
```

**backend/requirements.txt:**
```txt
fastapi==0.109.0
uvicorn[standard]==0.27.0
sqlalchemy==2.0.25
alembic==1.13.1
psycopg2-binary==2.9.9
pydantic==2.5.3
pydantic-settings==2.1.0
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-multipart==0.0.6
reportlab==4.0.9
pytest==7.4.4
pytest-asyncio==0.23.3
httpx==0.26.0
python-dotenv==1.0.0
```

```bash
# Instalar dependencias
pip install -r requirements.txt

# Crear estructura de directorios
mkdir -p app/api/v1/endpoints app/core app/models app/schemas app/services tests
```

### 3. Configurar PostgreSQL

```bash
# Opción 1: Instalación local
# Crear base de datos
psql -U postgres
CREATE DATABASE historial_pacientes;
CREATE USER historial_user WITH PASSWORD 'historial_pass';
GRANT ALL PRIVILEGES ON DATABASE historial_pacientes TO historial_user;
\q

# Opción 2: Docker
docker run --name postgres-historial \
  -e POSTGRES_DB=historial_pacientes \
  -e POSTGRES_USER=historial_user \
  -e POSTGRES_PASSWORD=historial_pass \
  -p 5432:5432 \
  -d postgres:14
```

### 4. Configurar Variables de Entorno

**backend/.env:**
```env
# Database
DATABASE_URL=postgresql://historial_user:historial_pass@localhost:5432/historial_pacientes

# Security
SECRET_KEY=tu-clave-secreta-muy-segura-cambiar-en-produccion
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# CORS
BACKEND_CORS_ORIGINS=["http://localhost:5173", "http://localhost:3000"]

# App
PROJECT_NAME="Historial Pacientes API"
VERSION="1.0.0"
API_V1_STR="/api/v1"

# File Storage
UPLOAD_DIR=./uploads
MAX_UPLOAD_SIZE=10485760  # 10MB
```

### 5. Configurar Frontend (React + Vite)

```bash
cd ../frontend

# Crear proyecto React con Vite y TypeScript
npm create vite@latest . -- --template react-ts

# Instalar dependencias base
npm install

# Instalar dependencias adicionales
npm install react-router-dom @tanstack/react-query axios zustand
npm install react-hook-form @hookform/resolvers zod
npm install lucide-react
npm install -D tailwindcss postcss autoprefixer
npm install -D @types/node

# Inicializar Tailwind CSS
npx tailwindcss init -p
```

**frontend/tailwind.config.js:**
```js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

**frontend/src/index.css:**
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

**frontend/.env:**
```env
VITE_API_BASE_URL=http://localhost:8000
VITE_API_VERSION=v1
```

### 6. Configurar Docker Compose (Opcional)

**docker-compose.yml** (en raíz del proyecto):
```yaml
version: '3.8'

services:
  postgres:
    image: postgres:14
    container_name: historial-postgres
    environment:
      POSTGRES_DB: historial_pacientes
      POSTGRES_USER: historial_user
      POSTGRES_PASSWORD: historial_pass
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  backend:
    build: ./backend
    container_name: historial-backend
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    volumes:
      - ./backend:/app
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://historial_user:historial_pass@postgres:5432/historial_pacientes
    depends_on:
      - postgres

  frontend:
    build: ./frontend
    container_name: historial-frontend
    command: npm run dev -- --host
    volumes:
      - ./frontend:/app
      - /app/node_modules
    ports:
      - "5173:5173"
    environment:
      VITE_API_BASE_URL: http://localhost:8000

volumes:
  postgres_data:
```

### 7. Verificar Instalación

```bash
# Backend
cd backend
source venv/bin/activate  # o venv\Scripts\activate en Windows
python -c "import fastapi; print(fastapi.__version__)"

# Frontend
cd ../frontend
npm run dev

# PostgreSQL
psql -U historial_user -d historial_pacientes -h localhost
```

## Comandos Útiles

### Backend
```bash
# Activar entorno virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Ejecutar servidor de desarrollo
uvicorn app.main:app --reload

# Crear migración
alembic revision --autogenerate -m "descripcion"

# Aplicar migraciones
alembic upgrade head

# Ejecutar tests
pytest

# Formatear código
black app/
isort app/
```

### Frontend
```bash
# Ejecutar servidor de desarrollo
npm run dev

# Build para producción
npm run build

# Preview build
npm run preview

# Linting
npm run lint
```

### Docker
```bash
# Iniciar todos los servicios
docker-compose up -d

# Ver logs
docker-compose logs -f

# Detener servicios
docker-compose down

# Reconstruir servicios
docker-compose up -d --build
```

## Estructura de Archivos Inicial

```
historial-pacientes-web/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── api/
│   │   ├── core/
│   │   ├── models/
│   │   ├── schemas/
│   │   └── services/
│   ├── alembic/
│   ├── tests/
│   ├── .env
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── App.tsx
│   │   ├── main.tsx
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   └── types/
│   ├── public/
│   ├── .env
│   ├── package.json
│   ├── tsconfig.json
│   └── Dockerfile
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Próximos Pasos

1. Implementar configuración base de FastAPI
2. Crear modelos SQLAlchemy
3. Configurar Alembic para migraciones
4. Implementar autenticación JWT
5. Crear componentes React básicos
