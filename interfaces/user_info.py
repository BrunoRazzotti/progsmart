class UserData:
    def __init__(self, name, subname, password, mail, role,):
        self.name = name
        self.subname = subname
        self.password = password
        self.mail = mail
        self.role = role

    def get_is_admin(self):    
       return True if self.role else False

