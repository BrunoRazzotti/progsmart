from auth.auth import Auth
def login_user():
    name = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    user = Auth(name, password).login()
    if user != None:
        print("Bienvenido, administrador" if user.role == "admin" else "Bienvenido, usuario")
        return user
    else:
        print("Usuario/Contraseña incorrecta")
        return None