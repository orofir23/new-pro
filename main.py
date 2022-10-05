import datetime
from Classses import Member, Duty
from openpyxl import Workbook, load_workbook


def is_duty_exist(duties, name):
    for duty in duties:
        if name == duty:
            return duty.get_loc()
    return -1


def start_day():
    week = int(input("לאיזה שבוע תרצה להכין את הפוטנציאל -->  "))
    dt = datetime.datetime.now()
    dt += datetime.timedelta(weeks=week)
    start = dt - datetime.timedelta(days=dt.weekday() + 1)
    return start.date()


def end_day(week):
    end = start_day(week) + datetime.timedelta(days=7)
    return end.date()


def init_excel(members, duties):
    days = ["ראשון", "שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת"]
    path = r'EXTRA\‏‏‏‏potential - copy.xlsx'
    wb = load_workbook(path)
    ws_weekly = wb['פוטנציאל שבועי מאסטר']
    date = start_day()
    for i in range(7):
        cell = chr(ord('I') + i) + '12'
        print((date + datetime.timedelta(days=i)).strftime("%d.%m"))
        ws_weekly[cell].value = (date + datetime.timedelta(days=i)).strftime("%d.%m") + " " + days[i]
    wb.save(path)

    ws_yearly = wb['פוטנציאל 2022']
    ver_char = 3
    while ws_yearly['A' + str(ver_char)].value.date() != date:
        ver_char += 1
    print('A' + str(ver_char))

    hor_char = 'D'
    for member in members:
        hor_char = chr(ord(hor_char) + 1)
        for i in range(7):
            duty_name = ws_yearly[hor_char + str(ver_char + i)].value
            loc = is_duty_exist(duties, duty_name)
            if duty_name != "" and loc != -1:
                ws_weekly['H' + loc] =


def init_members(members):
    path = r'EXTRA\members.txt'
    with open(path, 'r', encoding='utf-8') as f:
        str_member = f.readline()
        while str_member != '' and str_member != '\n':
            str_member = str_member.rsplit(",")
            name = str_member[0]
            kind = Member.man if str_member[1] == "גבר" else Member.woman
            if str_member[2] == "לא מוסמך":
                status = Member.baby
            elif str_member[2] == "טכנאי":
                status = Member.technician
            elif str_member[2] == "טכנאי בכיר":
                status = Member.senior_technician
            elif str_member[2] == "אחמש":
                status = Member.manager_technician
            departures = Member.daily if str_member[3] == "יומיות" else Member.weekly
            members.append(Member(name, status, kind, departures))
            str_member = f.readline()

    for member in members:
        print(member.str())
    print("---------------------------------------------------------------")


def init_duties(duties):
    path = r'EXTRA\duties.txt'
    with open(path, 'r', encoding='utf-8') as f:
        str_duty = f.readline()
        loc = 0
        while str_duty != '' and str_duty != '\n':
            str_duty = str_duty.rsplit(" - ")
            name = str_duty[0]
            count = str_duty[1]
            duties.append(Duty(name, count, loc))
            loc += 1
            str_duty = f.readline()

    for duty in duties:
        print(duty.str())
    print("---------------------------------------------------------------")


def main():
    duties = []
    init_duties(duties)
    members = []
    init_members(members)
    init_excel(members, duties)


if __name__ == "__main__":
    main()
