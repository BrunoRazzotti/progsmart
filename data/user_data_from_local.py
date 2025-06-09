from interfaces import user_info
from helpers import get_user_status

user1 = user_info.UserData("Bruno", "Razzotti", "bruno", "brunorazzotti@gmail.com", "admin" )
user2 = user_info.UserData("Juan", "Lopez", "juan" ,"Juanlopez@gmail.com", "user" ) 
user3 = user_info.UserData("Clara", "Rosales", "clara", "Clarita1977@gmail.com", "user" ) 

users = [user1,user2,user3]

def get_users ():
    return users

def set_new_user(user):
    users.append(user)

class UserDataFromLocal:
    def get_user_status(self):
        return get_user_status()
    
 