class Notification:
    def __init__(self, title, detail, sending_time):
        self.__title = title
        self.__detail = detail
        self.__sending_time = sending_time

    @property
    def title(self):
        return self.__title
    
    @property
    def detail(self):
        return self.__detail
    
    @property
    def sending_time(self):
        return self.__sending_time