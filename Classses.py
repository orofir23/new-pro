import datetime

'''def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month'''


class Duty:

    def __init__(self, name, count):
        self.__name = name
        self.__count = count


class DutyWeek:

    def __init__(self, member, duty_name, date):
        self.__member = member
        self.__duty_name = duty_name
        self.__date = date


class Member:
    # status
    baby = 1
    technician = 2
    senior_technician = 3
    manager_technician = 4

    # kind
    man = 32
    woman = 24

    #
    daily = 5
    weekly = 6

    def __init__(self, name, status, kind, departures, duties):
        self.__name = name
        self.__status = status
        self.__kind = kind
        self.__departures = departures
        self.__count_shift = 0
        self.__duties = duties[:]

    def get_status(self):
        if self.__status == self.baby:
            return "לא מוסמך"
        elif self.__status == self.technician:
            return "טכנאי"
        elif self.__status == self.senior_technician:
            return "טכנאי בכיר"
        elif self.__status == self.manager_technician:
            return "אחמש"

    def get_kind(self):
        return "גבר" if self.__kind == self.man else "אישה"

    def get_departures(self):
        return "יומיות" if self.__departures == self.daily else "חמשושים"

    def str(self):
        a = self.get_status()
        b = self.get_departures()
        txt = "name: " + self.__name + ", kind: " + self.get_kind()
        txt += ", status: " + a + ", departures: " + b
        return txt
