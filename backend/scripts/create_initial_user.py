"""
Script para crear usuario inicial en la base de datos.
Ejecutar después de aplicar migraciones.
"""
import sys
from pathlib import Path

# Agregar directorio raíz al path
sys.path.append(str(Path(__file__).parent.parent))

from app.core.database import SessionLocal
from app.core.security import get_password_hash
from app.models.usuario import Usuario


def create_initial_user():
    """Crear usuario inicial admin"""
    db = SessionLocal()
    
    try:
        # Verificar si ya existe un usuario
        existing_user = db.query(Usuario).first()
        if existing_user:
            print("Ya existen usuarios en la base de datos.")
            return
        
        # Crear usuario admin
        admin_user = Usuario(
            usuario="admin",
            email="admin@historial.com",
            password_hash=get_password_hash("admin123"),
            nombre_completo="Administrador del Sistema",
            rol="admin",
            activo=True
        )
        
        db.add(admin_user)
        db.commit()
        db.refresh(admin_user)
        
        print("✓ Usuario admin creado exitosamente")
        print(f"  Usuario: admin")
        print(f"  Password: admin123")
        print(f"  Email: admin@historial.com")
        print(f"  Rol: admin")
        print("\n⚠️  IMPORTANTE: Cambiar la contraseña después del primer login")
        
        # Crear usuario médico de ejemplo
        medico_user = Usuario(
            usuario="jserrano",
            email="jserrano@historial.com",
            password_hash=get_password_hash("123456"),
            nombre_completo="Juan Serrano",
            rol="medico",
            activo=True
        )
        
        db.add(medico_user)
        db.commit()
        db.refresh(medico_user)
        
        print("\n✓ Usuario médico de ejemplo creado")
        print(f"  Usuario: jserrano")
        print(f"  Password: 123456")
        print(f"  Email: jserrano@historial.com")
        print(f"  Rol: medico")
        
    except Exception as e:
        print(f"Error al crear usuarios: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("Creando usuarios iniciales...")
    create_initial_user()
