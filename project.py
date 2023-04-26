from credit_card_transaction import CreditCardTransaction
from pledge_reward import PledgeReward
from comment import Comment
from update import Update
from reward_shipping import RewardShipping

class Project:
    id_counter = 1

    def __init__(
        self,
        project_name,
        category,
        project_image,
        project_duration,
        project_creator,
        pledge_goal
    ):
        self.id = Project.id_counter
        Project.id_counter += 1

        self.__project_name = project_name
        self.__category = category
        self.__project_image = project_image
        self.__project_duration = project_duration
        self.__project_detail = ""
        self.__project_creator = project_creator
        self.__pledge_goal = pledge_goal
        self.__pledge_received = 0
        self.__pledge_rewards = []
        self.__updates = []
        self.__backings = []
        self.__comments = []
        self.__credit_card = None

    def add_backing(self, backing):
        self.__backings.append(backing)
        self.pledge_received = self.pledge_received + \
            backing.reward_cost + backing.bonus_cost
        backing.reward_item.reward_left = backing.reward_item.reward_left - 1

    def add_reward(
        self, reward_goal, reward_name, reward_detail, reward_left, estimated_delivery, ships_to
    ):
        new_shipping = RewardShipping(estimated_delivery, ships_to)
        new_reward = PledgeReward(
            reward_goal, reward_name, reward_detail, reward_left, new_shipping
        )
        self.__pledge_rewards.append(new_reward)

    def get_project_detail(self):
        project_detail = {
            "name": self.__project_name,
            "image": self.__project_image,
            "detail": self.__project_detail,
            "category": self.__category,
            "pledge_received": self.__pledge_received,
            "number_of_backers": len(self.__backings),
            "pledge_goal": self.__pledge_goal,
            "project_duration": self.__project_duration
        }
        creator_detail = self.__project_creator.get_creator_detail()

        pledge_rewards_list = [
            reward.get_reward_detail() for reward in self.__pledge_rewards
        ]
        updates_list = [update.get_update_detail()
                        for update in self.__updates]
        comments_list = [comment.get_comment_detail()
                         for comment in self.__comments]
        print(updates_list)

        return {
            "project_detail": project_detail,
            "creator_detail": creator_detail,
            "pledge_rewards": pledge_rewards_list,
            "updates": updates_list,
            "comments": comments_list,
        }

    def add_update(self, update_title, update_creator, update_detail, update_image):
        new_update = Update(update_title, update_creator,
                            update_detail, update_image)
        self.__updates.append(new_update)
        return "finished add update"

    def get_creator_detail(self):
        pass

    def edit_project(self, project_name, category, project_image, pledge_duration):
        self.project_name = project_name
        self.__category = category
        self.project_image = project_image
        self.project_duration = pledge_duration

    def set_reward_shipping(self, estimated_delivery, ships_to, old_reward_shipping):
        pass

    def create_comment(self, sending_time, text, writer):
        new_comment = Comment(sending_time, text, writer)
        self.__comments.append(new_comment)
        return "comment successful"

    def create_update(self, update_title, update_creator, update_detail, update_image):
        new_update = Update(update_title, update_creator, update_detail, update_image)
        self.__updates.append(new_update)
        # print(f"title: {new_update.update_title} \ncreator: {new_update.update_creator} \ndetail: {new_update.update_detail} \nimage: {new_update.update_image}")
        return "finished add update"
    
    def get_reward_from_id(self, id):
        for pledge_reward in self.__pledge_rewards:
            if pledge_reward.id == id:
                return pledge_reward
        return "reward not found"
    
    @property
    def project_detail(self):
        return self.__project_detail
    
    @project_detail.setter
    def project_detail(self, new_project_detail):
        if isinstance(new_project_detail, str):
            self.__project_detail = new_project_detail

    def get_reward_from_id(self, id):
        for reward in self.__pledge_rewards:
            print(f"id = {id} reward_id = {reward.id}")
            if reward.id == id:
                return reward

    def delete_reward(self, reward_id):
        for reward in self.__pledge_rewards:
            if reward.id == reward_id:
                self.__pledge_rewards.remove(reward)
                return f"remove reward with id {reward_id} success!"
            
    @property
    def pledge_rewards(self):
        return self.__pledge_rewards

    @property
    def pledge_goal(self):
        return self.__pledge_goal

    @property
    def comments(self):
        return self.__comments

    @comments.setter
    def comments(self, new_comment):
        if isinstance(new_comment, Comment):
            self.__comments.append(new_comment)

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

    @property
    def project_detail(self):
        return self.__project_detail

    @property
    def pledge_rewards(self):
        return self.__pledge_rewards

    @property
    def credit_card(self):
        return self.__credit_card

    @credit_card.setter
    def credit_card(self, new_credit_card):
        self.__credit_card = new_credit_card

    @project_detail.setter
    def project_detail(self, new_project_detail):
        if isinstance(new_project_detail, str):
            self.__project_detail = new_project_detail

    @project_name.setter
    def project_name(self, new_project_name):
        if isinstance(new_project_name):
            self.__project_name = new_project_name

    @category.setter
    def category(self, new_category):
        self.__category = new_category

    @pledge_goal.setter
    def pledge_goal(self, new_pledge_goal):
        self.__pledge_goal = int(new_pledge_goal)

    @project_image.setter
    def project_image(self, new_project_image):
        if isinstance(new_project_image, str):
            self.__project_image = new_project_image

    @project_duration.setter
    def project_duration(self, new_project_duration):
        self.__project_duration = int(new_project_duration)

    @property
    def pledge_received(self):
        return self.__pledge_received

    @pledge_received.setter
    def pledge_received(self, new_value):
        if isinstance(new_value, int) and new_value >= 0:
            self.__pledge_received = new_value