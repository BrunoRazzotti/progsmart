from data.user_data_from_local import users as local_users

class Auth:
    def __init__(self):
        self.users = { user.name: user for user in local_users}

    def login(self, name, password):
        if name in self.users:
            user = self.users[name]
            if user.password == password:
                return  user.get_is_admin()
            else:
                return False
        else:
            return None     