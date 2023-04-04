class Project:
    def __init__(self, project_image, project_name, project_detail, project_creator, pledge_goal, pledge_received, pledge_backers, pledge_duration, category, filters, pledge_rewards, risk_detail, question, update, community):
        self.__project_image = project_image
        self.__project_name = project_name
        self.__project_detail = project_detail
        self.__project_creator = project_creator
        self.__pledge_goal = pledge_goal
        self.__pledge_received = pledge_received
        self.__pledge_backers = pledge_backers
        self.__pledge_duration = pledge_duration
        self.__category = category
        self.__pledge_rewards = pledge_rewards
        self.__risk_detail = risk_detail
        self.__question = question
        self.__update = update
        self.__community = community

    def __init__(self, project_name, category, project_image, project_duration, project_creator):
        self.__project_name = project_name
        self.__category = category
        self.__project_image = project_image
        self.__project_duration = project_duration
        self.__project_creator = project_creator
        self.__pleadge_rewards = []
        self.__pleadge_backers = []
        self.__update = []

    def get_project_detail(self):
        pass

    def get_creator_detail(self):
        pass

    def edit_project(self, project_name, category, project_image, pledge_duration):
        pass

    def set_reward_shipping(self, estimated_delivery, ships_to, old_reward_shipping):
        pass

    def set_pledge_rewards(self, reward_goal, reward_name, reward_detail, max_reward_backers, reward_include, old_pledge_reward):
        pass

    def verify_creator_detail(self, legal_first_name, legal_last_name, email_address, date_of_birth, home_address, city, state, postal_code, phone_number):
        pass

    def create_comment(self, sending_time, text, writer):
        pass

    def create_update(self, update_title, update_creator, update_detail, update_image):
        pass

    @property
    def pledge_reward(self):
        return self.__pleadge_rewards
    
    @property
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