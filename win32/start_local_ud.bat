@echo off

title PyDO - UberDog Server

cd ../

rem This start script is used during the development of PyDO to run the test UD server.
rem We recommend creating your own start scripts when running in production.

:main
python -m otp.ud.UDStart --md-host 127.0.0.1 --md-port 7101
pause

goto main