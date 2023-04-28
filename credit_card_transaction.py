class CreditCardTransaction:
    id_counter = 1

    def __init__(self, country, cvc, expiration, card_number):
        self.id = CreditCardTransaction.id_counter
        CreditCardTransaction.id_counter += 1

        self.__country = country
        self.__cvc = cvc
        self.__expiration = expiration
        self.__card_number = card_number
        self.__money_left = 10000

    def edit_credit_card(self, country, cvc, expiration, card_number):
        self.__country = country
        self.__cvc = cvc
        self.__expiration = expiration
        self.__card_number = card_number

    @property
    def money_left(self):
        return self.__money_left
    
    @money_left.setter
    def money_left(self, new_amount):
        print("money left setter")
        if isinstance(new_amount, int) and new_amount >= 0:
            self.__money_left = new_amount

