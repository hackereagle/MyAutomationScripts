
class MonthMaxDay:
    #def __init__(self, isLeapYear):
    #    if isLeapYear == True:
    #        self.mMonthMaxDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #    else:
    #        self.mMonthMaxDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, year):
        if (year % 4) == 0:
            isLeapYear = True
        else:
            isLeapYear = False
        
        if isLeapYear == True:
            self.mMonthMaxDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            self.mMonthMaxDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def GetMonthMaxDay(self, month):
        if month <= 12 and month > 0:
            return self.mMonthMaxDay[month - 1]

class TestMonthMaxDay:
    def TestLeepYearFebruary(self):
        print('\nTestMonthMaxDay.TestLeepYearFebruary')
        # ARRANGE
        
        # ACT
        #monthMaxDay = MonthMaxDay(True)
        monthMaxDay = MonthMaxDay(2020)
        maxDay = monthMaxDay.GetMonthMaxDay(2)
        print('Fabruary max day = ' + str(maxDay))

        if maxDay == 29:
            print('OK')
        else:
            print('FAIL')

    def TestNotLeepYearFebruary(self):
        print('\nTestMonthMaxDay.TestNotLeepYearFebruary')
        # ARRANGE
        
        # ACT
        #monthMaxDay = MonthMaxDay(False)
        monthMaxDay = MonthMaxDay(2023)
        maxDay = monthMaxDay.GetMonthMaxDay(2)
        print('Fabruary max day = ' + str(maxDay))

        if maxDay == 28:
            print('OK')
        else:
            print('FAIL')
