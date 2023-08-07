import MonthMaxDayModule

class Date:
    def __init__(self, date):
        dateArray = date.split('.')
        self.mYear = int(dateArray[0])
        self.mMonth = int(dateArray[1])
        self.mDay = int(dateArray[2])
        self.mMonthMaxDay = MonthMaxDay(self.mYear)
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
            ret = Date(self.ToString())
            ret.mDay = self.mDay + day
            if ret.mDay > self.mMonthMaxDay.GetMonthMaxDay(self.mMonth):
                if self.mMonth == 12:
                    ret.mYear = ret.mYear + 1
                    ret.mMonth = 1
                else:
                    ret.mMonth = self.mMonth + 1
                ret.mDay = ret.mDay - self.mMonthMaxDay.GetMonthMaxDay(self.mMonth)
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
        if self.mYear > _year:
            isBigger = True
        elif self.mMonth > _month:
            isBigger = True
        else:
            if self.mDay > _day:
                isBigger = True
        return isBigger

    def IsBiggerThanDay_Date(self, day):
        isBigger = False
        if self.mYear > day.GeYyear:
            isBigger = True
        elif self.mMonth > day.GetMonth():
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
        if self.mYear < _year:
            isSmaller = True
        elif self.mMonth < _month:
            isSmaller = True
        elif self.mMonth == _month:
            if self.mDay < _day:
                isSmaller = True
        return isSmaller

    def IsSmallerThanDay_Date(self, day):
        isSmaller = False
        if self.mYear < day.GetYear():
            isSmaller = True
        elif self.mMonth < day.GetMonth():
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

class TestDate:
    def TestAddDay(self):
        print('\nTestDate.TestAddDay')
        # ARRANGE
        date = Date('2022.01.22')
        print('input date = ' + date.ToString())
        
        # ACT
        end = date.AddDay(10)
        print('after AddDay = ' + end.ToString())
        
        # ASSERT
        if end.ToString() == '2022.02.01':
            print('OK')
        else:
            print('FAIL')

    def TestAddDayAndCrossYear(self):
        print('\nTestDate.TestAddDayAndCrossYear')
        # ARRANGE
        date = Date('2022.12.22')
        print('input date = ' + date.ToString())
        
        # ACT
        end = date.AddDay(10)
        print('after AddDay = ' + end.ToString())
        
        # ASSERT
        if end.ToString() == '2023.01.01':
            print('OK')
        else:
            print('FAIL')

    # TODO: test four method related check whether input date bigger or smaller current class
    #       And need to check cross situation. 