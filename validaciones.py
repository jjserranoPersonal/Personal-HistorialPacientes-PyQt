# Valida usuario
def validar_usuario(usuario: str) -> bool:
    return (len(usuario) > 0 and len(usuario) <= 50)

# Valida password
def validar_password(password: str) -> bool:
    return (len(password) > 0 and len(password) <= 50)

# Valida identificacion.
def validar_identificacion(identificacion: str) -> bool:
    return (identificacion.isnumeric() and len(identificacion) <= 50)

# Valida nombres
def validar_nombres(nombres: str) -> bool:
    return (len(nombres) > 0 and len(nombres) <= 100)

# Valida apellidos
def validar_apellidos(apellidos: str) -> bool:
    return (len(apellidos) > 0 and len(apellidos) <= 100)

