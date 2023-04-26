from pledgereward import PledgeReward
from update import Update
from comment import Comment
class Project:
    id_counter = 1

    def __init__(
        self,
        project_name,
        category,
        project_image,
        project_duration,
        project_detail,
        project_creator,
        pledge_goal
    ):
        self.id = Project.id_counter
        Project.id_counter += 1

        self.__project_name = project_name
        self.__category = category
        self.__project_image = project_image
        self.__project_duration = project_duration
        self.__project_detail = project_detail
        self.__project_creator = project_creator
        self.__pledge_goal = pledge_goal
        self.__pledge_received = 0
        self.__pledge_rewards = []
        self.__updates = []
        self.__backings = []
        self.__comments = []
    
    @property
    def pledge_reward(self):
        return self.__pleadge_rewards
    
    @property
    def comments(self):
        return self.__comments
    
    @property
    def pledge_goal(self):
        return self.__pledge_goal
            
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