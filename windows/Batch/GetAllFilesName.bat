@echo off

REM:: Check parameter whether valid
if "%~1" == "" goto blank_1
if "%~2" == "" goto blank_2

REM:: Check parameter whether valid
dir %1 /b > "%2.txt"
echo "Already listed files in %1 into %2.txt"
pause
goto DONE

:blank_1
echo "First parameter is empty."
echo "Please type directory which would be listed file."
pause
goto DONE

:blank_2
echo "Second parameter is empty."
echo "Please type file storing information name."
pause
goto DONE

:DONE

