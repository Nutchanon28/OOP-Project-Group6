class CreditCardTransaction:
    id_counter = 1

    def __init__(self, country, cvc, expiration, card_number):
        self.__id = CreditCardTransaction.id_counter
        CreditCardTransaction.id_counter += 1

        self.__country = country
        self.__cvc = cvc
        self.__expiration = expiration
        self.__card_number = card_number

    @property
    def id(self):
        return self.__id

    @property
    def country(self):
        return self.__country
    
    @property
    def cvc(self):
        return self.__cvc
    
    @property
    def expiration(self):
        return self.__expiration
    
    @property
    def card_number(self):
        return self.__card_number
