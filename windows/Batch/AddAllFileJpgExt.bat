@echo off
setlocal enableextensions
FOR /F "tokens=*" %%g IN ('dir /b') do (
	REM set file=%%g
	REM set EXT=%%~xg
	echo %%g
	echo ", extension = " %%~xg

	ren "%%g" "%%g.jpg"
)
endlocal
