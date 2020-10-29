import functools

user = {"username": "jose", "access_level": "user"}

def make_secure(function):
    @functools.wraps(function) # -> decorator that keeps the original names of decorated functions - use it on each decorator you write (on the  inner function)!
    def secure_get_password(ars, **kwargs):
        if user["access_level"]=="admin":
            return function(*ars, **kwargs)
        else:
            return f'No admin permissions for user {user["username"]}'
    return secure_get_password

@make_secure  # -> this is a decorator (not it's inner function). it's equal to "get_admin_password = make_secure(get_admin_password)"
def get_password(panel):
    if panel=="admin":
        return "1234"
    elif panel == "billing":
        return "gfFsvciW!!7r6?2864"

print(get_password("admin"))
print(get_password.__name__)

    
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


