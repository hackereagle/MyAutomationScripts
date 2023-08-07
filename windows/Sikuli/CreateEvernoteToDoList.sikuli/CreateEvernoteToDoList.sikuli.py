import MonthMaxDayModule
import DateModule


# global variable
#monthMaxDay = MonthMaxDay(False)
monthMaxDay = MonthMaxDay(2023)

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





originDay = [Pattern("1642946701374.png").similar(.80), Pattern("1642946760378.png").similar(.80), Pattern("1642946788844.png").similar(.80), Pattern("1642946800414.png").similar(.90), Pattern("1642946823444.png").similar(.80), Pattern("1642946837403.png").similar(.80), Pattern("1642946847284.png").similar(.80)]
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
            #_day = _day - monthMaxDay.GetMonthMaxDay(_month)
            _day = 1
            _month = _month + 1



def CreateEvernoteToDoList(beginDay, endDay):
    if IsCorrectDayFormat(beginDay) and IsCorrectDayFormat(endDay):
        _beginDay = Date(beginDay)
        _endDay = _beginDay.AddDay(6)
        
        while _beginDay.IsSmallerThanDay_str(endDay):
            click(Pattern("1642860440444.png").similar(.43))
            wait(2)
        
            click("1642861196260.png")
            wait(4)
        
            click("1642861244399.png")
            wait(1)
    
            type(_beginDay.ToString() + '~' + _endDay.ToString() + ' To Do List')
            wait(1)
        
            click("1642861289557.png")
            wait(1)
        
            click("1642861410315.png")
            wait(2)

            ModifyDatesInNoteBeginDate(_beginDay)

            _beginDay = _beginDay.AddDay(7)
            print(_beginDay.ToString())
            _endDay = _beginDay.AddDay(6)
    else:
        print('Please check date format!')


if __name__ == '__main__':
    CreateEvernoteToDoList('2023.10.02', '2023.12.31')
    
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
    #print('Test MonthMaxDay module')
    #testMonthMaxDay = TestMonthMaxDay()
    #testMonthMaxDay.TestLeepYearFebruary()
    #testMonthMaxDay.TestNotLeepYearFebruary()

    # testing IsCorrectDayFormat
    #print(IsCorrectDayFormat('2022.01.22'))

    # testing Date
    #print('Test Date module')
    #testDate = TestDate()
    #testDate.TestAddDay()
    #testDate.TestAddDayAndCrossYear()
    
    
    


