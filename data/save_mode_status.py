save_mode_status = False

def get_status():
	return "ACTIVADO" if save_mode_status else "DESACTIVADO"

def update_status():
	global save_mode_status
	if save_mode_status:
		save_mode_status = False
	else:
		save_mode_status = True