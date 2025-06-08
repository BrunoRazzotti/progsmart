from auth.auth import Auth
def login_user():
    name = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    is_admin = Auth().login(name, password)
    if is_admin == True:
        print("Bienvenido, administrador" if is_admin else "Bienvenido, usuario")
        return is_admin
    else:
        print("Usuario/Contraseña incorrecta")
        