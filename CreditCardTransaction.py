class CreditCardTransaction:
    def __init__(self, country, cvc, expiration, card_number):
        self.__country = country
        self.__cvc = cvc
        self.__expiration = expiration
        self.__card_number = card_number

    def edit_credit_card(self, country, cvc, expiration, card_number):
        self.__country = country
        self.__cvc = cvc
        self.__expiration = expiration
        self.__card_number = card_number