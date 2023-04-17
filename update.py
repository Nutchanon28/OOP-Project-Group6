class Update:
    def __init__(self, update_title, update_creator, update_detail, update_image, likes):
        self.__update_title = update_title
        self.__update_creator = update_creator
        self.__update_detail = update_detail
        self.__update_image = update_image
        self.__update_likes = 0
        
        
    @property
    def update_title(self):
        return self.__update_title
    
    @property
    def update_creator(self):
        return self.__update_creator
    
    @property
    def update_detail(self):
        return self.__update_detail
    
    @property
    def update_image(self):
        return self.__update_image
