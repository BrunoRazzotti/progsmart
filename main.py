from menu_methods import list_devices, search_devices, add_device, delete_device, manage_automations, consult_user_data
from helpers import get_user_status 
from auth import login 

def main():
	print("Bienvenido a SmartHome Solutions, el sistema de automatización de casas inteligentes.\n")
	is_admin = login.login_user()
	if is_admin is None:
		print("Usuario no existe")
	elif is_admin:	
		return handle_menu_selection_admin()
	else:
		return handle_menu_selection_user()
	
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
			

def display_menu_admin():
	print("::::::::::::::::::::::::::::::::::")
	print("1. Listar dispositivos")
	print("2. Buscar dispositivos")
	print("3. Agregar dispositivos")
	print("4. Eliminar dispositivos")
	print("5. Gestionar automatizaciones")
	print("6. Consultar información")
	print("0. Salir")
	print("::::::::::::::::::::::::::::::::::")
def display_menu_user():
	print("::::::::::::::::::::::::::::::::::")
	print("1. Listar dispositivos")
	print("2. Buscar dispositivos")
	print("3. Gestionar automatizaciones")
	print("4. Consultar información")
	print("0. Salir")
	print("::::::::::::::::::::::::::::::::::")

main()