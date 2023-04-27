from backing import Backing
from address import Address
from comment import Comment
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
            new_backing = Backing(self.id, project, pledge_reward, reward_goal, bonus_cost)
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
    def name(self):
        return self.__name
        
    @property
    def notifications(self):
        return self.__notifications
    
    @property
    def payment_methods(self):
        return self.__payment_methods
    
    @property
    def following(self):
        return self.__following
    
    @property
    def followers(self):
        return self.__followers
    
    @property
    def blocked(self):
        return self.__blocked
    
    @property
    def addresses(self):
        return self.__addresses
    
    def add_address(self, country, address_nickname, full_name, address, city, phone_number):
        pass

