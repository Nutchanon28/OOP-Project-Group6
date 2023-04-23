from backing import Backing
from address import Address
from comment import Comment
from creditCardTransaction import CreditCardTransaction
class User:
    id_counter = 1
    
    def __init__(self, name, avatar, biography, location, website):
        self.id = User.id_counter
        User.id_counter += 1

        self.__name = name
        self.__avatar = avatar
        self.__biography = biography
        self.__location = location
        self.__website = website
        self.__backings = []
        self.__notifications = []
        self.__payment_methods = []
        self.__gmail = ""
        self.__password = ""
        self.__addresses = []
    
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
        if credit_card.money_left >= pledge_reward.reward_goal:
            new_amount = credit_card.money_left - pledge_reward.reward_goal - bonus_cost
            credit_card.money_left = new_amount
            print(f"lose {pledge_reward.reward_goal} bath from {credit_card}")
            new_backing = Backing(self.id, project, pledge_reward, pledge_reward.reward_goal, bonus_cost)
            self.__backings.append(new_backing)
            project.add_backing(new_backing)
            return "successful backing, money left = " + str(credit_card.money_left)
        else:
            return "insufficient fund"
 
    def add_address(self, country, address_nickname, full_name, address, city, phone_number):
        new_address = Address(country, address_nickname, full_name, address, city, phone_number)
        self.__addresses.append(new_address)
        return "finished add address"

    def create_address(self, country, address_nickname, full_name, address, city, phone_number):
        self.__address_list.append(Address(country, address_nickname, full_name, address, city, phone_number))
                
    def send_comment(self, project, ):
        self.__name
        new_comment = Comment("time_now", "text", self)
              
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
    def addresses(self):
        return self.__addresses