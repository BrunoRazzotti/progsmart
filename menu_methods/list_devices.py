from data import devices_data_from_local
from helpers import get_device_attr

def list():
	devices = devices_data_from_local.get_devices()
	print("::::::::::::::::::::::::::::::::::::::")
	print(":::::::DISPOSITIVOS REGISTRADOS:::::::")
	print("::::::::::::::::::::::::::::::::::::::")
	print("\n")
	for device in devices:
		get_device_attr.get_device_attr(device)
	print("\n")
