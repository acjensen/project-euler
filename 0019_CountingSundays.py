weeks = {
    1:	'Monday',
    2:	'Tuesday',
    3:	'Wednesdady',
    4:	'Thursday',
    5:	'Friday',
    6:	'Saturday',
    7:	'Sunday',
    8:	'error',
}
months = {
    1:	'January',
    2:	'February',
    3:	'March',
    4:	'April',
    5:	'May',
    6:	'June',
    7:	'July',
    8:	'August',
    9:	'September',
    10:	'October',
    11:	'November',
    12:	'December',
    13: 'error'
}

month = 1
year = 1901
dayCounterMonth = 1
dayCounterWeek = 1 # in 1901, week starts on Monday

daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]
total = 0
while year < 2000:
    if dayCounterWeek > 7:
        dayCounterWeek = 1
    if dayCounterMonth > daysInMonth[month]:
        month = month + 1
        dayCounterMonth = 1
    if month > 12:
        year = year + 1
        month = 1
        if (year%4 == 0 and year%100 != 0) or (year%400 == 0):
            # leap year
            daysInMonth = [0,31,29,31,30,31,30,31,31,30,31,30,31]
        else:
            daysInMonth = [0,31,28,31,30,31,30,31,31,30,31,30,31]

    print ('Date:', weeks[dayCounterWeek]+ ',', months[month], str(dayCounterMonth) + ',', year)
    if dayCounterMonth == 1 and dayCounterWeek == 7:
        #print 'Sunday fell on the first of the month!!'
        total += 1

    dayCounterMonth += 1
    dayCounterWeek += 1

print (total)
