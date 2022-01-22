

class MonthMaxDay:
    def __init__(self, isLeapYear):
        if isLeapYear == True:
            self.mMonthMaxDay = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        else:
            self.mMonthMaxDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def GetMonthMaxDay(self, month):
        if month <= 12 and month > 0:
            return self.mMonthMaxDay[month - 1]

# global variable
monthMaxDay = MonthMaxDay(False)

def IsCorrectDayFormat(day):
    strs = day.split('.')
    
    isThreeEle = False
    length = len(strs)
    if length == 3:
        isThreeEle = True
    else:
        isThreeEle = False

    isMonthReasonable = False
    month = int(strs[1])
    if month > 0 and month <= 12:
        isMonthReasonable = True
    else:
        isMonthReasonable = False

    isDayReasonable = False
    maxDay = monthMaxDay.GetMonthMaxDay(month)
    day = int(strs[2])
    if day > 0 and day <= maxDay:
        isDayReasonable = True
    else:
        isDayReasonable = False

    return isThreeEle and isMonthReasonable and isDayReasonable


class Date:
    def __init__(self, date):
        dateArray = date.split('.')
        self.mYear = int(dateArray[0])
        self.mMonth = int(dateArray[1])
        self.mDay = int(dateArray[2])

    #def __init__(self, year, month, day):
    #    # TODO: need checking is correct format
    #    self.mYear = year
    #    self.mMonth = month
    #    self.mDay = day

    def GetYear(self):
        return self.mYear

    def GetMonth(self):
        return self.mMonth

    def GetDay(self):
        self.mDay

    def AddDay(self, day):
        if day < 31:
            #ret = Date(self.mYear, self.mMonth, self.mDay)
            ret = Date(self.ToString())
            ret.mDay = self.mDay + day
            if ret.mDay > monthMaxDay.GetMonthMaxDay(self.mMonth):
                ret.mMonth = self.mMonth + 1
                ret.mDay = ret.mDay - monthMaxDay.GetMonthMaxDay(self.mMonth)
            return ret
        else:
            print('Input day too large!')
            return self

    def ToString(self):
        return str(self.mYear) + '.' + '{:02d}'.format(self.mMonth) + '.' + '{:02d}'.format(self.mDay)

    def IsBiggerThanDay_str(self, day):
        isBigger = False
        dateArray = day.split('.')
        _year = int(dateArray[0])
        _month = int(dateArray[1])
        _day = int(dateArray[2])
        if self.mMonth > _month:
            isBigger = True
        else:
            if self.mDay > _day:
                isBigger = True
        return isBigger

    def IsBiggerThanDay_Date(self, day):
        isBigger = False
        if self.mMonth > day.GetMonth():
            isBigger = True
        else:
            if self.mDay > day.GetDay():
                isBigger = True
        return isBigger

    def AssignClass_Date(self, date):
        self.mYear = date.GetYear()
        self.mMonth = date.GetMonth()
        self.mDay = date.GetDay()

    def AssignClass_str(self, date):
        temp = Date(date)
        self.mYear = temp.GetYear()
        self.mMonth = temp.GetMonth()
        self.mDay = temp.GetDay()


def CreateEvernoteToDoList(beginDay, endDay):
    if IsCorrectDayFormat(beginDay) and IsCorrectDayFormat(endDay):
        _beginDay = Date(beginDay)
        _endDay = _beginDay.AddDay(6)
        
        while _beginDay.IsBiggerThanDay_str(endDay) != True:
            click("1642860440444.png")
            wait(1)
        
            click("1642861196260.png")
            wait(1)
        
            click("1642861244399.png")
            wait(1)
    
            type(_beginDay.ToString() + '~' + _endDay.ToString() + ' To Do List')
            wait(1)
        
            click("1642861289557.png")
            wait(1)
        
            click("1642861410315.png")
            wait(1)

            # TODO: modify day

            _beginDay = _beginDay.AddDay(7)
            print(_beginDay.ToString())
            _endDay = _beginDay.AddDay(6)
    else:
        print('Please check date format!')


if __name__ == '__main__':
    CreateEvernoteToDoList('2022.04.04', '2022.04.10')
    
    # testing MonthMaxDay
    #test = MonthMaxDay(False)
    #print(test.GetMonthMaxDay(2))

    # testing IsCorrectDayFormat
    #print(IsCorrectDayFormat('2022.01.22'))

    # testing Date
    #date = Date('2022.01.22')
    #end = date.AddDay(10)
    #print(date.ToString())
    #print(end.ToString())


