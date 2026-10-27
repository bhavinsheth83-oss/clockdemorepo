
import time
from datetime import datetime

alarm_time = input("Enter alarm time (HH:MM in 24-hour format): ")

print(f"Alarm set for {alarm_time}")

while True:
    current_time = datetime.now().strftime("%H:%M")

    if current_time == alarm_time:
        print("⏰ ALARM! Wake up!")
        for i in range(10):
            print("\a")  # System beep
            time.sleep(1)
        break

    time.sleep(1)
