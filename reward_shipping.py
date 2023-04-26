class RewardShipping:
    def __init__(self, estimated_delivery, ships_to, address, shipping_cost):
        self.__estimated_delivery = estimated_delivery
        self.__ships_to = ships_to
        self.__address = address
        self.__shipping_cost = shipping_cost

    def __str__(self):
        return f"{self.__estimated_delivery}\n{self.__ships_to}\n{self.__address}\n{self.__shipping_cost}"
    
    def get_detail(self):
        return {
            "estimated_delivery": self.__estimated_delivery,
            "ships_to": self.__ships_to,
            "address": self.__address,
            "shipping_cost": self.__shipping_cost
        }