def divide(a, b):
    """Divide a entre b.

    Args:
        a: Numerador.
        b: Denominador.

    Returns:
        El resultado de dividir a entre b.

    Raises:
        ValueError: Si b es 0.
    """
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def get_user(users, id):
    """Busca un usuario por su id dentro de una lista de usuarios.

    Args:
        users: Lista de diccionarios que representan usuarios, cada uno
            con al menos la clave "id".
        id: Id del usuario a buscar.

    Returns:
        dict: El diccionario del usuario cuyo campo "id" coincide con
        el id buscado, o None si no se encuentra ningún usuario con
        ese id.
    """
    for u in users:
        if u["id"] == id:
            return u
    return None
