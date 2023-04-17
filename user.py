from backing import Backing
from address import Address
from comment import Comment
class User:
    id_counter = 1
    
    def __init__(self, id,  gmail, password, name, avatar, biography, location, website):
        self.id = User.id_counter
        User.id_counter += 1
        
        self.__id = id
        self.__gmail = gmail
        self.__password = password
        self.__payment_method = [] #list of creditcard
        self.__name = name
        self.__avatar = avatar
        self.__biography = biography
        self.__location = location
        self.__website = website
        self.__addresses = []
        self.__notifications = []
        self.__backings = []
    
    def edit_user(self, gmail, password, name, avatar, biography, location, vanity_url, website):
        self.__gmail = gmail
        self.__password = password
        self.__name = name
        self.__avatar = avatar
        self.__biography = biography
        self.__location = location
        self.__vanity_url = vanity_url
        self.__website = website
        
    def back_project(self, project, credit_card, pledge_reward, bonus_cost):
        # if make_payment(credit_card, pledge_reward.reward_goal) == "successful":
        if True:
            print(f"lose {pledge_reward.reward_goal} bath from {credit_card}")
            new_backing = Backing(self.name, project, pledge_reward, bonus_cost)
            self.__backings.append(new_backing)
            project.add_backing(new_backing)
            print("success backing")
        else:
            print("insufficient fund")
        
    def add_address(self, country, address_nickname, full_name, address, city, phone_number):
        new_address = Address(country, address_nickname, full_name, address, city, phone_number)
        self.__addresses.append(new_address)
        return "finished add address"

    def create_address(self, country, address_nickname, full_name, address, city, phone_number):
        self.__address_list.append(Address(country, address_nickname, full_name, address, city, phone_number))
                
    def send_comment(self, project, ):
        self.__name
        new_comment = Comment("time_now", "text", self)
              
    def add_payment_method(self):
        pass
    def save_credit_card(self):
        pass
    
    @property
    def notification(self):
        return self.__notification
    
    @property
    def addresses(self):
        return self.__addresses
    
    @property
    def id(self):
        return self.__id
