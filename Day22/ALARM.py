from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time of alarm to be set :HH:MM:SS \n ")
alarm_hour = alarm_time[:2]
alarm_minute = alarm_time[3:5]
alarm_second = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("Alarm is set .")

while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if alarm_period == current_period:
        if alarm_hour == current_hour:
            if alarm_minute == current_minute:
                if alarm_second == current_seconds:
                    print("Wake UP !")
                    playsound("Enter the path of mp3 file .")
                    break
