
class User:
    def __init__(self):
        self.user_name = "Guest" #defaults user name to Guest unitl changed by user


    def set_name(self, name):
        self.user_name = name #sets the chosen user name


    def get_name(self):
        return self.user_name #reason for this function is so that no matter how many changes the user name
    #undergoes, anytime this method is called, it will always return the most recent username.



