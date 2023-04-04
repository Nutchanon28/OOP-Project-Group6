class Message:
    def __init__(self, writer, text, sending_time):
        self.__writer = writer
        self.__text = text
        self.__sending_time = sending_time

    