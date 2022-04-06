

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
        #print(self.mYear)
        #print(self.mMonth)
        #print(self.mDay)

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

    def IsSmallerThanDay_str(self, day):
        isSmaller = False
        dateArray = day.split('.')
        _year = int(dateArray[0])
        _month = int(dateArray[1])
        _day = int(dateArray[2])
        if self.mMonth < _month:
            isSmaller = True
        elif self.mMonth == _month:
            if self.mDay < _day:
                isSmaller = True
        return isSmaller

    def IsSmallerThanDay_Date(self, day):
        isSmaller = False
        if self.mMonth < day.GetMonth():
            isSmaller = True
        elif self.mMonth == day.GetMonth():
            if self.mDay < day.GetDay():
                isSmaller = True
        return isSmaller

    def AssignClass_Date(self, date):
        self.mYear = date.GetYear()
        self.mMonth = date.GetMonth()
        self.mDay = date.GetDay()

    def AssignClass_str(self, date):
        temp = Date(date)
        self.mYear = temp.GetYear()
        self.mMonth = temp.GetMonth()
        self.mDay = temp.GetDay()


originDay = ["1642946701374.png", "1642946760378.png", "1642946788844.png", "1642946800414.png", "1642946823444.png", "1642946837403.png", "1642946847284.png"]
def ModifyDatesInNoteBeginDate(date):
    print(date.ToString())
    _year = date.GetYear()
    _month = date.GetMonth()
    _day = date.mDay
    for i in range(7):
        print(i)
        pos = find(originDay[i])
        click(pos)
        
        wait(1)
        type(Key.HOME)
        wait(1)
        for j in range(5):
            type(Key.DELETE)
        
        newDay = '{:02d}'.format(_month) + '/' + '{:02d}'.format(_day)
        type(newDay)

        wheel(pos, Button.WHEEL_DOWN, 2)
        wait(1)

        _day = _day + 1
        if _day > monthMaxDay.GetMonthMaxDay(_month):
            _month = _month + 1
            _day = _day - monthMaxDay.GetMonthMaxDay(_month)


def CreateEvernoteToDoList(beginDay, endDay):
    if IsCorrectDayFormat(beginDay) and IsCorrectDayFormat(endDay):
        _beginDay = Date(beginDay)
        _endDay = _beginDay.AddDay(6)
        
        while _beginDay.IsSmallerThanDay_str(endDay):
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

            ModifyDatesInNoteBeginDate(_beginDay)

            _beginDay = _beginDay.AddDay(7)
            print(_beginDay.ToString())
            _endDay = _beginDay.AddDay(6)
    else:
        print('Please check date format!')


if __name__ == '__main__':
    CreateEvernoteToDoList('2022.06.06', '2022.07.03')
    
    #_beginDay = Date('2022.04.18')
    #ModifyDatesInNoteBeginDate(_beginDay)

    # 2022.01.24 Testing mouse wheel
    #wheel("1643037253309.png", Button.WHEEL_DOWN, 5)
    #wait(1)

    # 2022.01.24 Test find result
    #x = find("1643037435053.png")
    #print(x)
    #Offset(31, 367)
    #print(x)
    
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


