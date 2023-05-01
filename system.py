from project import Project
from user import User
from notification import Notification

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
                # Rew: get creator's projects
        """for project in self.__project_list:
            if project.id == id:
                return project"""
        return "project not found"
    
    def get_project_in_project_list_from_id(self, id):
        for project in self.__project_list:
            print(f"{id} {project.id}")
            if project.id == id:
                return project

    def get_my_projects(self, creator_id):
        my_projects = []
        for project in self.__project_list:
            if project.project_creator.id == creator_id:
                my_projects.append(project)

        return my_projects

    def delete_project(self, project_id):
        for project in self.__project_list:
            if project_id == project.id:
                self.__project_list.remove(project)
                return "remove successfully"
        for project in self.__launched_projects:
            if project_id == project.id:
                self.__launched_projects.remove(project)
                return "remove successfully"

    def launch_project(self, project):
        if isinstance(project, Project):
            self.__launched_projects.append(project)
            
    def search_project(self, keyword, category):
        searched_projects = []
        for project in self.__launched_projects:
            print("---------------------")
            print(project.category)
            print(category)
            if keyword in project.project_name and (project.category == category or category == "all"):
                searched_projects.append(project)
        return searched_projects

    # This should be changed in some way, it's just wrong, so so wrong like, it's straight up sinning.
    # def create_notification(self, actor, type, project, amount, more_detail):
    #     if (type == "has backed"):
    #         new_notification = Notification(
    #             actor.name,
    #             project.project_name,
    #             "new backed items",
    #             "you have backed to '" + str(project.project_name) + "' for " + str(amount) + "Baht"
    #             )
    #     elif (type == "received"):
    #         new_notification = Notification(
    #             actor.name,
    #             project.project_name,
    #             "new received",
    #             "project '" + str(project.project_name) + "' receive " + str(amount) + "Baht" + "from '" + str(actor.name) 
    #             )
    #     elif (type == "post update"):
    #         new_notification = Notification(
    #             actor.name,
    #             project.project_name,
    #             "new update on project you backed",
    #             str(actor.name) + " have posted '" + str(more_detail) + "' on '" + str(project.project_name) +"'"
    #         )
    #     return new_notification
    
    def send_notification(self, send_to, new_notification):
        for user in send_to:
            user.add_new_notification(new_notification)
            print(user)
        print("added noti to user")
        return "send notification successful"
    
    @property
    def project_list(self):
        return self.__project_list

    @property
    def user_list(self):
        return self.__user_list

    @property
    def launched_projects(self):
        return self.__launched_projects

