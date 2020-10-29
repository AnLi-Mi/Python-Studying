user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"

def secure_get_passoword(function):
    if user["access_level"]=="admin":
        return function
    

print(get_admin_password())
print (secure_get_passoword(get_admin_password))
    




