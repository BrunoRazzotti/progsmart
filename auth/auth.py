from data.user_data_from_local import users as local_users

class Auth:
    def __init__(self, name,password):
        self.name = name
        self.password = password
        self.users = local_users
        self.user = None

    def login(self):
        for user in self.users:
            if user.name == self.name and user.password == self.password:
                self.user = user
        return self.user

           