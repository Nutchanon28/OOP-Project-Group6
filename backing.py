class Backing:
    def __init__(self, backer, project, reward_item, reward_cost, bonus_cost):
        self.__backer = backer
        self.__project = project
        self.__reward_item = reward_item
        self.__reward_cost = reward_cost
        self.__bonus_cost = bonus_cost

    @property
    def backer(self):
        return self.__backer

    @property
    def reward_item(self):
        return self.__reward_item

    @property
    def reward_cost(self):
        return self.__reward_cost
    
    @property
    def project(self):
        return self.__project

    @reward_cost.setter
    def reward_cost(self, value):
        if value >= 0:
            self.__reward_cost = value
        else:
            raise ValueError("Reward cost cannot be negative")

    @property
    def bonus_cost(self):
        return self.__bonus_cost

    @bonus_cost.setter
    def bonus_cost(self, value):
        if value >= 0:
            self.__bonus_cost = value
        else:
            raise ValueError("Bonus cost cannot be negative")
