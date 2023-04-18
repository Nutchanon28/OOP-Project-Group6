from backing import Backing
from address import Address
from creditcardtransaction import CreditCardTransaction

class User:
    id_counter = 1
    
    def __init__(self, gmail, password, name, avatar, biography, location, website):
        self.__id = User.id_counter
        User.id_counter += 1
        
        self.__gmail = gmail
        self.__password = password
        self.__name = name
        self.__avatar = avatar
        self.__biography = biography
        self.__location = location
        self.__website = website
        self.__address_list = []
        self.__creditcard_list = []

    def edit_account(self, gmail, password):
        self.gmail = gmail
        self.password = password

    def edit_profile(self, name, avatar, biography, location, website):
        self.name = name
        self.avatar = avatar
        self.biography = biography
        self.location = location
        self.website = website

    def create_address(self, country, address_nickname, full_name, address, city, phone_number):
        self.__address_list.append(Address(country, address_nickname, full_name, address, city, phone_number))

    def delete_address(self, id):
        for address in self.__address_list:
            if id == address.id:
                self.__address_list.remove(address)
                return "delete address successfully"

    def get_all_address(self):
        return self.__address_list
    
    def create_creditcard(self, country, cvc, expiration, card_number):
        self.__creditcard_list.append(CreditCardTransaction(country, cvc, expiration, card_number))

    def delete_creditcard(self, id):
        for creditcard in self.__creditcard_list:
            if id == creditcard.id:
                self.__creditcard_list.remove(creditcard)
                return "delete creditcard successfully"

    def get_all_creditcard(self):
        return self.__creditcard_list
    
    @property
    def id(self):
        return self.__id
    
    @property
    def gmail(self):
        return self.__gmail

    @property
    def password(self):
        return self.__password

    @property
    def name(self):
        return self.__name
    
    @property
    def avatar(self):
        return self.__avatar
    
    @property
    def biography(self):
        return self.__biography
    
    @property
    def location(self):
        return self.__location
    
    @property
    def website(self):
        return self.__website
    
    @property
    def address_list(self):
        return self.__address_list
    
    @property
    def creditcard_list(self):
        return self.__creditcard_list
    
    @gmail.setter
    def gmail(self, new_gmail):
        if isinstance(new_gmail, str) and "@" in new_gmail:
            self.__gmail = new_gmail
        else:
            print("!!!!!Please enter a valid gmail.")

    @password.setter
    def password(self, new_password):
        if isinstance(new_password, str):
            self.__password = new_password
        else:
            print("!!!!!Please enter a valid password.")

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print("!!!!!Please enter a valid name.")

    @avatar.setter
    def avatar(self, new_avatar):
        if isinstance(new_avatar, str):
            self.__avatar = new_avatar
        else:
            print("!!!!!Please enter a valid avatar.")

    @biography.setter
    def biography(self, new_biography):
        if isinstance(new_biography, str):
            self.__biography = new_biography
        else:
            print("!!!!!Please enter a valid biography.")

    @location.setter
    def location(self, new_location):
        if isinstance(new_location, str):
            self.__location = new_location
        else:
            print("!!!!!Please enter a valid location.")

    @website.setter
    def website(self, new_website):
        if isinstance(new_website, str):
            self.__website = new_website
        else:
            print("!!!!!Please enter a valid website.")
    
    def add_address(self, country, address_nickname, full_name, address, city, phone_number):
        new_address = Address(country, address_nickname, full_name, address, city, phone_number)
        self.__addresses.append(new_address)
        return "finished add address"
