from user import User
from project import Project

class System:
    def __init__(self):
        self.__project_list = []
        self.__launched_projects = []
        self.__user_list = []

    def delete_project(self, project_id):
        for project in self.__launched_projects:
            if project_id == project.id:
                self.__launched_projects.remove(project)
                return "remove successfully"

    def add_project(self, project_name, category, project_image, project_duration, project_detail, project_creator_id):
        self.__project_list.append(Project(project_name, category, project_image, project_duration, project_detail, project_creator_id))

    def add_project(self, project):
        self.__project_list.append(project)

    def launch_project(self, project):
        if isinstance(project, Project):
            self.__launched_projects.append(project)

    def add_user(self, gmail, password, name, avatar, biography, location, website):
        self.__user_list.append(User(gmail, password, name, avatar, biography, location, website))

    def add_user(self, user):
        if isinstance(user, User):
            self.__user_list.append(user)

    def get_user_by_id(self, id):
        for user in self.__user_list:
            if id == user.id:
                return user

    @property
    def project_list(self):
        return self.__project_list
    
    @property
    def launched_projects(self):
        return self.__launched_projects
    
    @property
    def user_list(self):
        return self.__user_list