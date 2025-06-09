from data import user_data_from_local

def update_user():
	logged_user = user_data_from_local.get_logged_user()
	users_list = user_data_from_local.get_users()
	print("Lista de usuarios")
	for index, user in enumerate(users_list):
		if is_user_logged(logged_user, user) == False :
			print("--------------")
			print("Identificador Interno:", index)
			print("Nombre:", user.name)
			print("Apellido:", user.subname)
			print("Email:", user.mail)
			print("Rol:", user.role)

	user_id_selected = int(input("Seleccione un usuario a través de su 'Identificador Interno': "))
	try:
		selected_user = users_list[user_id_selected]
		print("Está por hacer ADMINISTRADOR al usuario", selected_user.name, selected_user.subname)
		answer = input("Está seguro? (s/n) ")
		if answer == "s":
			selected_user.role = "admin"
			print("Cambio realizado con éxito.")
	except:
		print("Identificador ingresado no válido.")
		

def is_user_logged(logged_user, user):
	return logged_user.name == user.name and logged_user.subname == user.subname and logged_user.mail == user.mail