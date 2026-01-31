# Roles de Usuario

## Sistema de Roles

El sistema no implementa un sistema de roles complejo. Todos los usuarios autenticados tienen los mismos permisos.

## Tabla de Usuarios

- **usuarios**: Tabla que almacena usuarios con usuario y password

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | INTEGER | ID único |
| usuario | VARCHAR(50) | Nombre de usuario (único) |
| password | VARCHAR(50) | Contraseña (texto plano) |
| created_at | TIMESTAMP | Fecha de creación |

## Usuario por Defecto

- **usuario**: jserrano
- **password**: 123456

## Permisos

Todos los usuarios pueden:

- **Gestión de Pacientes**: Crear, consultar, actualizar pacientes
- **Registro de Eventos**: Crear eventos médicos para pacientes
- **Consulta de Historial**: Ver historial completo de eventos por paciente
- **Generación de Reportes**: Descargar historial en PDF
- **Gestión de Soportes**: Subir y consultar archivos adjuntos
- **Gestión de Fotos**: Cargar y mostrar fotos de pacientes
- **Consulta de Listados**: Ver listado general de pacientes

## Control de Acceso

- **Autenticación**: Usuario y contraseña en tabla usuarios
- **Sesión**: Mantiene sesión abierta hasta cerrar aplicación
- **Validaciones**: Básicas en frontend (longitud usuario/password)

## Limitaciones Actuales

- No hay roles diferenciados (todos son iguales)
- Contraseñas en texto plano (inseguro)
- No hay expiración de sesiones
- No hay logging de accesos

## Recomendaciones de Mejora

Implementar un sistema de roles con permisos granulares:

### Roles Sugeridos

1. **Administrador**
   - Todos los permisos
   - Gestión de usuarios
   - Configuración del sistema

2. **Médico**
   - CRUD pacientes
   - Registro eventos médicos
   - Consulta historial
   - Generación reportes

3. **Enfermera**
   - Consulta pacientes
   - Registro eventos básicos
   - Gestión soportes

4. **Recepcionista**
   - Consulta pacientes
   - Gestión fotos y soportes básicos

### Mejoras de Seguridad

- Hash de contraseñas (bcrypt)
- JWT o sesiones seguras
- Logging de acciones
- Control de acceso basado en roles (RBAC)
