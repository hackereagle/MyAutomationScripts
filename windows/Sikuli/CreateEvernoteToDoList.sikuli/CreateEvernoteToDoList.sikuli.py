from MonthMaxDayModule import *
from DateModule import *

# global variable
#monthMaxDay = MonthMaxDay(2023)

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

    monthMaxDay = MonthMaxDay(int(strs[0]))
    isDayReasonable = False
    maxDay = monthMaxDay.GetMonthMaxDay(month)
    day = int(strs[2])
    if day > 0 and day <= maxDay:
        isDayReasonable = True
    else:
        isDayReasonable = False

    return isThreeEle and isMonthReasonable and isDayReasonable


originDay = [Pattern("1710641326621.png").similar(.80), Pattern("1710641395688.png").similar(.85), Pattern("1710641432817.png").similar(.95), Pattern("1710641483222.png").similar(.80), Pattern("1710641517708.png").similar(.95), Pattern("1710641553350.png").similar(.85), Pattern("1710641584388.png").similar(.80)]
def ModifyDatesInNoteBeginDate(date):
    print(date.ToString())
    _year = date.GetYear()
    _month = date.GetMonth()
    _day = date.mDay
    monthMaxDay = MonthMaxDay(_year)
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
        wait(1)
        type(Key.ESC)
        wait(1)

        wheel(pos, Button.WHEEL_DOWN, 2)
        wait(1)

        _day = _day + 1
        if _day > monthMaxDay.GetMonthMaxDay(_month):
            _day = 1
            _month = _month + 1
            if _month > 12:
                _year = _year + 1
                monthMaxDay = MonthMaxDay(_year)


language = 1
# row = step, col = language
evernoteGui = [[Pattern("1642860440444.png").similar(.43), "1722781851996.png"],
                   ["1642861196260.png", "1722781851996.png"],
                   ["1642861244399.png", "1691416115722.png"],
                   ["1642861289557.png", "1710640995438.png"]]

todoListIcon = "1642861410315.png"

def CreateEvernoteToDoList(beginDay, endDay):
    if IsCorrectDayFormat(beginDay) and IsCorrectDayFormat(endDay):
        _beginDay = Date(beginDay)
        _endDay = _beginDay.AddDay(6)

        # TODO: if cross year, here will bug
        #       Because current will bigger than end day, after crossed year
        #       It maybe need a method to judge whether equal or bigger
        while _beginDay.IsSmallerThanDay_str(endDay):
            # 2024.03.17 newest evernote removed this button. 
            #click(evernoteGui[0][language])
            #wait(2)
        
            click(evernoteGui[1][language])
            wait(10)
        
            click(evernoteGui[2][language])
            wait(1)
    
            type(_beginDay.ToString() + '~' + _endDay.ToString() + ' To Do List')
            wait(1)
        
            click(evernoteGui[3][language])
            wait(3)
        
            click(todoListIcon)
            wait(5)

            ModifyDatesInNoteBeginDate(_beginDay)

            _beginDay = _beginDay.AddDay(7)
            print(_beginDay.ToString())
            _endDay = _beginDay.AddDay(6)
    else:
        print('Please check date format!')


if __name__ == '__main__':
   # TODO: regonize screen dimension and do something or display warning message
   #       1. https://stackoverflow.com/questions/55120579/sikuli-changing-screen-size
   #       2. https://sikulix-2014.readthedocs.io/en/latest/screen.html
    CreateEvernoteToDoList('2024.09.23', '2024.09.29')
    
    #_beginDay = Date('2022.04.18')
    #ModifyDatesInNoteBeginDate(_beginDay)

    # 2022.01.24 Testing mouse wheel
    #wheel("1643037253309.png", Button.WHEEL_DOWN, 5)
    #wait(1)

    # 2022.01.24 Test find result
    #x = find()
    #print(x)
    #Offset(31, 367)
    #print(x)
    
    # testing MonthMaxDay
    #print('Test MonthMaxDay module')
    #testMonthMaxDay = TestMonthMaxDay()
    #testMonthMaxDay.TestLeepYearFebruary()
    #testMonthMaxDay.TestNotLeepYearFebruary()

    # testing IsCorrectDayFormat
    #print('\n\nTest IsCorrectDayFormat')
    #print(IsCorrectDayFormat('2022.01.22'))

    # testing Date
    #print('\n\nTest Date module')
    #testDate = TestDate()
    #testDate.TestAddDay()
    #testDate.TestAddDayAndCrossYear()
    
    
    


