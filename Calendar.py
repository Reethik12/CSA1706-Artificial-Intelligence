#Calendar for given month and year
import calendar
year=int(input("Enter year: "))
month=int(input("Enter month(1-12): "))
print("\nCalendar for",month,"/",year)
print(calendar.month(year,month))
