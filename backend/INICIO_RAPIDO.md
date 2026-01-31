# 🚀 Inicio Rápido - Backend

## Comandos Rápidos para Probar el Backend

### 1️⃣ Instalar Dependencias (Primera vez)

```bash
cd backend
python -m venv venv
venv\Scripts\activate
# Usar requirements-windows.txt para Windows con asyncpg
pip install -r requirements-windows.txt
```

### 2️⃣ Configurar PostgreSQL

**Opción más fácil - Docker:**

```bash
docker run --name postgres-historial -e POSTGRES_DB=historial_pacientes -e POSTGRES_USER=historial_user -e POSTGRES_PASSWORD=historial_pass -p 5432:5432 -d postgres:14
```

**O instalar PostgreSQL localmente y crear la base de datos.**

### 3️⃣ Verificar Archivo .env

Tu archivo `.env` ya está configurado correctamente. Si no, copia de `.env.example`:

```bash
cp .env.example .env
```

**Asegúrate de que la URL de base de datos use `asyncpg`:**

```env
DATABASE_URL=postgresql+asyncpg://historial_user:historial_pass@localhost:5432/historial_pacientes
```

### 4️⃣ Ejecutar Migraciones

```bash
# Crear migración inicial
alembic revision --autogenerate -m "Initial migration"

# Aplicar migraciones
alembic upgrade head
```

### 5️⃣ Crear Usuarios Iniciales

```bash
python scripts/create_initial_user.py
```

Usuarios creados:
- `jserrano` / `123456` (médico)
- `admin` / `admin123` (administrador)

### 6️⃣ Ejecutar Servidor

```bash
uvicorn app.main:app --reload
```

### 7️⃣ Probar la API

Abrir en el navegador: **http://localhost:8000/docs**

## Flujo de Prueba Rápido

1. **Login:**
   - Ir a `/api/v1/auth/login`
   - Click "Try it out"
   - Username: `jserrano`
   - Password: `123456`
   - Click "Execute"
   - Copiar el `access_token`

2. **Autorizar:**
   - Click en el botón "Authorize" (🔒) arriba a la derecha
   - Pegar el token (sin "Bearer")
   - Click "Authorize"

3. **Crear Paciente:**
   - Ir a `POST /api/v1/pacientes`
   - Click "Try it out"
   - Usar este JSON:
   ```json
   {
     "identificacion": "1234567890",
     "nombres": "Juan",
     "apellidos": "Pérez",
     "fecha_nacimiento": "1990-05-15",
     "sexo": "M",
     "telefono": "555-1234",
     "correo": "juan@example.com"
   }
   ```
   - Click "Execute"

4. **Listar Pacientes:**
   - Ir a `GET /api/v1/pacientes`
   - Click "Try it out"
   - Click "Execute"

5. **Crear Evento:**
   - Ir a `POST /api/v1/eventos`
   - Usar el ID del paciente creado
   - Ejemplo:
   ```json
   {
     "paciente_id": 1,
     "estado": "Estable",
     "motivo_consulta": "Dolor abdominal",
     "imp_diagnostica": "Gastritis aguda",
     "temperatura": "36.5",
     "tension_arterial": "120/80"
   }
   ```

6. **Ver Historial:**
   - Ir a `GET /api/v1/eventos/pacientes/{id}/historial`
   - Usar el ID del paciente
   - Click "Execute"

## ✅ Checklist de Verificación

- [ ] PostgreSQL está corriendo
- [ ] Dependencias instaladas
- [ ] Migraciones aplicadas
- [ ] Usuarios creados
- [ ] Servidor ejecutándose en http://localhost:8000
- [ ] Swagger UI accesible en http://localhost:8000/docs
- [ ] Login funciona y retorna token
- [ ] Puedo crear pacientes
- [ ] Puedo listar pacientes
- [ ] Puedo crear eventos
- [ ] Puedo ver historial

## 🐛 Solución Rápida de Problemas

**Error: "alembic: command not found"**
```bash
pip install alembic
```

**Error: "could not connect to database"**
```bash
# Verificar que PostgreSQL esté corriendo
docker ps
# O reiniciar el contenedor
docker start postgres-historial
```

**Error: "401 Unauthorized"**
- Hacer login nuevamente (el token expira en 30 minutos)

**Error: "relation does not exist"**
```bash
alembic upgrade head
```

## 📝 Próximos Pasos

Una vez que todo funcione:

1. ✅ **Backend funcionando** ← Estás aquí
2. 🔄 **Implementar frontend React**
3. 🔗 **Integrar frontend con backend**
4. 📦 **Agregar funcionalidades avanzadas**

Ver `GUIA_PRUEBAS.md` para más detalles y ejemplos con curl.
