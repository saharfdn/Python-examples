class Address:
    def __init__(self, city, street, p_number, postal_code):
        self.city = city
        self.street = street
        self.p_number = p_number
        self.postal_code = postal_code

    def __repr__(self):
        return f"{self.city}-{self.street}-{self.p_number}-{self.postal_code}"

    def change_address(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'city':
                self.city = value
            elif key == 'street':
                self.street = value
            elif key == 'p_number':
                self.p_number = value
            elif key == 'postal_code':
                self.postal_code = value


a = Address('tabriz', '18', '333', '286')
a.change_address(city='tehran', street='12')
print(a)


class Person:
    def __init__(self, f_name, l_name, email, id_code, phone_number):
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.id_code = id_code
        self.phone_number = phone_number

    def validation_address_email(self):
        if self.email[-4:] == '.com' and '@' in self.email:
            print("The address is correct!")
        else:
            print("Enter another email address")

    def validation_id_code(self):
        if len(self.id_code) == 10:
            print("The id_code is correct!")
        else:
            print("It is'nt correct!")

    def change_info(self, **kwargs):
        for key, value in kwargs.items():
            if key == 'first_name':
                self.first_name = value
            elif key == 'last_name':
                self.last_name = value
            elif key == 'email':
                self.email = value
            elif key == 'id_code':
                self.id_code = value
            elif key == 'phone_number':
                self.phone_number = value

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Apartment():
    def __init__(self, owner, tenant, count_room, metraj, floor, count_floor, phone_number,
                 address, rahn_cost, ejare_cost, sell_cost, sell_or_ejare, park):
        self.owner = owner
        self.tenant = tenant
        self.count_room = count_room
        self.metraj = metraj
        self.floor = floor
        self.count_floor = count_floor
        self.phone_number = phone_number
        self.address = address
        self.is_active = True
        self.rahn_cost = rahn_cost
        self.ejare_cost = ejare_cost
        self.sell_cost = sell_cost
        self.sell_or_ejare = sell_or_ejare
        self.park = park

    def __repr__(self):
        return f"""owmner is {self.owner} home has {self.count_room} room
and {self.metraj} meter and has {self.count_floor} floor that is {self.floor}. address of home is {self.address}
and has {self.park} park place and this is for {self.sell_or_ejare}"""

    def change_home_info(self, **kwargs):
        # this is like above
        pass


class House():
    def __init__(self, owner, tenant, count_room, metraj, count_floor, phone_number,
                 address, rahn_cost, ejare_cost, sell_cost, sell_or_ejare, hayat_metraj):
        self.owner = owner
        self.tenant = tenant
        self.count_room = count_room
        self.metraj = metraj
        self.count_floor = count_floor
        self.phone_number = phone_number
        self.address = address
        self.is_active = True
        self.rahn_cost = rahn_cost
        self.ejare_cost = ejare_cost
        self.sell_cost = sell_cost
        self.sell_or_ejare = sell_or_ejare
        self.hayat_metraj = hayat_metraj

    def __repr__(self):
        return f"""owmner is {self.owner} home has {self.count_room} room
and {self.metraj} meter and has {self.count_floor} floor. address of home is {self.address}
and has {self.hayat_metraj} meter hayat and this is for {self.sell_or_ejare}"""

    def change_home_info(self, **kwargs):
        # this is like above
        pass


class Shop():
    def __init__(self, owner, tenant, metraj, phone_number, address, rahn_cost, ejare_cost
                 , sell_cost, sell_or_ejare):
        self.owner = owner
        self.tenant = tenant
        self.metraj = metraj
        self.phone_number = phone_number
        self.address = address
        self.is_active = True
        self.rahn_cost = rahn_cost
        self.ejare_cost = ejare_cost
        self.sell_cost = sell_cost
        self.sell_or_ejare = sell_or_ejare

    def __repr__(self):
        return f"""owmner of shop is {self.owner} and {self.metraj} meter and address of shop
is {self.address} and this is for {self.sell_or_ejare}"""

    def change_home_info(self, **kwargs):
        # this is like above
        pass


class MoshaverAmlak(House, Apartment, Shop):
    def __init__(self):
        super(House, self).__init__()
        super(Apartment, self).__init__()
        super(Shop, self).__init__()

    @staticmethod
    def search_by_sell(self, object_list):
        list_of_sell = []
        for item in object_list:
            if item.sell_or_ejare == 'sell':
                list_of_sell.append(item)
        return list_of_sell

    @staticmethod
    def search_by_ejare(self, object_list):
        list_of_ejare = []
        for item in object_list:
            if item.sell_or_ejare == 'ejare':
                list_of_ejare.append(item)
        return list_of_ejare

    @staticmethod
    def search_by_metraj(self, object_list, user_metraj):
        list_of_user_metraj = []
        for item in object_list:
            if item.metraj == user_metraj:
                list_of_user_metraj.append(item)
        return list_of_user_metraj

    @staticmethod
    def search_by_rahn_cost(self, object_list, user_rahn_cost):
        list_of_user_cost = []
        for item in object_list:
            if item.rahn_cost == user_rahn_cost:
                list_of_user_cost.append(item)

        return list_of_user_cost

    @staticmethod
    def search_by_ejare_cost(self, object_list, user_ejare_cost):
        list_of_user_cost = []
        for item in object_list:
            if item.ejare_cost == user_ejare_cost:
                list_of_user_cost.append(item)
        return list_of_user_cost

    @staticmethod
    def search_by_sell_cost(self, object_list, user_sell_cost):
        list_of_user_cost = []
        for item in object_list:
            if item.sell_cost == user_sell_cost:
                list_of_user_cost.append(item)
        return list_of_user_cost


class Transaction(House, Apartment, Shop):
    def __init__(self, kharidar, malek, ex_date_t, date_t):
        super(House, self).__init__()
        super(Apartment, self).__init__()
        super(Shop, self).__init__()
        self.kharidar = kharidar
        self.malek = malek
        self.ex_date_t = ex_date_t
        self.date_t = date_t

    def ejare(self):
        if self.is_active:
            self.sell_or_ejare = 'ejare'
            self.is_active = False
        else:
            print("in melk ejare dade shode!")

    def sell(self):
        if self.is_active:
            self.sell_or_ejare = 'sell'
            self.is_active = False
        else:
            print("in melk furukhte shode ast!")

    def __str__(self):
        if self.sell_or_ejare == 'ejare':
            return f"in melk ke motaalegh be {self.malek} bud be {self.kharidar} ejare dade shod."
        elif self.sell_or_ejare == 'sell':
            return f"in melk ke motaalegh be {self.malek} bud be {self.kharidar} furukhte shod."

#
#
#
#
# a = Address('tab', 'mad', '2', '123')
# print(a)
# a.change_address('teh', 'ma', '23', '234')
# print(a)
# b = Person('sahar', 'fardin', 'sahar@gmail.com', '2860293744', '3245')
# b.validation_address_email()
# b.validation_id_code()
