"""Something"""

class FirstClass:
    """doesnt do anything"""
    #constructor
    def __init__(self,user_id,username) -> None:
        print("New user has been created.")
        self.i_d = user_id
        self.username = username
        self.followers = 0
    def Hello(self):
        print("Hello"+self.username)
USER = FirstClass("007","Bond")

print(USER.i_d,USER.username)
# have to put an argument
print(USER.followers)
USER.Hello()