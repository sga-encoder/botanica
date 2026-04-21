from domain import UserService

if __name__ == "__main__":
    user_id = 1  # Cambia por el ID que quieras consultar
    service = UserService()
    user_info = service.get_user_info(user_id)
    if user_info:
        print("Usuario encontrado:", user_info)
    else:
        print("Usuario no encontrado.")
