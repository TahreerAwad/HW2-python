from datetime import *

class Date:
    def __init__(self, day, month , year):
        self.day = day
        self.month = month
        self.year = year

    def __repr__(self):
        s = '%d/%d/%04d' % (self.day, self.month, self.year)
        return s

    # order Method
    def order(self):
        d0 = date(self.year,1,1)
        d1 = date(self.year,self.month,(self.day)+1)
        delta = (d1 - d0)
        return str(delta.days) +', since ' + str(self.day) + '/' + str(self.month)\
               + ' is the ' + str(delta.days) +'th day in the year. '

    # addition Method
    def addition(self,d2):
        d0= date(self.year,self.month,self.day)
        d1 =d0 + timedelta(days=d2)
        return d1

    # substraction Date
    def substraction(d1,d4):
        print("the number of days between 2 dates:")
        return abs(d4.day - d1.day)


    # compsrison
    def compsrison(d1):
        if d1.day < 22:
            return True
        else :
            return False


# The  Output .................
# -----------------------------#

d1 = Date(23,12,2020)
print(d1)
print('-----------')
d3 = Date(15,2,2020)
print(d3.order())
print('-----------')
d4 = Date(18,6,1997)
print(d4)
print('-----------')
d2 = d1.addition(22)
print(d2)
print('-----------')
print(Date.substraction(d1,d4))
print('-----------')
print(Date.compsrison(d1))