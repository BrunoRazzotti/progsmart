from data.user_data_from_local import get_logged_user
from menu_methods import list_devices, search_devices, add_device, delete_device, manage_automations, consult_user_data, update_user_role
from helpers import get_user_status 
from auth import login , register

def main():
	print("Bienvenido a SmartHome Solutions, el sistema de automatización de casas inteligentes.\n")
	
	while True:
		display_auth()
		selected_option = input("Seleccione una opción: ")
		print("\n")
		match selected_option:
			case "1":
				login.login_user()
				logged_user = get_logged_user()
				if logged_user is None:
						main()
				else: 	
						return display_menu(logged_user)
			case "2":
				register.register_user()	
		
def display_auth():
	print("::::::::::::::::::::::::::::::::::")
	print("1. Ingresar Usuario")
	print("2. Registrar usuario")
	print("::::::::::::::::::::::::::::::::::")

def display_menu(user):
	menu = filter_menu(menu_list, user.role)
	print("::::::::::::::::::::::::::::::::::")
	print(":::::::::::::: MENU ::::::::::::::")
	print("::::::::::::::::::::::::::::::::::")
	for i,menu_item in enumerate(menu) :
			print (i,". ",menu_item["name"])
	print("::::::::::::::::::::::::::::::::::")
	selected_option = handle_menu_selection(menu)
	if selected_option != 0:
		display_menu(user)

def despedida():
	print("Gracias por usar SmartHome Solutions, Adios")
menu_list = [
	{
		"name": "Salir",
		"role": ["user", "admin"],
		"function": despedida
	},
	{
		"name": "Listar Dispositivos",
		"role": ["user", "admin"],
		"function": list_devices.list
	},
	{
		"name": "Buscar dispositivos",
		"role": ["user", "admin"],
		"function": search_devices.search
	},
	{
		"name": "Agregar dispositivos",
		"role": ["admin"],
		"function": add_device.add
	},
	{
		"name": "Eliminar dispositivos",
		"role": ["admin"],
		"function": delete_device.delete
	},
	{
		"name": "Gestionar automatizaciones",
		"role": ["user"],
		"function": manage_automations.manage_automations
	},
	{
		"name": "Automatizaciones activas",
		"role": ["admin"],
		"function": manage_automations.manage_automations
	},
	{
		"name": "Consultar información de usuario",
		"role": ["user"],
		"function": consult_user_data.show_user_data
	},
	{
		"name": "Actualizar rol de un usuario",
		"role": ["admin"],
		"function": update_user_role.update_user
	}
]

def filter_menu(list, role):
	filtered_list = [item for item in list if role in item["role"]]
	return filtered_list


def handle_menu_selection(menu):
	selected_option = int(input("Seleccione una opción: "))
	for i,menu_item in enumerate(menu) :
		if i == selected_option :
			menu_item["function"]()
	return selected_option




main()