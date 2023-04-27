from project import Project
from user import User

class System:
    def __init__(self):
        self.__project_list = []
        self.__launched_projects = []
        self.__user_list = []

    def add_user(self, user):
        if isinstance(user, User):
            self.__user_list.append(user)

    def add_project(self, project):
        self.__project_list.append(project)

    # system's method (view project)
    def get_user_from_id(self, id):
        for user in self.__user_list:
            if user.id == id:
                return user
        return "user not found"
    
    # system's method (view project)
    def get_project_from_id(self, id):
        for project in self.__launched_projects:
            if project.id == id:
                return project
                # Rew
        """for project in self.__project_list:
            if project.id == id:
                return project"""
        return "project not found"
    
    def get_my_projects(self, creator_id):
        my_projects = []
        for project in self.__project_list:
            if project.project_creator.id == creator_id:
                my_projects.append(project)

        return my_projects

    def delete_project(self, project):
        if project in self.__project_list:
            self.__project_list.remove(project)

    def launch_project(self, project):
        if isinstance(project, Project):
            self.__launched_projects.append(project)

    def check_project_payment_detail(self, Project):
        pass

    def search_project(self, keyword, category):
        searched_projects = []
        for project in self.__launched_projects:
            print("---------------------")
            print(project.category)
            print(category)
            if keyword in project.project_name and (project.category == category or category == "all"):
                searched_projects.append(project)
        return searched_projects

    def create_notification(self):
        pass

    def get_project_list(self):
        pass

    def get_launched_projects(self):
        pass

    @property
    def project_list(self):
        return self.__project_list
    
    @property
    def user_list(self):
        return self.__user_list
    
    @property
    def launched_projects(self):
        return self.__launched_projects