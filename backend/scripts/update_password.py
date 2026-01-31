"""
Script para actualizar la contraseña del usuario jserrano a una más segura.
"""
import sys
from pathlib import Path

# Agregar directorio raíz al path
sys.path.append(str(Path(__file__).parent.parent))

from app.core.database import SessionLocal
from app.core.security import get_password_hash
from app.models.usuario import Usuario


def update_password():
    """Actualizar contraseña del usuario jserrano"""
    db = SessionLocal()
    
    try:
        # Buscar usuario jserrano
        user = db.query(Usuario).filter(Usuario.usuario == "jserrano").first()
        
        if not user:
            print("❌ Usuario jserrano no encontrado")
            return
        
        # Nueva contraseña segura
        new_password = "JSerrano2024!Secure"
        user.password_hash = get_password_hash(new_password)
        
        db.commit()
        
        print("✅ Contraseña actualizada exitosamente")
        print(f"  Usuario: jserrano")
        print(f"  Nueva contraseña: {new_password}")
        print("\n⚠️  Guarda esta contraseña en un lugar seguro")
        
    except Exception as e:
        print(f"❌ Error al actualizar contraseña: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    print("Actualizando contraseña de usuario jserrano...")
    update_password()
