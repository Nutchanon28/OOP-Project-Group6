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
    
    @property
    def name(self):
        return self.__name
        
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

