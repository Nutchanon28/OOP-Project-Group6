from update import Update
from comment import Comment
class Project:
    id_counter = 1

    def __init__(self, project_name, category, project_image, project_duration, project_detail, project_creator_id):
        self.id = Project.id_counter
        Project.id_counter += 1
    
class Project:

    def __init__(self, project_name, category, project_image, project_duration, project_creator):
        self.__project_name = project_name
        self.__category = category
        self.__project_image = project_image
        self.__project_duration = project_duration        
        self.__project_detail = project_detail
        self.__project_creator_id = project_creator_id # change project_creator to an id
        self.__pledge_rewards = []
        self.__pleadge_backers = []
        self.__updates = []
        self.__backings = []
        self.__comments = []
        
    def get_project_detail(self):
        pass
      
    def add_update(self, update_title, update_creator, update_detail, update_image):
        new_update = Update(update_title, update_creator, update_detail ,update_image)
        self.__updates.append(new_update)
        print(f"title: {new_update.update_title} \ncreator: {new_update.update_creator} \ndetail: {new_update.update_detail} \nimage: {new_update.update_image}")
        return "finished add update"
    def create_comment(self, sending_time, text, writer):
        pass

    def create_update(self, update_title, update_creator, update_detail, update_image):
        pass
    
    
    @property
    def pledge_reward(self):
        return self.__pleadge_rewards
    
    @property
    def comments(self):
        return self.__comments
    
    @property
    def pledge_goal(self):
        return self.__pledge_goal
    
    @comments.setter
    def comments(self, new_comment):
        if isinstance(new_comment, Comment):
            self.__comments.append(new_comment)
            
    def pledge_goal(self):
        return self.__pledge_goal
    
    @pledge_goal.setter
    def pledge_goal(self, new_pledge_goal):
        if isinstance(new_pledge_goal, int):
            self.__pledge_goal

    @property
    def project_name(self):
        return self.__project_name
    
    @property
    def category(self):
        return self.__category
    
    @property
    def project_image(self):
        return self.__project_image
    
    @property
    def project_duration(self):
        return self.__project_duration
    
    @property
    def project_creator(self):
        return self.__project_creator