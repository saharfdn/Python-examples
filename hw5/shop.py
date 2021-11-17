from person import Person
from address import Address


class Shop():
    def __init__(self, dict):
        self.dict = dict
        self.is_active = True
        # self.info_list = [self.owner, self.tenant, self.count_room, self.metraj, self.count_floor,
        #                   self.phone_number, self.address, self.rahn_cost, self.ejare_cost,
        #                   self.sell_cost, self.sell_or_ejare, self.hayat_metraj]

    @classmethod
    def add_shop(cls):
        d1 = {}
        print("please enter owner's info: ")
        owner = Person.add_person()
        d1['owner'] = owner
        while True:
            if owner.validation_address_email():
                break
            else:
                e = input("enter another email address: ")
                index = owner.info_list.index(owner.email)
                owner.info_list[index] = e
                owner.email = e
        while True:
            if owner.validation_id_code():
                break
            else:
                i = input("enter another identity code: ")
                index = owner.info_list.index(owner.id_code)
                owner.info_list[index] = i
                owner.id_code = i
        sell_or_ejare = input("sell/ejare? ")
        d1['sell_or_ejare'] = sell_or_ejare
        if sell_or_ejare.lower() != 'sell':
            print("please enter tenant's info: ")
            tenant = Person.add_person()
            d1['tenant'] = tenant
            while True:
                if tenant.validation_address_email():
                    break
                else:
                    e = input("enter another email address: ")
                    index = tenant.info_list.index(tenant.email)
                    tenant.info_list[index] = e
                    tenant.email = e
            while True:
                if tenant.validation_id_code():
                    break
                else:
                    i = input("enter another identity code: ")
                    index = tenant.info_list.index(tenant.id_code)
                    tenant.info_list[index] = i
                    tenant.id_code = i
        else:
            d1['tenant'] = None
        metraj = input("enter metraj: ")
        d1['metraj'] = metraj
        phone_number = input("enter apartment's phone number: ")
        d1['phone_number'] = phone_number
        print("please enter apartment address: ")
        address = Address.add_address()
        d1['address'] = address
        rahn_cost = input("enter rahn cost: ")
        d1['rahn_cost'] = rahn_cost
        ejare_cost = input("enter ejare cost: ")
        d1['ejare_cost'] = ejare_cost
        sell_cost = input("enter sell cost")
        d1[sell_cost] = sell_cost
        return cls(d1)

    def __repr__(self):
        return f"""owmner of shop is {self.dict['owner']} and {self.dict['metraj']} meter and address of shop
        is {self.dict['address']} and this is for {self.dict['sell_or_ejare']}"""

    def change_home_info(self, **kwargs):
        self.dict.update((k, v) for k, v in kwargs.items())
        return self.dict
#     def __init__(self, owner, tenant, metraj, phone_number, address, rahn_cost, ejare_cost
#                  , sell_cost, sell_or_ejare):
#         self.owner = owner
#         self.tenant = tenant
#         self.metraj = metraj
#         self.phone_number = phone_number
#         self.address = address
#         self.is_active = True
#         self.rahn_cost = rahn_cost
#         self.ejare_cost = ejare_cost
#         self.sell_cost = sell_cost
#         self.sell_or_ejare = sell_or_ejare
#         self.info_list = [self.owner, self.tenant, self.metraj,self.phone_number, self.address,
#                           self.rahn_cost, self.ejare_cost, self.sell_cost, self.sell_or_ejare]
#
#     @classmethod
#     def add_house(cls):
#         print("please enter owner's info: ")
#         owner = Person.add_person()
#         while True:
#             if owner.validation_address_email():
#                 break
#             else:
#                 e = input("enter another email address: ")
#                 index = owner.info_list.index(owner.email)
#                 owner.info_list[index] = e
#                 owner.email = e
#         while True:
#             if owner.validation_id_code():
#                 break
#             else:
#                 i = input("enter another identity code: ")
#                 index = owner.info_list.index(owner.id_code)
#                 owner.info_list[index] = i
#                 owner.id_code = i
#         print("please enter tenant's info: ")
#         tenant = Person.add_person()
#         while True:
#             if tenant.validation_address_email():
#                 break
#             else:
#                 e = input("enter another email address: ")
#                 index = tenant.info_list.index(tenant.email)
#                 tenant.info_list[index] = e
#                 tenant.email = e
#         while True:
#             if tenant.validation_id_code():
#                 break
#             else:
#                 i = input("enter another identity code: ")
#                 index = tenant.info_list.index(tenant.id_code)
#                 tenant.info_list[index] = i
#                 tenant.id_code = i
#         metraj = input("enter metraj: ")
#         phone_number = input("enter store's phone number: ")
#         print("please enter store's address: ")
#         address = Address.add_address()
#         rahn_cost = input("enter rahn cost: ")
#         ejare_cost = input("enter ejare cost: ")
#         sell_cost = input("enter sell cost")
#         sell_or_ejare = input("sell/ejare? ")
#         return cls(owner, tenant, metraj, phone_number,
#                    address, rahn_cost, ejare_cost, sell_cost, sell_or_ejare)
#
#     def __repr__(self):
#         return f"""owmner of shop is {self.owner} and {self.metraj} meter and address of shop
# is {self.address} and this is for {self.sell_or_ejare}"""
#
#     def change_home_info(self, **kwargs):
#         # this is like above
#         pass