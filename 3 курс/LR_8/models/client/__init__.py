
class Client():
    def __init__(self, first_name, last_name, email, index):
        #self.__client = {"first_name": first_name, "last_name":last_name, "email": email}
        self.__firstname = first_name
        self.__lastname = last_name
        self.__email = email
        self.__index = index


    def __str__(self):
        return f'{str(self.firstname) + " " + str(self.lastname)}'


    @property
    def firstname(self):
        return self.__firstname

    @property
    def lastname(self):
        return self.__lastname

    @property
    def email(self):
        return self.__email

    @property
    def index(self):
        return self.__index
    
