from data import user_data_from_local

def show_user_data():
	user = user_data_from_local.get_logged_user()
	print("Datos del usuario:")
	print("Nombre:", user.name)
	print("Apellido:", user.subname)
	print("Email:", user.mail)
	print("Rol:", user.role)