from user import User
class Creator(User):
    def __init__(self, account, message, payment_method, name, avatar, biography, location, time_zone, vanity_url, website, addresses, following, followers, blocked):
        super().__init__(self, account, message, payment_method, name, avatar, biography, location, time_zone, vanity_url, website, addresses, following, followers, blocked)
        pass
    
    @property
    def message(self):
        return self.__message
    
    @property
    def name(self):
        return self.__name
    
    @property
    def biography(self):
        return self.__biography
    
    @property
    def location(self):
        return self.__location
    
    def edit_project():
        pass
    
    def view_setting():
        pass
    
    def add_update():
        pass
    
    def delete_project():
        pass
    
     
