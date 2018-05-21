# Classes and Objects

class Person:
    __name = ''  # Private property - cant access or change from outisde of the class
    __email = ''

    def __init__(self, name, email):
        self.__name = name
        self.__email = email

    def set_name(self, name):
        self.__name = name
    
    def get_name(self):
        return self.__name
    
    def set_email(self, email):
        self.__email = email
    
    def get_email(self):
        return self.__email
    
    def toString(self):
        return '{} can be contacted at {}'.format(self.__name, self.__email)
    
sivar = Person('Sivar Sarkawt', 'sivar@test.com')
#sivar.set_name('Sivar Sarkawt')
#sivar.set_email('sivar@test.com')

print(sivar.get_name())
print(sivar.get_email())
print(sivar.toString())

class Customer(Person):
    __balance = 0

    def __init__(self, name, email, balance):
        self.__name = name
        self.__email = email
        self.__balance = balance
        super(Customer, self).__init__(name, email)
    
    def set_balance(self, balance):
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def toString(self):
        return '{} has a balance of {} can be contacted at {}'.format(self.__name, self.__balance, self.__email)

seever = Customer('Seever Sarkawt', 'sivar@test.com', 100)
seever.set_balance(400)
print(seever.toString())

kate = Customer('Kate Smith', 'ksmith@test.com', 456)
print(kate.toString())