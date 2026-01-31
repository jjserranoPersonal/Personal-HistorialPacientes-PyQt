# Base de Datos

## Esquema General

El sistema utiliza una base de datos relacional con 3 tablas principales:

- `paciente`: Información de pacientes
- `historial`: Eventos médicos del paciente
- `usuarios`: Usuarios del sistema

## Tablas

### paciente

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | ID único del paciente |
| identificacion | VARCHAR(50) | UNIQUE NOT NULL | Número de identificación |
| nombres | VARCHAR(100) | NOT NULL | Nombres del paciente |
| apellidos | VARCHAR(100) | NOT NULL | Apellidos del paciente |
| direccion | VARCHAR(200) |  | Dirección |
| correo | VARCHAR(100) |  | Correo electrónico |
| telefono | VARCHAR(50) |  | Teléfono |
| fechaNacimiento | DATE |  | Fecha de nacimiento |
| sexo | VARCHAR(1) |  | Sexo (M/F) |
| transfusiones | VARCHAR(2) |  | Transfusiones (SI/NO) |
| peso | VARCHAR(20) |  | Peso |
| talla | VARCHAR(20) |  | Talla |
| habitosToxicos | VARCHAR(300) |  | Hábitos tóxicos |
| alergiaMedicamentos | VARCHAR(300) |  | Alergias a medicamentos |
| vacunacion | VARCHAR(300) |  | Información de vacunación |
| app | VARCHAR(300) |  | Antecedentes personales patológicos |
| apf | VARCHAR(300) |  | Antecedentes personales fisiológicos |
| nombreAcompanante | VARCHAR(200) |  | Nombre del acompañante |
| created_at | TIMESTAMP | NOT NULL DEFAULT CURRENT_TIMESTAMP | Fecha de creación |

### historial

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | ID único del evento |
| pacienteId | INT | NOT NULL, FOREIGN KEY REFERENCES paciente(id) | ID del paciente |
| estado | VARCHAR(1000) |  | Estado del paciente |
| hea | VARCHAR(1000) |  | Historia enfermedad actual |
| impDiagnostica | VARCHAR(1000) |  | Impresión diagnóstica |
| conductaSeguir | VARCHAR(1000) |  | Conducta a seguir |
| motivoConsulta | VARCHAR(1000) |  | Motivo de consulta |
| temperatura | VARCHAR(20) |  | Temperatura |
| tensionArterial | VARCHAR(20) |  | Tensión arterial |
| freCardiaca | VARCHAR(20) |  | Frecuencia cardíaca |
| freRespiratoria | VARCHAR(20) |  | Frecuencia respiratoria |
| oxigenacion | VARCHAR(20) |  | Oxigenación |
| created_at | TIMESTAMP | NOT NULL DEFAULT CURRENT_TIMESTAMP | Fecha del evento |

### usuarios

| Campo | Tipo | Restricciones | Descripción |
|-------|------|---------------|-------------|
| id | INTEGER | PRIMARY KEY AUTOINCREMENT | ID único del usuario |
| usuario | VARCHAR(50) | UNIQUE NOT NULL | Nombre de usuario |
| password | VARCHAR(50) | NOT NULL | Contraseña |
| created_at | TIMESTAMP | NOT NULL DEFAULT CURRENT_TIMESTAMP | Fecha de creación |

## Relaciones

- `historial.pacienteId` -> `paciente.id` (1:N)

## Consultas Comunes

### Crear paciente
```sql
INSERT INTO paciente (identificacion, nombres, apellidos, ...) VALUES (...)
```

### Consultar historial de paciente
```sql
SELECT h.* FROM historial h JOIN paciente p ON p.id = h.pacienteId WHERE p.identificacion = ?
```

### Autenticar usuario
```sql
SELECT * FROM usuarios WHERE usuario = ? AND password = ?
```

## Migraciones

- Inicial: database/Scripts/Inicial_000/SQLite_Script_DB_Historial_Pacientes.sql
- Soporte para MySQL y SQLite con scripts separados
