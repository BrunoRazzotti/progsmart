from menu_methods.automations.save_mode import save_mode

def manage_automations():
	print("::::::::::::::::::::::::::::::::::::::")
	print(":::::::::::AUTOMATIZACIONES:::::::::::")
	print("::::::::::::::::::::::::::::::::::::::")
	print("\n")

	print("1. Modo Ahorro de Energía")
	print("2. Volver al menú anterior")

	print("\n")

	while True:
		selected_option = input("Seleccione una automatización para configurarla: ")
		match selected_option:
			case "1":
				save_mode()
				return
			case "2":
				break
			case _:
				print("Opción seleccionada inválida.")
	
	
	print("\n\n")