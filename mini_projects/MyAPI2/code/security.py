from user import User

users = [
    User(1, "bob", "asdf")
]

username_mapping = {u.username: u for u in users}


userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None) # it's the same as username_mapping[username] but we can add default value in the second argument
    if user and user["password"]==password: #it's the same as if user in not None
        return user

def identity(payload): # function specific for JWT library
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
