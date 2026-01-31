# Frontend - Historial Pacientes

Aplicación web frontend desarrollada con React + TypeScript + Vite para gestión de historiales clínicos de pacientes.

## 🚀 Inicio Rápido

### Prerrequisitos

- Node.js 18+ y npm
- Backend FastAPI ejecutándose en http://localhost:8000

### Instalación

```bash
cd frontend

# Instalar dependencias
npm install

# Copiar archivo de variables de entorno
copy .env.example .env

# Ejecutar en modo desarrollo
npm run dev
```

La aplicación estará disponible en: **http://localhost:5173**

## 📦 Tecnologías Utilizadas

- **React 18** - Librería UI
- **TypeScript** - Tipado estático
- **Vite** - Build tool y dev server
- **React Router** - Enrutamiento
- **TanStack Query** - Gestión de estado del servidor
- **Zustand** - Gestión de estado global
- **Axios** - Cliente HTTP
- **Tailwind CSS** - Estilos
- **Lucide React** - Iconos
- **React Hook Form + Zod** - Formularios y validación

## 📁 Estructura del Proyecto

```
frontend/
├── src/
│   ├── components/        # Componentes reutilizables
│   │   └── Layout.tsx    # Layout principal con navegación
│   ├── pages/            # Páginas de la aplicación
│   │   ├── LoginPage.tsx
│   │   ├── DashboardPage.tsx
│   │   └── PacientesPage.tsx
│   ├── services/         # Servicios de API
│   │   └── api.ts       # Cliente Axios y endpoints
│   ├── stores/          # Stores de Zustand
│   │   └── authStore.ts # Estado de autenticación
│   ├── types/           # Tipos TypeScript
│   │   └── index.ts
│   ├── utils/           # Utilidades
│   ├── App.tsx          # Componente principal
│   ├── main.tsx         # Punto de entrada
│   └── index.css        # Estilos globales
├── public/              # Archivos estáticos
├── index.html
├── package.json
├── tsconfig.json
├── vite.config.ts
└── tailwind.config.js
```

## 🔐 Autenticación

El sistema usa JWT tokens para autenticación:

1. Login en `/login`
2. Token guardado en localStorage
3. Token enviado en header `Authorization: Bearer <token>`
4. Rutas protegidas redirigen a login si no hay token

### Usuarios de Prueba

- **Usuario:** `jserrano` / **Password:** `123456` (médico)
- **Usuario:** `admin` / **Password:** `admin123` (admin)

## 🛠️ Scripts Disponibles

```bash
# Desarrollo
npm run dev

# Build para producción
npm run build

# Preview del build
npm run preview

# Linting
npm run lint
```

## 🌐 Variables de Entorno

Crear archivo `.env` basado en `.env.example`:

```env
VITE_API_URL=http://localhost:8000
```

## 📱 Páginas Implementadas

### 1. Login (`/login`)
- Formulario de autenticación
- Validación de credenciales
- Redirección al dashboard

### 2. Dashboard (`/`)
- Vista general del sistema
- Estadísticas básicas
- Información del usuario actual

### 3. Pacientes (`/pacientes`)
- Lista de pacientes
- Búsqueda por nombre
- Paginación
- Acciones CRUD

## 🔌 Integración con Backend

El frontend se conecta al backend FastAPI a través de:

- **Base URL:** `http://localhost:8000`
- **API Version:** `/api/v1`
- **Autenticación:** JWT Bearer Token

### Endpoints Utilizados

```typescript
// Auth
POST /api/v1/auth/login
GET  /api/v1/auth/me

// Pacientes
GET    /api/v1/pacientes
GET    /api/v1/pacientes/{id}
POST   /api/v1/pacientes
PUT    /api/v1/pacientes/{id}
DELETE /api/v1/pacientes/{id}

// Eventos
GET  /api/v1/eventos
POST /api/v1/eventos
GET  /api/v1/eventos/pacientes/{id}/historial
```

## 🎨 Estilos y UI

- **Tailwind CSS** para estilos utility-first
- **Diseño responsive** mobile-first
- **Tema:** Azul/Indigo (personalizable en `tailwind.config.js`)
- **Iconos:** Lucide React

## 🐛 Solución de Problemas

### Error: "Cannot connect to backend"

Verificar que el backend esté ejecutándose:
```bash
cd backend
uvicorn app.main:app --reload
```

### Error: "401 Unauthorized"

El token expiró. Hacer logout y login nuevamente.

### Error: CORS

Verificar que el backend tenga configurado CORS para `http://localhost:5173`

## 📝 Próximas Funcionalidades

- [ ] Formulario de creación/edición de pacientes
- [ ] Vista detalle de paciente
- [ ] Gestión de eventos médicos
- [ ] Carga de archivos adjuntos
- [ ] Generación de reportes PDF
- [ ] Búsqueda avanzada
- [ ] Filtros y ordenamiento
- [ ] Paginación completa

## 🚀 Deployment

### Build para Producción

```bash
npm run build
```

Los archivos se generarán en la carpeta `dist/`

### Variables de Entorno en Producción

Actualizar `VITE_API_URL` con la URL del backend en producción.

## 📄 Licencia

Este proyecto es parte del sistema de migración de Historial Pacientes PyQt a Web.
