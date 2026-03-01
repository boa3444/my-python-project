
class User:
    def __init__(self, username):
        self.username = username
        self.following = 0
        self.follower = 0

    def follow (self , user):
        self.following +=1
        user.follower +=1

user1 = User("divyanshe")
user2 = User("ddiveezz")

user1.follow(user2)
user1.follow(user2)

print(user2.follower , user1.following)