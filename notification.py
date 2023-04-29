
class Notification:
    def __init__(self, actor, project, title, detail):
        self.__actor = actor
        self.__project = project
        self.__title = title
        self.__detail = detail
        
    @property
    def actor(self):
        return self.__actor
    
    @property
    def project(self):
        return self.__project
        
    @property
    def title(self):
        return self.__title
        
    @property
    def detail(self):
        return self.__detail