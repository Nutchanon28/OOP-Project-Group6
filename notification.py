
class Notification:
    def __init__(self, title, detail):
        self.__title = title
        self.__detail = detail
        
    @property
    def title(self):
        return self.__title
        
    @property
    def detail(self):
        return self.__detail