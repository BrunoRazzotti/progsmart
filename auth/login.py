from auth.auth import Auth
from data.user_data_from_local import set_logged_user
def login_user():
    name = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    user = Auth(name, password).login()
    if user != None:
        print("Bienvenido, administrador" if user.role == "admin" else "Bienvenido, usuario")
        set_logged_user(user)
    else:
        print("Usuario/Contraseña incorrecta")
        return None