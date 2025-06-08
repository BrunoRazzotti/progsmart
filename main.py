from menu_methods import list_devices, search_devices, add_device, delete_device, manage_automations, consult_user_data
from helpers import get_user_status 
from auth import login 

def main():
	print("Bienvenido a SmartHome Solutions, el sistema de automatización de casas inteligentes.\n")
	user = login.login_user()
	if user is None:
		main()
	elif user.role == "admin":	
		return display_menu(user)
	else:
		return display_menu(user)
	
def handle_menu_selection_admin():
	while True:
		display_menu_admin()
		selected_option = input("Seleccione una opción: ")
		print("\n")
		match selected_option:
			case "1":
				list_devices.list()
			case "2":
				search_devices.search()
			case "3":
				add_device.add()
			case "4":
				delete_device.delete()
			case "5":
				manage_automations.manage_automations()
			case "6":
				consult_user_data.show_user_data()
			case "0":
				break
			case _:
				print("Valor recibido inválido")
def handle_menu_selection_user():
	while True:
		display_menu_user()
		selected_option = input("Seleccione una opción: ")
		print("\n")
		match selected_option:
			case "1":
				list_devices.list()
			case "2":
				search_devices.search()
			case "3":
				manage_automations.manage_automations()
			case "4":
				consult_user_data.show_user_data()
			case "0":
				break
			case _:
				print("Valor recibido inválido")

def display_menu_general():
	print("::::::::::::::::::::::::::::::::::")
	print("0. Salir")
	print("1. Listar dispositivos")
	print("2. Buscar dispositivos")

def display_menu_admin():
	print("3. Agregar dispositivos")
	print("4. Eliminar dispositivos")
	print("5. Automatizaciones activas")
	print("::::::::::::::::::::::::::::::::::")
def display_menu_user():
	print("3. Gestionar automatizaciones")
	print("4. Consultar información")
	print("::::::::::::::::::::::::::::::::::")

def display_menu(user):
	#display_menu_general()
	#if user.is_admin == True :
	#	display_menu_admin()
	#else : 
	#	display_menu_user()
	handle_menu_selection()

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



def handle_menu_selection():
		selected_option = int(input("Seleccione una opción: "))
		for i,menu_item in enumerate(menu_list) :
			if i == selected_option :
				menu_item["function"]()



main()