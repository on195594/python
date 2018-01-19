class User(object):
    """It's about user info"""
    def __init__(self, first_name,last_name,gender,age):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print (self.first_name.title() + ' ' + self.last_name.title())
        print (self.gender)
        print (self.age)

    def greet_user(self):
        print('Hello,' + self.first_name.title() + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

girl = User('lily','chen','girl','22')
girl.describe_user()
girl.greet_user()

me = User('林','英军','男','33')
me.describe_user()
me.greet_user()
me.increment_login_attempts()
me.increment_login_attempts()
me.increment_login_attempts()
print (me.login_attempts)
me.reset_login_attempts()
print (me.login_attempts)




class Privileges(object):
    """docstring for privileges"""
    def __init__(self):
        self.privileges = ['can add post','can delete post','can ban user']

    def show_privileges(self):
        for p in self.privileges:
            print ('Admin '+p)

class Admin(User):
    """docstring for Admin"""
    def __init__(self, first_name,last_name,gender,age):
        super().__init__(first_name,last_name,gender,age)
        self.privileges = Privileges()



admin = Admin('admin','admin',None,0)
admin.privileges.show_privileges()
        
        