def divide(a, b):
    return a / b


def get_user(users, id):
    for u in users:
        if u["id"] == id:
            return u
