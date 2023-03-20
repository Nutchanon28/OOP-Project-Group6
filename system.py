class System:
    def __init__(self, project_list, launched_projects, user_list):
        self.__project_list = project_list
        self.__launched_projects = launched_projects
        self.__user_list = user_list

    def delete_project(self, Project, user_password):
        pass

    def launch_project(self, Project):
        pass

    def check_project_payment_detail(self, Project):
        pass

    def search_project(self, keyword, category):
        pass

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
    def launched_projects(self):
        return self.__launched_projects