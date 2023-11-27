@echo off
@echo Starting Gesture Recognition......
@echo Choose the Following:
@echo 1.Detection 1 Hands
@echo 2.Detection 2 Hands
@echo 3.Static Gesture Training
@echo 4.Dynamic Gesture Training
@echo 5.Exit
set /p id=Enter your Option: 

if %id%==1 (
@echo ------------------------------
@echo Starting Gesture Detection....
@echo It may take a while....
@echo ------------------------------
python D:\PCode\Detection1H.py %*
@echo ------------------------------
@echo Gesture Detection Closed
@echo ------------------------------
timeout /t 5)

if %id%==2 (
@echo ------------------------------
@echo Starting Gesture Detection....
@echo It may take a while....
@echo ------------------------------
python D:\PCode\Detection2H.py %*
@echo ------------------------------
@echo Gesture Detection Closed
@echo ------------------------------
timeout /t 5)

if %id%==3 (
@echo ------------------------------
@echo Starting Static Gesture Training....
@echo It may take a while....
@echo ------------------------------
python D:\PCode\Static.py %*
@echo ------------------------------
@echo Static Gesture Training Ended
@echo ------------------------------
timeout /t 5)

if %id%==4 (
@echo ------------------------------
@echo Starting Dynamic Gesture Training....
@echo It may take a while....
@echo ------------------------------
python D:\PCode\Dynamic.py %*
@echo ------------------------------
@echo Dynamic Gesture Training Ended
@echo ------------------------------
timeout /t 5)


if %id%==5 (
@echo --------
@echo Quitting
@echo --------
timeout /t 5
exit /b 2)

pause
