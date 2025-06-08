from data import devices_data_from_local
from helpers import get_device_attr

def search():
	print("::::::::::::::::::::::::::::::::::::::")
	print(":::::::BUSQUEDA DE DISPOSITIVO::::::::")
	print("::::::::::::::::::::::::::::::::::::::")
	print("\n")
	devices = devices_data_from_local.get_devices()
	while True:
		print("1. Buscar dispositivo")
		print("2. Volver al menú principal")
		selected_option = input("Seleccione una opción: ")
		if selected_option == "2":
			break
		elif selected_option == "1":
			device_name = input("\nEscriba el nombre del dispositivo: \n")

			for device in devices:
				if device.name.lower() == device_name.lower():
					print("DISPOSITIVO ENCONTRADO\n")
					get_device_attr.get_device_attr(device)
					print("-----------------")
					break
				else:
					print(f"No existe un dispositivo en el sistema con el nombre ingresado: {device_name}")

		print("\n")
