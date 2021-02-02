year = 2017
month = 1
day = 9

if (month == 1 or month == 2):
    year -= 1
    month += 12

y2 = (year % 100)
c = int(year / 100)

week_day = ( day + int((13*(month+1))/5) + y2 + int(y2/4) + int(c/4) - (2*c) ) % 7
out = int(week_day)
print(out)
