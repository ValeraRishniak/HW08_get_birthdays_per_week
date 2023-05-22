import collections
from datetime import datetime, timedelta

USERS = collections.namedtuple("user", ["name", "birthday"])

monday_list_for_dict = []
tuesday_list_for_dict = []
wednesday_list_for_dict = []
thursday_list_for_dict = []
friday_list_for_dict = []


def get_birthdays_per_week(users):
    current_date = datetime.now().date() 
    plus_week = current_date + timedelta(days=7)
    for user in users:
        a = datetime.strptime(user.birthday, '%d.%m.%Y')
        new_a = a.replace(year=current_date.year)
        if new_a.date() >= current_date and new_a.date() < plus_week and datetime.weekday(new_a) == 0:
            monday_list_for_dict.append(user.name)
        elif new_a.date() >= current_date and new_a.date() < plus_week and datetime.weekday(new_a) == 1:
            tuesday_list_for_dict.append(user.name)
        elif new_a.date() >= current_date and new_a.date() < plus_week and datetime.weekday(new_a) == 2:
            wednesday_list_for_dict.append(user.name)
        elif new_a.date() >= current_date and new_a.date() < plus_week and datetime.weekday(new_a) == 3:
            thursday_list_for_dict.append(user.name)
        elif new_a.date() >= current_date and new_a.date() < plus_week and datetime.weekday(new_a) == 4:
            friday_list_for_dict.append(user.name)
        elif new_a.date() >= current_date and new_a.date() < plus_week and (datetime.weekday(new_a) == 5 or 6):
            monday_list_for_dict.append(user.name)
        else:
            continue

    mon = ''
    for i, el in enumerate(monday_list_for_dict):
        if i < len(monday_list_for_dict)-1:
            mon += str(el)
            mon += ', '
        else:
            mon += str(el)

    tue = ''
    for i, el in enumerate(tuesday_list_for_dict):
        if i < len(tuesday_list_for_dict)-1:
            tue += str(el)
            tue += ', '
        else:
            tue += str(el)

    wed = ''
    for i, el in enumerate(wednesday_list_for_dict):
        if i < len(wednesday_list_for_dict)-1:
            wed += str(el)
            wed += ', '
        else:
            wed += str(el)

    thur = ''
    for i, el in enumerate(thursday_list_for_dict):
        if i < len(thursday_list_for_dict)-1:
            thur += str(el)
            thur += ', '
        else:
            thur += str(el)

    fri = ''
    for i, el in enumerate(friday_list_for_dict):
        if i < len(friday_list_for_dict)-1:
            fri += str(el)
            fri += ', '
        else:
            fri += str(el)
 
    print("\n".join((f'Monday: {mon}', f'Tuesday: {tue}', f'Wednesday: {wed}', f'Thursday: {thur}', f'Friday: {fri}')))

if __name__ == '__main__':
    get_birthdays_per_week([USERS("Mick",     '22.05.1991'), 
                            USERS("Mayka",    '23.05.1992'), 
                            USERS("Mikha",    '24.07.1993'),
                            USERS("Oleg",     '25.05.1994'),
                            USERS("Vasyl",    '26.05.1995'),
                            USERS("Denis",    '27.05.1996'),
                            USERS("Georg",    '28.05.1997'),
                            USERS("Vova",     '29.05.1998'),
                            USERS("Kobieta",  '30.05.1999'),
                            USERS("Barbie",   '31.05.2000'),
                            USERS("Jenny",    '01.06.2001'),
                            USERS("Iren",     '02.06.2002'),
                            ])


