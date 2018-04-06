@echo off

title PyDO - OTP Server

cd ../

rem This start script is used during the development of PyDO to run the server.
rem We recommend creating your own start scripts when running in production.
rem A.K.A. Don't run components in different threads, run them inside different python instances.

:main
python main.py --server-host 127.0.0.1 --md-port 7101 --ca-port 6667 --game-config Config.prc
pause

goto main