def isBefore(date1, date2):
    return date1[0] < date2[0] or date1[1] < date2[1] or date1[2] < date2[2]

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    iterations = 0
    currentDate = (year1, month1, day1)
    endDate = (year2, month2, day2)

    while (isBefore(currentDate, endDate)):
            currentDate = getNextDay(currentDate)
            iterations += 1
    
    return iterations

def getNextDay(date):
    year = date[0]
    month = date[1]
    day = date[2]

    days_in_month = {
        1: 31,
        2: 29 if isLeapYear(year) else 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    day += 1

    if (day > days_in_month[month]):
        month += 1
        day = 1

    if (month > 12):
        year += 1
        month = 1

    return (year, month, day)



def isLeapYear(year):
    if (year % 100 == 0):
        if (year % 400 == 0):
            return True
        return False

    if (year %  4 is 0):
        return True

    return False

def testGetNextDay():
    assert(getNextDay((2019, 8, 24)) == (2019, 8, 25))
    assert(getNextDay((2019, 8, 24)) == (2019, 8, 25))
    assert(getNextDay((2019, 12, 31)) == (2020, 1, 1))
    assert(getNextDay((2020, 2, 28)) == (2020, 2, 29))
    assert(getNextDay((2021, 2, 28)) == (2021, 3, 1))

    print("Get Next Day Tests Pass")

def testLeapYears():
    assert(isLeapYear(2019) == False)
    assert(isLeapYear(2020) == True)
    assert(isLeapYear(2021) == False)
    assert(isLeapYear(2022) == False)
    assert(isLeapYear(2100) == False)
    assert(isLeapYear(2000) == True)


    print("Leap Year Tests Pass")


def testDaysBetweenDates():
    
    # test same day
    assert(daysBetweenDates(2017, 12, 30,
                              2017, 12, 30) == 0)
    # test adjacent days
    assert(daysBetweenDates(2017, 12, 30, 
                              2017, 12, 31) == 1)
    # test new year
    assert(daysBetweenDates(2017, 12, 30, 
                              2018, 1,  1)  == 2)
    # test full year difference
    assert(daysBetweenDates(2012, 6, 29,
                              2013, 6, 29)  == 365)
    
    print("Days Between Dates Tests Pass")

testDaysBetweenDates()