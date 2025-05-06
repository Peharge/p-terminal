@echo off
call "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvarsall.bat" x64
echo Visual Studio Compiler Environment enabled.
cd /d "%~dp0\..\..\peharge"
echo Start compiling the peharge project...
cl.exe /EHsc main.cpp /Fe:peharge_project.exe
pause
