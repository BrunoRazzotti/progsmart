from interfaces import user_info
from helpers import get_user_status

user1 = user_info.UserData("Bruno", "Razzotti", "bruno", "brunorazzotti@gmail.com", True )
user2 = user_info.UserData("Juan", "Lopez", "juan" ,"Juanlopez@gmail.com", False ) 
user3 = user_info.UserData("Clara", "Rosales", "clara", "Clarita1977@gmail.com", False ) 

users = [user1,user2,user3]

def get_users ():
    return users

class UserDataFromLocal:
    def get_user_status(self):
        return get_user_status()
    
 