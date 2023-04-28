class Notification:
    def __init__(self, sender, title, detail):
        self.__sender = sender
        self.__title = title
        self.__detail = detail
        
    @property
    def sender(self):
        return self.__sender
    
    @property
    def sender_name(self):
        return self.__sender.name
        
    @property
    def title(self):
        return self.__title
        
    @property
    def detail(self):
        return self.__detail