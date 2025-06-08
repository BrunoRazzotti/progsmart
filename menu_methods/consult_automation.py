from data import save_mode_status

class Automation:
    def __init__(self,name,status):
        self.name = name
        self.status = status


def show_active_automations():
    active_automations = [
        Automation("Save Mode", save_mode_status.get_status()),
    ]

    is_at_least_one_active = False
    for automation in active_automations :
     if automation.status == "ACTIVADO":
      is_at_least_one_active = True
      print(f"Nombre: {automation.name}")
      print(f"Estado: {automation.status}")
         
    if is_at_least_one_active == False :
       print(f"No existen automatizaciones activas")

    
   

