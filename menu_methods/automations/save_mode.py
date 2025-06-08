from data import devices_data_from_local, save_mode_status

def save_mode():
	print(f"\nModo ahorro de energía: {save_mode_status.get_status()}")
	update_status = input("Desea cambiar el estado del Modo de Ahorro de Energía? (s/n): ")
	if update_status == "s":
		save_mode_status.update_status()
		if save_mode_status.get_status():
			devices = devices_data_from_local.get_devices()
			for device in devices:
				if device.is_essential == False:
					device.status = False
			print("Modo de Ahorro de Energía ACTIVADO")
			print("Todos los dispositivos NO esenciales han sido apagados.\n")
		else:
			print("Modo de Ahorro de Energía DESACTIVADO")

	return

