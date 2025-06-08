class DeviceData:
	def __init__(self, name, status = False, is_essential = False):
		self.name = name
		self.status = status
		self.is_essential = is_essential

	def get_status(self):
		return "Prendida" if self.status else "Apagada"
	
	def get_is_essential(self):
		return "Si" if self.is_essential else "No"

class RecorderDeviceData(DeviceData):
	def __init__(self, name, status = False, is_essential = False, isRecording = False):
		super().__init__(name, status, is_essential)
		self.isRecording = isRecording

class TempratureDeviceData(DeviceData):
	def __init__(self, name, status = False, is_essential = False, temprature = 0):
		super().__init__(name, status, is_essential)
		self.temprature = temprature