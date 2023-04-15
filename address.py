class Address:
    id_counter = 1

    def __init__(self, country, address_nickname, full_name, address, city, phone_number):
        self.__id = Address.id_counter
        Address.id_counter += 1
        self.__country = country
        self.__address_nickname = address_nickname
        self.__full_name = full_name
        self.__address = address
        self.__city = city
        self.__phone_number = phone_number

    @property
    def id(self):
        return self.__id

    @property
    def country(self):
        return self.__country
    
    @property
    def address_nickname(self):
        return self.__address_nickname
    
    @property
    def full_name(self):
        return self.__full_name

    @property
    def address(self):
        return self.__address
    
    @property
    def city(self):
        return self.__city
    
    @property
    def phone_number(self):
        return self.__phone_number