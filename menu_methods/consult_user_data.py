from data import user_data_from_local


def show_user_data():
    for user in user_data_from_local.get_users():
        if user.name == False:
            print("Datos del usuario:")
            print("Nombre:", user.name)
            print("Apellido:", user.subname)
            print("Email:", user.mail)
            print("Es admin o usuario:", user.is_admin)