

class Person:
    def __init__(self, given_name, middle_name, last_name):
        self.__given_name = given_name
        self.__middle_name = middle_name
        self.__last_name = last_name
        self.__age = None
        self.__address = None

    def full_name(self):
        return f"{self.__given_name} {self.__middle_name} {self.__last_name}"

    def personal_info(self):
        return f"Full Name: {self.full_name()}\nAge: {self.get_age()}\nAddress: {self.get_address()}"

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_address(self, address):
        self.__address = address

    def get_address(self):
        return self.__address
