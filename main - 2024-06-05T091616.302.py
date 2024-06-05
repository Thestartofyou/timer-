import time
from plyer import notification

def pomodoro_work():
    notification.notify(
        title="Work Time",
        message="Focus on your task for the next 25 minutes.",
        timeout=10
    )

def pomodoro_break():
    notification.notify(
        title="Break Time",
        message="Take a 5-minute break. Relax and stretch.",
        timeout=10
    )

# Work for 25 minutes, then take a 5-minute break
while True:
    pomodoro_work()
    time.sleep(25 * 60)  # 25 minutes
    pomodoro_break()
    time.sleep(5 * 60)   # 5 minutes

