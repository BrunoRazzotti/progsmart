def get_device_attr(device):
	print("-----------------")
	print(f"Nombre: {device.name}")
	print(f"Estado: {device.get_status()}")
	print(f"Es esencial: {device.get_is_essential()}")
	if hasattr(device, 'isRecording'):
		print("Grabando: Si")
	if hasattr(device, 'temprature'):
		print(f"Temperatura del dispositivo: {device.temprature}°")