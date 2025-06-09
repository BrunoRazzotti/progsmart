from interfaces import user_info
from data import user_data_from_local
def register_user():
    
    user_name = input("Ingrese Nombre del Usuario: ")
    password = input("Ingrese la contraseña:  ")            
    subname = input("Ingrese su apellido:  ")            
    mail = input("Ingrese su mail:  ")     
           
    
    new_user = user_info.UserData(user_name,subname,password, mail,"user")

    user_data_from_local.set_new_user(new_user)

    print("Usuario registrado con exito")
     
