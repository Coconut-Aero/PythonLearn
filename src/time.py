import time

t = time.time()
t = int(t)
totalSEC = int(t)
totalMIN = int(totalSEC / 60)
totalHOUR = int(totalMIN / 60)
totalDAY = int(totalHOUR / 24)
curreSEC = int(totalSEC % 60)
curreMIN = int(totalMIN % 60)
curreHOUR = int(totalHOUR % 24)
dayInMonth = 31
month = 1
year = 1970

while totalDAY >= dayInMonth:
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        totalDAY -= 31
        month += 1
    elif month == 4 or month == 6 or month == 9 or month == 11:
        totalDAY -= 30
        month += 1
    else:
        if year % 4 == 0 and year % 100 != 0 or (year % 400 == 0):
            totalDAY -= 29
            month += 1
        else:
            totalDAY -= 28
            month += 1
    if month == 13:
        month = 1
        year += 1

day = totalDAY + 1
print("Current time is ", year, "-", month, "-", day, " ", curreHOUR, ":", curreMIN, ":", curreSEC, " GMT")
