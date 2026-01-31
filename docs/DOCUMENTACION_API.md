# Documentación API

## Visión General

El sistema Historial Pacientes PyQt es una aplicación de escritorio que no expone una API REST, GraphQL u otro tipo de interfaz programática externa. Todas las operaciones se realizan a través de la interfaz gráfica de usuario (GUI) desarrollada con PyQt5.

## Arquitectura

- **Tipo de Aplicación**: Desktop Application
- **Interfaz**: GUI directa, no API
- **Acceso a Datos**: Directo desde la aplicación a la base de datos

## No hay Endpoints

Dado que no existe una API, no hay endpoints documentables. Las funcionalidades se acceden únicamente a través de la interfaz gráfica.

## Consideraciones para Futuras Mejoras

Si se requiere integrar con otros sistemas, se recomienda:

1. Desarrollar una API REST usando Flask o FastAPI
2. Implementar endpoints para:
   - Autenticación de usuarios
   - CRUD de pacientes
   - Gestión de historial médico
   - Generación de reportes

## Seguridad

Actualmente, la seguridad se maneja a nivel de aplicación. Para una API futura:

- Implementar JWT para autenticación
- Usar HTTPS
- Validar inputs
- Control de acceso basado en roles
