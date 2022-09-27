import datetime
from Classses import Member, Duty
from openpyxl import Workbook, load_workbook


def start_day():
    week = int(input("לאיזה שבוע תרצה להכין את הפוטנציאל -->  "))
    dt = datetime.datetime.now()
    dt += datetime.timedelta(weeks=week)
    start = dt - datetime.timedelta(days=dt.weekday() + 1)
    return start.date()


def end_day(week):
    end = start_day(week) + datetime.timedelta(days=7)
    return end.date()


def init_excel():
    days = ["ראשון", "שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת"]
    wb = load_workbook(r'C:\python_ws\ITPOTENTIAL\EXTRA\‏‏‏‏potential - copy.xlsx')
    ws = wb['פוטנציאל שבועי מאסטר']
    date = start_day()
    for i in range(7):
        cell = chr(ord('I') + i) + '12'
        print((date + datetime.timedelta(days=i)).strftime("%d.%m"))
        ws[cell].value = (date + datetime.timedelta(days=i)).strftime("%d.%m") + " " + days[i]
    wb.save(r'C:\python_ws\ITPOTENTIAL\EXTRA\‏‏‏‏potential - copy.xlsx')

    ws = wb['פוטנציאל 2022']
    i = 3
    while ws['A' + str(i)].value.date() != date:
        i += 1
    print('A' + str(i))


def init_members():
    with open(r'C:\python_ws\ITPOTENTIAL\EXTRA\members.txt', 'r', encoding='utf-8') as f:
        members = []
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

'''def init_duties:
    with open(r'C:\python_ws\ITPOTENTIAL\EXTRA\duties.txt', 'r', encoding='utf-8') as f:
        duties = []
        str_duty = f.readline()
        while str_duty != '' and str_duty != '\n':
            str_duty = str_duty.rsplit(" - ")
            name = str_duty[0]
            count = str_duty[1]
            duties.append(Duty(name, count))
            str_duty = f.readline()

    for duty in duties:
        print(duty.str())
    print("---------------------------------------------------------------")'''

def main():
    init_excel()


if __name__ == "__main__":
    main()
