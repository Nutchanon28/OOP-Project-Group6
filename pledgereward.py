class PledgeReward:
    def __init__(self, reward_goal, reward_name, reward_detail, reward_include, reward_backers, max_reward_backers, reward_shipping, reward_id = 0):
        
        self.__id = reward_id
        
        self.__reward_goal = reward_goal
        self.__reward_name = reward_name
        self.__reward_detail = reward_detail
        self.__reward_include = []
        self.__reward_backers = reward_backers
        self.__max_reward_backers = max_reward_backers
        self.__reward_shipping = reward_shipping

    def get_reward_detail(self):
        reward_detail = {
            "reward_goal": self.__reward_goal,
            "reward_name": self.__reward_name,
            "reward_detail": self.__reward_detail,
            "reward_include": self.__reward_include,
            "reward_backers": self.__reward_backers,
            "max_reward_backers": self.__max_reward_backers,
            "max_reward_backers": self.__max_reward_backers,
            "reward_shipping": self.__reward_shipping.get_detail()
        }

        return reward_detail
    
    def add_reward_include(self, include):
        self.__reward_include.append(include)

    @property
    def id(self):
        return self.__id

    @property
    def reward_goal(self):
        return self.__reward_goal
    
    @property
    def reward_name(self):
        return self.__reward_name
    
    @property
    def reward_detail(self):
        return self.__reward_detail
    
    @property
    def reward_include(self):
        return self.__reward_include
    
    @property
    def max_reward_backers(self):
        return self.__max_reward_backers
    
    @property
    def reward_backers(self):
        return self.__reward_backers
    
    @property
    def reward_shipping(self):
        return self.__reward_shipping
    
    @reward_goal.setter
    def reward_goal(self, goal):
        self.__reward_goal = goal
    
    @reward_name.setter
    def reward_name(self, name):
        self.__reward_name = name
    
    @reward_detail.setter
    def reward_detail(self, detail):
        self.__reward_detail = detail
    
    @reward_include.setter
    def reward_include(self, include):
        self.__reward_include = include

    @max_reward_backers.setter
    def max_reward_backers(self, backers):
        self.__max_reward_backers = backers
    
    @reward_backers.setter
    def reward_backers(self, backers):
        self.__reward_backers = backers
    
    @reward_shipping.setter
    def reward_shipping(self, shipping):
        self.__reward_shipping = shipping
    

    
    
    
