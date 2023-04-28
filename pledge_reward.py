class PledgeReward:
    id_counter = 1

    def __init__(
        self, reward_goal, reward_name, reward_detail, reward_left, reward_shipping
    ):
        self.id = PledgeReward.id_counter
        PledgeReward.id_counter += 1

        self.__reward_goal = reward_goal
        self.__reward_name = reward_name
        self.__reward_detail = reward_detail
        self.__reward_include = []
        self.__reward_left = reward_left
        self.__reward_shipping = reward_shipping

    def add_reward_include(self, include):
        self.__reward_include.append(include)

    def get_reward_detail(self):
        reward_detail = {
            "id": self.id,
            "reward_goal": self.__reward_goal,
            "reward_name": self.__reward_name,
            "reward_detail": self.__reward_detail,
            "reward_include": self.__reward_include,
            "reward_left": self.__reward_left,
            "reward_shipping": self.__reward_shipping
        }
        return reward_detail

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
    def reward_left(self):
        return self.__reward_left

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

    @reward_left.setter
    def reward_left(self, reward_left):
        self.__reward_left = reward_left

    @reward_shipping.setter
    def reward_shipping(self, shipping):
        self.__reward_shipping = shipping

