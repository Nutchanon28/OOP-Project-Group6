from user import User
class Backer(User):
    def __init__(self, account, message, payment_method, name, avatar, biography, location, time_zone, vanity_url, website, addresses, following, followers, blocked):
        super().__init__(self, account, message, payment_method, name, avatar, biography, location, time_zone, vanity_url, website, addresses, following, followers, blocked)
        pass
    
    @property
    def message_log(self):
        return self.__message_log

    def contact_creator():
        pass
    
    def send_comment():
        pass
    
    def follow_cretor():
        pass
    
    def add_payment_method():
        pass
    