users = [
    {"id": 1,
    "username": "bob",
    "password":"asdf"
    }
]

username_mapping = {"bob":{
    "id": 1,
    "username": "bob",
    "password":"asdf"
    }
}

userid_mapping = {1 :{
    "id": 1,
    "username": "bob",
    "password":"asdf"
    }
}

def authenticate(username, password):
    user = username_mapping.get(username, None) # it's the same as username_mapping[username] but we can add default value in the second argument

    if user and user[password]==password: #it's the same as if user in not None
        return user
 
