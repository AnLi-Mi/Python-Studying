user = {"username": "jose", "access_level": "user"}


def make_secure(function):
    def secure_get_password():
        if user["access_level"]=="admin":
            return function()
        else:
            return f'No admin permissions for user {user["username"]}'
    return secure_get_password

@make_secure  # -> it's equal to "get_admin_password = make_secure(get_admin_password)"
def get_admin_password():
    return "1234" 


#get_admin_password = make_secure(get_admin_password)
print(get_admin_password())


    
#print(get_admin_password)
#print(type(get_admin_password))

#print(get_admin_password())
#print(type(get_admin_password()))

#get_admin_password = make_secure(get_admin_password)

#print(get_admin_password)
#print(type(get_admin_password))

#print(make_secure(get_admin_password))
#print(type(make_secure(get_admin_password)))

#print(make_secure(get_admin_password()))
#print(type(make_secure(get_admin_password())))

#print(make_secure(get_admin_password)())
#print(type(make_secure(get_admin_password)()))

#print(get_admin_password())
#print(type(get_admin_password()))


