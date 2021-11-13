# File          : q1.py
# Author        : Snehal Khairnar
# Version       : v1.0
# Created Date  : 12/10/2021
# Description   : Class
# Licensing     : Snehal Khairnar, LYIT
# ----------------------------------
import datetime


# noinspection SpellCheckingInspection
class Student:
    raise_amount = 5

    # noinspection SpellCheckingInspection
    def __init__(self, fname, lname, age, pay):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.pay = pay

    def display(self):
        print("{0} {1} {2}".format('snehal', 'khairnar', 29))
        return self.fname, self.lname, self.age

    def raise_amt(self):
        # self.amount = amount
        self.pay = self.pay * self.raise_amount
        print("{0}".format(self.pay))
        return self.pay

    @staticmethod
    def is_workday(day):
        if day == 5 or day == 6:
            return False
        return True


if __name__ == "__main__":
    s1 = Student('Snehal', 'Khairnar', 23, 50000)
    s1.display()
    s1.raise_amt()
    date1 = datetime.date(2020, 6, 6)
    print(s1.is_workday(date1))
