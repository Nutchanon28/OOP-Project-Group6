from backing import Backing
from address import Address
from comment import Comment
from notification import Notification
from credit_card_transaction import CreditCardTransaction

class User:
    id_counter = 1

    def __init__(self, gmail, password, name, avatar, biography, location, website):
        self.id = User.id_counter
        User.id_counter += 1

        self.__gmail = gmail
        self.__password = password
        self.__name = name
        self.__avatar = avatar
        self.__biography = biography
        self.__location = location
        self.__website = website
        self.__payment_methods = []
        self.__addresses = []
        self.__backings = []
        self.__notifications = []

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
            new_backing = Backing(self, project, pledge_reward, reward_goal, bonus_cost)
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
        backed_projects = []
        for backing in self.__backings:
            backed_projects.append(backing.project)
        return backed_projects
    
    @property
    def notifications(self):
        return self.__notifications
    
    def add_new_notification(self, new_notification):
        self.__notifications.append(new_notification)
        return "append notification success"
        
    @property
    def payment_methods(self):
        return self.__payment_methods
    
    @property
    def addresses(self):
        return self.__addresses
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def gmail(self):
        return self.__gmail
    
    @gmail.setter
    def gmail(self, gmail):
        self.__gmail = gmail
    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self, password):
        self.__password = password
    
    @property
    def avatar(self):
        return self.__avatar
    
    @avatar.setter
    def avatar(self, avatar):
        self.__avatar = avatar
    
    @property
    def biography(self):
        return self.__biography
    
    @biography.setter
    def biography(self, biography):
        self.__biography = biography
    
    @property
    def location(self):
        return self.__location
    
    @location.setter
    def location(self, location):
        self.__location = location
    
    @property
    def website(self):
        return self.__website
    
    @website.setter
    def website(self, website):
        self.__website = website

