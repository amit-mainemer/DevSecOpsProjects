class MyUser:
    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

    def __str__(self):
        return f'id -> {self.id}\nname -> {self.name}\nusername -> {self.username}\nemail -> {self.email}'
