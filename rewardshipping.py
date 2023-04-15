class RewardShipping:
    def __init__(self, estimated_delivery, ships_to, address):
        self.__estimated_delivery = estimated_delivery
        self.__ships_to = ships_to
        self.__address = address

    @property
    def estimated_delivery(self):
        return self.__estimated_delivery

    @property
    def ships_to(self):
        return self.__ships_to

    @property
    def address(self):
        return self.__address