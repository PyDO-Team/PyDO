@echo off

title PyDO - AI (Unnamed)

cd ../

rem This start script is used during the development of PyDO to run the test AI server.
rem We recommend creating your own start scripts when running in production.

set /P DISTRICT_NAME=District Name (Default: Toonville): || ^
set DISTRICT_NAME=Toonville

title PyDO - AI (%DISTRICT_NAME%)

:main
python -m otp.ai.AIStart --ai-name %DISTRICT_NAME% --md-host 127.0.0.1 --md-port 7101
pause

goto main