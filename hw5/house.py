from person import Person
from address import Address

class House():
    def __init__(self, dict):
        self.dict = dict
        self.is_active = True
        # self.info_list = [self.owner, self.tenant, self.count_room, self.metraj, self.count_floor,
        #                   self.phone_number, self.address, self.rahn_cost, self.ejare_cost,
        #                   self.sell_cost, self.sell_or_ejare, self.hayat_metraj]

    @classmethod
    def add_house(cls):
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
        count_room = input("enter count of apartment's room: ")
        d1['count_room'] = count_room
        metraj = input("enter metraj: ")
        d1['metraj'] = metraj
        count_floor = input("how many floor does it have? ")
        d1['count_floor'] = count_floor
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

        hayat_metraj = input("what is hayat's metraj?")
        d1['hayat_metraj'] = hayat_metraj
        return cls(d1)

    def __repr__(self):
        return f"""owmner is {self.dict['owner']} and tenant is {self.dict['tenant']} home has {self.dict['count_room']} room
and {self.dict['metraj']} meter and has {self.dict['count_floor']} floor. address of home is {self.dict['address']}
and has {self.dict['hayat_metraj']} meter hayat and this is for {self.dict['sell_or_ejare']}"""

    def change_home_info(self, **kwargs):
        self.dict.update((k,v) for k,v in kwargs.items())
        return self.dict



