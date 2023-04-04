class Payment:
    def __init__(self, project_id, reward_item, reward_cost, bonus_cost, shipping_cost):
        self.__project_id = project_id
        self.__reward_item = reward_item
        self.__reward_cost = reward_cost
        self.__bonus_cost = bonus_cost
        self.__shipping_cost = shipping_cost

    