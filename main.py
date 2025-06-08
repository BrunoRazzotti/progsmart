from menu_methods import list_devices, search_devices, add_device, delete_device, manage_automations, consult_user_data
from helpers import get_user_status 
from auth import login 

def main():
	print("Bienvenido a SmartHome Solutions, el sistema de automatización de casas inteligentes.\n")
	user = login.login_user()
	if user is None:
		main()
	else :	
		return display_menu(user)

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