@echo off
REM Tạo venv
python -m venv venv

REM Kích hoạt venv
call venv\Scripts\activate

REM Cài thư viện cần thiết
pip install flet

echo Đã tạo xong môi trường và cài flet!
pause
