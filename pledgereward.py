class PledgeReward:
    def __init__(
        self, reward_goal, reward_name, reward_detail, reward_include, reward_left
    ):
        self.__reward_goal = reward_goal
        self.__reward_name = reward_name
        self.__reward_detail = reward_detail
        self.__reward_include = reward_include
        self.__reward_backers = []
        self.__reward_left = reward_left

    def get_reward_detail(self):
        reward_detail = {
            "reward_goal": self.__reward_goal,
            "reward_name": self.__reward_name,
            "reward_detail": self.__reward_detail,
            "reward_include": self.__reward_include,
            "reward_left": self.__reward_left,
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
    def reward_backers(self):
        return self.__reward_backers

    @property
    def reward_left(self):
        return self.__reward_left

    # @reward_left
