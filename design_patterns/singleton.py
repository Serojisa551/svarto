class Database:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name, passport, server):
        self.name = name
        self.passport = passport
        self.server = server


user1 = Database("Seroj", "123", "am")
user2 = Database("Felx", "789", "ru")
print(user1 is user2)
