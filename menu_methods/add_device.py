from data.devices_data_from_local import set_new_device
from data.get_devices_types import get_devices_type_from_local
from interfaces.devices_info import DeviceData, RecorderDeviceData, TempratureDeviceData

def add():
	print("::::::::::::::::::::::::::::::::::::::")
	print(":::::::::AGREGAR DISPOSITIVO::::::::::")
	print("::::::::::::::::::::::::::::::::::::::")
	print("\n")
	name = input("Nombre del dispositivo: ")
	status = input("Estado inicial (prendido 'p'/apagado 'a'): ")
	is_essential = input("Es un dispositivo esencial? (sí 's'/no 'n'): ")
	
	print("Tipo de dispositivo")

	for index, device_type in enumerate(get_devices_type_from_local()):
		print(f"{int(index) + 1}. {device_type["name"]}")

	selected_device_type = input("Seleccione una opción: ")

	status_value = True if status == "p" else False
	is_essential_value = True if is_essential == "s" else False

	match selected_device_type:
		case "1":
			new_device = RecorderDeviceData(name, status_value, is_essential_value, False)
		case "2":
			new_device = DeviceData(name, status_value, is_essential_value)
		case "3":
			new_device = DeviceData(name, status_value, is_essential_value)
		case "4":
			new_device = TempratureDeviceData(name, status_value, is_essential_value, 0)
		case _:
			return
		
	set_new_device(new_device)
	print("-----------------")
	print(f"Dispositivo {name} ha agregado con éxito!\n")
	print("-----------------")
	