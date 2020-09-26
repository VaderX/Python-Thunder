import datetime

def has_friday_13(month, year):
    day = datetime.datetime(year, month, 13).weekday()
    if(day == 4):
        return True
    return False

print(has_friday_13(3, 2020))
