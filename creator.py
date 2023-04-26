from user import User
from update import Update
class Creator(User):
    def __init__(self, name, avatar, biography, location, website):
        super().__init__(self, name, avatar, biography, location, website)
        pass
    
    def add_update(self, project, update_title, update_detail, update_image):
        new_update = Update(project, update_title, self, update_detail, update_image)
        project.updates.append(new_update)
        return new_update.get_update_detail
        
    
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
    
    def delete_project():
        pass
    
     
