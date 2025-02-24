class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("email accessed")
        return self._email
    
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email
        else:
            print("Invalid email address")

  
user1 = User("Mark", "mark@gmail.com", 12098)
user1.email = "bobemail.com"
print(user1.email)

user2 = User("John", "john@gmail.com", "ab123")
print(user2.email)


# static attributes
class CreateUser:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email     
        CreateUser.user_count += 1   

    def display_user(self):
        print(f"username: {self.username}, EMail: {self.email}")

user_one = CreateUser("Jack", "jack@gmail.com")
user_two = CreateUser("Jill", "jill@gmail.com")

print(CreateUser.user_count)
