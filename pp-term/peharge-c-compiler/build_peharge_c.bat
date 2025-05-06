@echo off
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
echo Visual Studio C compiler environment activated.
cd /d "%~dp0\..\..\peharge_C"
echo Starting C compilation...
cl.exe /TC main.c /Fe:peharge_c.exe
pause
