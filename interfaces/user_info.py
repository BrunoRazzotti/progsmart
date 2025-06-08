class UserData:
    def __init__(self, name, subname, password, mail, is_admin,):
        self.name = name
        self.subname = subname
        self.password = password
        self.mail = mail
        self.is_admin = is_admin

    def get_is_admin(self):    
       return True if self.is_admin else False

