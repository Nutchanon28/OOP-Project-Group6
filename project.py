from PaymentDetail import PaymentDetail
class Project:
    
    id_counter = 1

    def __init__(
            self, project_creator
    ):
        self.id = Project.id_counter
        Project.id_counter += 1
        self.__project_name = ""
        self.__category = ""
        self.__project_image = ""
        self.__project_duration = ""
        self.__pledge_goal = 1
        self.__project_detail = ""
        self.__project_creator = project_creator
        self.__pledge_rewards = []
        self.__pleadge_backers = []
        self.__updates = []
        self.__backings = []

    def __init__(
        self, project_name, category, project_image, project_duration, project_detail, project_creator
    ):
        self.id = Project.id_counter
        Project.id_counter += 1

        self.__project_name = project_name
        self.__category = category
        self.__project_image = project_image
        self.__project_duration = project_duration
        self.__pledge_goal = 1
        self.__project_detail = project_detail
        self.__project_creator = project_creator
        self.__pledge_rewards = []
        self.__pleadge_backers = []
        self.__updates = []
        self.__backings = []
        self.__payment_detail = PaymentDetail("", "", "", "", "", "", "FLORIDA", "", "", "", "BANKOK BANK")

    def get_project_detail(self):
        project_detail = {
            "name": self.__project_name,
            "image": self.__project_image,
            "detail": self.__project_detail,
            "creator": self.__project_creator
        }
        # creator_detail = self.__project_creator.get_creator_detail() # require Project to have User as an attribute
        # project need to keep user's id instead of creator instance


        return {
            "project_detail": project_detail
        }
    
    def get_pledge_reward_detail(self):
        reward_detail_list = []
        for reward in self.__pledge_rewards:
            reward_detail_list.append(reward.get_reward_detail())

        return reward_detail_list

    def get_creator_detail(self):
        pass

    def edit_project(self, project_name, category, project_image, pledge_duration):
        self.project_name = project_name
        self.__category = category
        self.project_image = project_image
        self.project_duration = pledge_duration
        
    def print_project(self):
        print(f"project name: {self.__project_name}")
        print(f"project category: {self.__category}")
        print(f"pledge duration: {self.__project_duration}")
        print(f"project image: {self.__project_image}")
        print(f"pledge goal: {self.__pledge_goal}")
        print(f"project detail: {self.__project_detail}")
        print("pledge reward:")
        for reward in self.__pledge_rewards:
            tmp = vars(reward)
            print(', '.join("%s: %s" % item for item in tmp.items()))


    def set_reward_shipping(self, estimated_delivery, ships_to, old_reward_shipping):
        pass

    def set_pledge_rewards(self, reward_goal, reward_name, reward_detail, max_reward_backers, reward_include, old_pledge_reward):
        pass

    def set_funding_goal(self, goal):
        self.pledge_goal = goal

    def verify_creator_detail(self, legal_first_name, legal_last_name, email_address, date_of_birth, home_address, city, state, postal_code, phone_number):
        pass

    def create_comment(self, sending_time, text, writer):
        pass

    def create_update(self, update_title, update_creator, update_detail, update_image):
        pass

    def add_reward(self, reward):
        self.__pledge_rewards.append(reward)

    def get_reward_from_id(self, id):
        for reward in self.__pledge_rewards:
            print(f"id = {id} reward_id = {reward.id}")
            if reward.id == id:
                return reward
            
    def set_payment_detail(self, legal_first_name, legal_last_name, email_address,
                 date_of_birth, home_address, city, state, postal_code, phone_number, account_number, bank):
        self.__payment_detail = PaymentDetail(legal_first_name, legal_last_name, email_address,
                 date_of_birth, home_address, city, state, postal_code, phone_number, account_number, bank)

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
    def payment_detail(self):
        return self.__payment_detail
    
    def set_description(self, new_description):

        def is_valid_description(description):
            return len(description) < 600

        if isinstance(new_description, str) and is_valid_description(new_description):
            self.__project_detail = new_description
    
    @project_name.setter
    def project_name(self, new_name):
        if isinstance(new_name, str) and len(new_name) <= 100:
            self.__project_name = new_name
        else:
            print("!!!!!Please enter a valid name.")

    @category.setter
    def category(self, new_category):
            self.__category = new_category

    @pledge_goal.setter
    def pledge_goal(self, new_pledge_goal):
        self.__pledge_goal = int(new_pledge_goal)

    @project_image.setter
    def project_image(self, new_image):

        def is_valid_image(image):
            """[image_size <= 200 MB and image_type in [allowed_file_type]"""
            return True

        if isinstance(new_image, str) and is_valid_image(new_image):
            self.__project_image = new_image
        else:
            print("!!!!!Please enter a valid image.")

    @project_detail.setter
    def project_detail(self, new_detail):
        self.set_description(new_detail)

    @project_duration.setter
    def project_duration(self, new_duration):

        def is_valid_duration(duration):
            return 1 <= duration <= 60
        if new_duration == "":
            new_duration = 0
        new_duration = int(new_duration)
        if is_valid_duration(new_duration):
            self.__project_duration = new_duration
        else:
            print("!!!!!Please enter a valid duration")