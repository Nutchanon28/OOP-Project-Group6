class User:
    def __init__(self, account, message, payment_method, name, avatar, biography, location, time_zone, vanity_url, website, addresses, following, followers, blocked, notification):
        self.__account = account
        self.__message = message
        self.__payment_method = payment_method
        self.__name = name
        self.__avatar = avatar
        self.__biography = biography
        self.__location = location
        self.__time_zone = time_zone
        self.__vanity_url = vanity_url
        self.__website = website
        self.__addresses = addresses
        self.__following = following
        self.__followers = followers
        self.__blocked = blocked
        self.__notification = notification
        
    @property
    def notification(self):
        return self.__notification
    
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

