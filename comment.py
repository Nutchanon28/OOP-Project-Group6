class Comment:
    def __init__(self, sending_time, text, writer):
        self.__sending_time = sending_time
        self.__text = text
        self.__writer = writer

    def get_comment_detail(self):
        comment_detail = {
            "sending_time": self.__sending_time,
            "text": self.__text,
            "writer": self.__writer
        }
        return comment_detail
