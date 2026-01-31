# Lógica de Negocio

## Reglas de Negocio Críticas

### Gestión de Pacientes

1. **Identificación Única**
   - La identificación del paciente debe ser única en el sistema
   - Se valida al crear nuevo paciente
   - Si ya existe, se muestran los datos existentes en lugar de crear duplicado

2. **Campos Obligatorios**
   - Identificación, nombres, apellidos son requeridos para crear/actualizar
   - Otros campos son opcionales

3. **Cálculo de Edad**
   - Se calcula automáticamente al consultar paciente
   - Usa fecha de nacimiento vs fecha actual
   - Muestra años, meses o días según edad

### Gestión de Eventos Médicos

1. **Vinculación a Paciente**
   - Cada evento debe estar ligado a un paciente existente
   - Se valida existencia del paciente antes de crear evento

2. **Campos Médicos**
   - Estado, HEA, Impresión Diagnóstica, Conducta, Motivo Consulta
   - Signos vitales: temperatura, tensión, frecuencias, oxigenación

3. **Historial Ordenado**
   - Los eventos se muestran ordenados por fecha descendente (más reciente primero)

### Gestión de Archivos

1. **Fotos de Pacientes**
   - Archivo nombrado con identificación del paciente
   - Almacenado en Recursos/Soportes/Foto/
   - Se muestra automáticamente al consultar paciente

2. **Soportes Médicos**
   - Archivos almacenados en directorios por paciente: Recursos/Soportes/Historias/{identificacion}/
   - Pueden ser cualquier tipo de archivo

### Autenticación

1. **Usuarios Simples**
   - Usuario y password en tabla usuarios
   - No hay roles, todos tienen mismos permisos

2. **Validación Básica**
   - Longitud usuario/password: 1-50 caracteres
   - Comparación directa (no hash)

## Flujos de Trabajo

### Flujo de Creación de Paciente
1. Ingresar datos en formulario
2. Validar campos obligatorios
3. Verificar no existe identificación
4. Insertar en BD
5. Calcular edad
6. Mostrar éxito

### Flujo de Consulta de Historial
1. Ingresar identificación paciente
2. Validar paciente existe
3. Obtener lista de eventos ordenados por fecha
4. Formatear en HTML
5. Mostrar en text area

### Flujo de Generación de PDF
1. Obtener datos paciente
2. Obtener historial
3. Crear PDF con ReportLab
4. Dibujar título, datos paciente, tabla eventos
5. Guardar en directorio paciente

## Validaciones

### Validaciones de Input
- Identificación: numérica, <=50 caracteres
- Nombres/Apellidos: alfanumérico, 1-100 caracteres
- Usuario/Password: cualquier caracter, 1-50 caracteres

### Validaciones de Negocio
- Paciente debe existir para eventos
- Identificación única para pacientes
- Usuario único para login

## Cálculos

### Edad
```python
from dateutil.relativedelta import relativedelta
edad = relativedelta(datetime.now(), fecha_nacimiento)
```

### No hay cálculos matemáticos complejos adicionales

## Máquinas de Estado

No hay máquinas de estado explícitas. El sistema es CRUD simple.

## Casos Especiales

- Paciente sin historial: mostrar mensaje info
- Archivos no encontrados: no mostrar foto
- Conexión BD falla: excepción general
