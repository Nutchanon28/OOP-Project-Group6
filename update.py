class Update:
    def __init__(self, update_title, update_creator, update_detail, update_image, likes):
        self.__update_title = update_title
        self.__update_creator = update_creator
        self.__update_detail = update_detail
        self.__update_image = update_image
        self.__likes = 0

    def get_update_detail(self):
        update_detail = {
            "project": self.__project,
            "update_title": self.__update_title,
            "update_creator": self.__update_creator,
            "update_detail": self.__update_detail,
            "update_image": self.__update_image,
            "likes": self.__likes,
        }
        return update_detail