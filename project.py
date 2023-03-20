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
        # self.__filters = filters # remove this attribute
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
        # self.__community = Community

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