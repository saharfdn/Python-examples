class Person:
    """"
    this class is used for create owners and buyer an seller and tenant and have two method for check user's info
    """
    def __init__(self, f_name, l_name, email, id_code, phone_number):
        self.first_name = f_name
        self.last_name = l_name
        self.email = email
        self.id_code = id_code
        self.phone_number = phone_number
        self.info_list = [self.first_name, self.last_name, self.email, self.id_code, self.phone_number]

    @classmethod
    def add_person(cls):
        first_name = input("enter your first name: ")
        last_name = input("enter your last name: ")
        id_code = input("enter your identity code: ")
        ph_num = input("enter your phone number: ")
        email = input("enter your email address: ")
        return cls(first_name, last_name, email, id_code, ph_num)

    def validation_address_email(self):
        if self.email[-4:] == '.com' and '@' in self.email:
            return True
        else:
            print("Email address is not correct!")
            return False

    def validation_id_code(self):
        if len(self.id_code) == 10:
            return True
        else:
            print("Id code is not correct!enter a 10 digit number")
            return False

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

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"