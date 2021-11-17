import apartmentt
import house
import shop
import pandas as pd
from csv import writer
from person import Person



class ReadFile():
    # information of files
    files = {'malek': {
        'path': 'malek.csv',
        'col_names': ['fname', 'lname', 'email', 'id_num', 'ph_num'],
        'sep': ',',
        'skiprows': 1
    }, 'house': {
        'path': 'house.csv',
        'col_names': ['owner', 'sell_or_ejare', 'tenant', 'count_room', 'metraj', 'count_floor', 'phone_number',
                      'address'
            , 'rahn_cost', 'ejare_cost', 'sell_cost', 'hayat_metraj'],
        'sep': ',',
        'skiprows': 1
    }, 'shop': {
        'path': 'shop.csv',
        'col_names': ['owner', 'sell_or_ejare', 'tenant', 'metraj', 'phone_number', 'address'
            , 'rahn_cost', 'ejare_cost', 'sell_cost'],
        'sep': ',',
        'skiprows': 1
    }, 'apartemant': {
        'path': 'apartemant.csv',
        'col_names': ['owner', 'sell_or_ejare', 'tenant', 'count_room', 'metraj', 'floor', 'count_floor',
                      'phone_number', 'address'
            , 'rahn_cost', 'ejare_cost', 'sell_cost', 'park'],
        'sep': ',',
        'skiprows': 1
    }}

    def __init__(self, path, skiprows=0, names=None):
        self.path = path
        self.data = pd.read_csv(self.path, skiprows=skiprows, names=names)

    def head(self, n=2):
        return self.data.head(n)

    # show number of samples and number of outliers
    def __str__(self):
        return f"Total Samples : {len(self.data)}"

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data.iloc[idx]

    # when we want to read files with their name
    @classmethod
    def from_name(cls, name):
        info = cls.files[name]
        return cls(info['path'], info['skiprows'], info['col_names'])

    #when we want to write files
    def add_info(self, file_name, info_list):
        with open(file_name, 'a') as f_object:
            writer_object = writer(f_object)

            # Pass the list as an argument into
            # the writerow()
            writer_object.writerow(info_list)

            # Close the file object
            f_object.close()


class MoshaverAmlak():
    """"
    this class used for search about house and shop and
    apartment information
    """

    @staticmethod
    def search_by_sell(object_list):
        list_of_sell = []
        for item in object_list:
            if item.dict['sell_or_ejare'] == 'sell':
                list_of_sell.append(item)
        return list_of_sell

    @staticmethod
    def search_by_ejare(object_list):
        list_of_ejare = []
        for item in object_list:
            if item.dict['sell_or_ejare'] == 'ejare':
                list_of_ejare.append(item)
        return list_of_ejare

    @staticmethod
    def search_by_metraj(object_list, user_metraj):
        list_of_user_metraj = []
        for item in object_list:
            if item.dict['metraj'] == user_metraj:
                list_of_user_metraj.append(item)
        return list_of_user_metraj

    @staticmethod
    def search_by_rahn_cost(object_list, user_rahn_cost):
        list_of_user_cost = []
        for item in object_list:
            if item.dict['rahn_cost'] == user_rahn_cost:
                list_of_user_cost.append(item)

        return list_of_user_cost

    @staticmethod
    def search_by_ejare_cost(object_list, user_ejare_cost):
        list_of_user_cost = []
        for item in object_list:
            if item.dict['ejare_cost'] == user_ejare_cost:
                list_of_user_cost.append(item)
        return list_of_user_cost

    @staticmethod
    def search_by_sell_cost(object_list, user_sell_cost):
        list_of_user_cost = []
        for item in object_list:
            if item.dict['sell_cost'] == user_sell_cost:
                list_of_user_cost.append(item)
        return list_of_user_cost


class Transaction():
    """"
    this class used for transaction between seller and buyer
    and update information of house and shop and apartment
    """
    def __init__(self, kharidar, malek, ex_date_t, date_t):
        self.kharidar = kharidar
        self.malek = malek
        self.ex_date_t = ex_date_t
        self.date_t = date_t

    @classmethod
    def add_transaction(cls, object):
        print("Please enter kharidar's info:")
        kharidar = Person.add_person()
        while True:
            if kharidar.validation_address_email():
                break
            else:
                e = input("enter another email address: ")
                index = kharidar.info_list.index(kharidar.email)
                kharidar.info_list[index] = e
                kharidar.email = e
        while True:
            if kharidar.validation_id_code():
                break
            else:
                i = input("enter another identity code: ")
                index = kharidar.info_list.index(kharidar.id_code)
                kharidar.info_list[index] = i
                kharidar.id_code = i
        # malek =input("Please enter malek's name: ")
        malek = object.dict['owner']
        date_t = input("please enter date of transaction: ")
        ex_date_t = input("please enter ex_date of transaction: ")
        return cls(kharidar, malek, ex_date_t, date_t)

    def ejare(self, object):
        if object.is_active:
            object.dict['sell_or_ejare'] = 'ejare'
            object.dict['tenant'] = self.kharidar
            object.is_active = False
        else:
            print("in melk ejare dade shode!")

    def sell(self, object):
        if object.is_active:
            object.dict['sell_or_ejare'] = 'sell'
            object.dict['owner'] = self.kharidar
            object.is_active = False
        else:
            print("in melk furukhte shode ast!")

    def __str__(self):
        if self.sell_or_ejare == 'ejare':
            return f"in melk ke motaalegh be {self.malek} bud be {self.kharidar} ejare dade shod."
        elif self.sell_or_ejare == 'sell':
            return f"in melk ke motaalegh be {self.malek} bud be {self.kharidar} furukhte shod."


f = ReadFile.from_name('house')
# h = house.House.add_house()
# f.add_info('house.csv', list(h.dict.values()))
# print(h.change_home_info(owner ='hosein rezaei'))
# f.add_info('house.csv', list(h.dict.values()))

object_list = []
# with this code we convert each line of files to object
for i in range(len(f)):
    a = f[i].to_dict()
    h = house.House(a)
    object_list.append(h)
print(object_list)
sell_or_ejare = input("sell/ejare? ")
if sell_or_ejare.lower() == 'sell':
    print(MoshaverAmlak.search_by_sell(object_list))
elif sell_or_ejare.lower() == 'ejare':
    print(MoshaverAmlak.search_by_ejare(object_list))
a = True
while a:
    malek = input("which person's house do you want to rent or buy? ")
    for i in object_list:
        if str(i.dict['owner']) == malek.lower():
            t = Transaction.add_transaction(i)
            a = False
            break
    else:
        print("there is not a house with this person")
        continue

for i in object_list:
    if i.dict['owner'] == str(t.malek) and sell_or_ejare.lower() == 'sell':
        t.sell(i)

    elif i.dict['owner'] == str(t.malek) and sell_or_ejare.lower() == 'ejare':
        print('a')
        t.ejare(i)


print("update of object list: ", object_list)

# f1 = ReadFile.from_name('malek')
# f2 = ReadFile.from_name('apartemant')
# # p = person.Person.add_person()
# # while True:
# #     if p.validation_address_email():
# #         break
# #     else:
# #         e = input("enter another email address: ")
# #         index = owner.info_list.index(owner.email)
# #         owner.info_list[index] = e
# #         p.email = e
# # while True:
# #     if p.validation_id_code():
# #         break
# #     else:
# #         i = input("enter another identity code: ")
# #         index = owner.info_list.index(owner.id_code)
# #         owner.info_list[index] = i
# #         p.id_code = i
# # f1.add_info('malek.csv', p.info_list)
#
# object_list = []
# a = apartmentt.Apartment.add_apartment()
# object_list.append((a))
# # f1.add_info('malek.csv', a.owner.info_list)
# # f2.add_info('apartemant.csv', list(a.dict.values))

