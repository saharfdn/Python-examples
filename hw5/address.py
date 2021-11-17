class Address:
    """
    this class is used for creat house shop and apartments address

    """
    def __init__(self, city, street, p_number, postal_code):
        self.city = city
        self.street = street
        self.p_number = p_number
        self.postal_code = postal_code

    @classmethod
    def add_address(cls):
        city = input("enter city's name: ")
        street = input("enter street's name: ")
        p_number = input("enter pelak number: ")
        postal_code = input("enter postal code: ")
        return cls(city, street, p_number, postal_code)

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