def divide(a, b):
    if b == 0:
        raise ValueError("division by zero")
    return a / b


def get_user(users, id):
    for u in users:
        if u["id"] == id:
            return u
    return None
