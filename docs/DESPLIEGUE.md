# Procedimientos de Despliegue

## Empaquetado de la Aplicación

El sistema se empaqueta como aplicación de escritorio usando PyInstaller.

### Prerrequisitos

- Python con dependencias instaladas
- PyInstaller (incluido en requirements.txt)

### Comando de Empaquetado

```bash
pyinstaller --onefile --windowed MainWindow_Login.py
```

### Opciones

- `--onefile`: Genera un único ejecutable
- `--windowed`: Sin consola (para aplicaciones GUI)

### Archivos Generados

- dist/MainWindow_Login.exe (Windows)
- build/ (archivos temporales)

### Distribución

1. Copiar el ejecutable a los usuarios
2. Asegurar que tengan Python instalado (o empaquetar con --onedir si no)
3. Incluir AppConfig.json y directorios de recursos

### Configuración de Producción

- Cambiar configuración de BD a servidor MySQL de producción
- Asegurar backups de BD
- Configurar permisos de archivos

### Consideraciones

- La aplicación requiere acceso a BD y sistema de archivos
- Para distribución masiva, considerar instaladores como NSIS
- Probar en máquinas limpias
