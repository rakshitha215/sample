import calendar
month, day, year = map(int, input().split())
day_number = calendar.weekday(year, month, day)
print(calendar.day_name[day_number]                 )
print(calendar.month(2024, 2))
print(calendar.calendar(2024))
