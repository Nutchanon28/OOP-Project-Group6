from backing import Backing
from address import Address
from comment import Comment
from notification import Notification
from credit_card_transaction import CreditCardTransaction

class User:
    id_counter = 1

    def __init__(self, gmail, password, name, avatar, location, biography, website):
        self.id = User.id_counter
        User.id_counter += 1

        self.__gmail = gmail
        self.__password = password
        self.__name = name
        self.__avatar = avatar
        self.__location = location
        self.__biography = biography
        self.__website = website
        self.__payment_methods = []
        self.__addresses = []
        self.__backings = []
        self.__notifications = []

    def edit_account(self, gmail, old_password, new_password):
        if old_password == self.__password:
            if new_password != "":
                self.__password = new_password
            self.gmail = gmail

    def edit_profile(self, name, avatar, biography, location, website):
        self.name = name
        self.avatar = avatar
        self.biography = biography
        self.location = location
        self.website = website

    def create_address(self, country, address_nickname, full_name, address, city, phone_number):
        self.__addresses.append(Address(country, address_nickname, full_name, address, city, phone_number))

    def delete_address(self, id):
        for address in self.__addresses:
            if id == address.id:
                self.__addresses.remove(address)
                return "delete address successfully"
    
    def add_payment_method(self, country, cvc, expiration, card_number):
        self.__payment_methods.append(CreditCardTransaction(country, cvc, expiration, card_number))

    def delete_payment_method(self, id):
        for creditcard in self.__payment_methods:
            if id == creditcard.id:
                self.__payment_methods.remove(creditcard)
                return "delete creditcard successfully"
    
    # user's method (view project)
    def get_creator_detail(self):
        # creator (User) is keep in System, but also here ??
        creator_detail = {
            "name": self.__name,
            "avatar": self.__avatar,
            "biography": self.__biography,
            "location": self.__location,
            "website": self.__website
        }
        return creator_detail

    def back_project(self, project, credit_card, pledge_reward, bonus_cost):
        reward_goal = 0
        if pledge_reward != "reward not found":
            reward_goal = pledge_reward.reward_goal
        if credit_card.money_left >= (reward_goal + bonus_cost):
            new_amount = credit_card.money_left - reward_goal - bonus_cost
            credit_card.money_left = new_amount
            print(f"lose {reward_goal + bonus_cost} baht from {credit_card}")
            new_backing = Backing(self.id, project.id, pledge_reward, reward_goal, bonus_cost)
            self.__backings.append(new_backing)
            project.add_backing(new_backing, reward_goal)
            return "successful backing, money left = " + str(credit_card.money_left)
        else:
            return "insufficient fund"
        
    def add_address(self, country, address_nickname, full_name, address, city, phone_number):
        new_address = Address(country, address_nickname, full_name, address, city, phone_number)
        self.__addresses.append(new_address)
        return "finished add address"

    def add_payment_method(self, country, cvc, expiration, card_number):
        new_credit_card = CreditCardTransaction(country, cvc, expiration, card_number)
        self.__payment_methods.append(new_credit_card)
    
    def get_credit_card_from_id(self, id):
        for credit_card in self.__payment_methods:
            if credit_card.id == id:
                return credit_card
        return "credit card not found"

    def get_backed_project(self):
        # TODO: recursion bug
        backed_projects = []
        for backing in self.__backings:
            backed_projects.append(backing.project)
        return backed_projects
    
    def add_new_notification(self, new_notification):
        self.__notifications.append(new_notification)
        return "append notification success"
        
    @property
    def notifications(self):
        return self.__notifications
        
    @property
    def payment_methods(self):
        return self.__payment_methods
    
    @property
    def addresses(self):
        return self.__addresses

    @property  
    def name(self):
        return self.__name
    
    @property
    def gmail(self):
        return self.__gmail
    
    @property
    def password(self):
        return self.__password
    
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

    @gmail.setter
    def gmail(self, new_gmail):
        if isinstance(new_gmail, str) and "@" in new_gmail:
            self.__gmail = new_gmail
        else:
            print("!!!!!Please enter a valid gmail.")

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
