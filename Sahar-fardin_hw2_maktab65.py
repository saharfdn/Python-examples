import datetime


class OneTrip:
    def __init__(self):
        self.using_time = 0

    def use_card(self):
        self.using_time += 1
        if self.using_time > 1:
            print('You can not use this card! this is one trip card.')


class CreditCard:
    def __init__(self, credit):
        self.trip_price = 5
        self.credit = credit

    def use_card(self):
        if self.credit < self.trip_price:
            print('There is not enough credit, Please charge!')
        else:
            self.credit -= self.trip_price

    def charge(self, charge_amount):
        self.credit += charge_amount

    def show_credit(self):
        return f'remain credit is {self.credit}'


class TimeCreditCard(CreditCard):
    def __init__(self, credit, ex_date):
        super().__init__(credit)
        self.ex_date = ex_date

    def use_card(self):
        if datetime.datetime.now() > self.ex_date:
            print(f'There is {self.credit // self.trip_price} trip credit but it is out of date!Please get a new card')
        if self.credit < self.trip_price:
            print('There is not enough credit, Please charge!')
        else:
            self.credit -= self.trip_price


c1 = OneTrip()
c1.use_card()
c1.use_card()
c2 = TimeCreditCard(35, datetime.datetime(2021, 10, 19))
c2.use_card()
print(c2.show_credit())
print(c2.credit)
c3 = CreditCard(30)
print(c3.show_credit())
c3.charge(10 * c3.trip_price)
print(c3.show_credit())
