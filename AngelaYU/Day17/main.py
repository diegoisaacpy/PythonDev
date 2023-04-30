class User:
    def __init__(self, user_id, username):#El método constuctor inicia el objeto
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', "Angela")
print(user_1.id)
print(user_1.username)



