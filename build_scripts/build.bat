@echo off
cd ..

echo Running pyinstaller...
pyinstaller --onefile main.py

echo Moving executable to root folder...
move dist\main.exe .
ren "main.exe" "bookbot.exe"

echo Removing leftover folders...
rmdir /s /q build
rmdir /s /q dist
del main.spec

echo Build complete! To run double click 'bookbot.exe'.