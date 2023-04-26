from backing import Backing
from address import Address
from comment import Comment
from creditCardTransaction import CreditCardTransaction
class User:
    id_counter = 1
    
    def __init__(self, gmail, password, name, avatar, biography, location, website):
        self.id = User.id_counter
        User.id_counter += 1
        
        self.__gmail = gmail
        self.__password = password
        self.__payment_methods = [] #list of creditcard
        self.__name = name
        self.__avatar = avatar
        self.__biography = biography
        self.__location = location
        self.__website = website
        self.__addresses = []
        self.__notifications = []
        self.__backings = []
            
    def add_address(self, country, address_nickname, full_name, address, city, phone_number):
        new_address = Address(country, address_nickname, full_name, address, city, phone_number)
        self.__addresses.append(new_address)
        return "finished add address"

    def create_address(self, country, address_nickname, full_name, address, city, phone_number):
        self.__address_list.append(Address(country, address_nickname, full_name, address, city, phone_number))
