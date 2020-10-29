user = {"username": "jose", "access_level": "guest"}

def get_admin_password():
    return "1234"

def secure_get_passoword():
    if user["access_level"]=="admin":
        return get_password()
    else:
        return"access denied"



print(get_admin_password())
print (secure_get_passoword())
    




