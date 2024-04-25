import schedule
import time

def my_task():
    print("Executing my task...")

# Schedule the task to run on a different day
schedule.every().monday.at("10:00").do(my_task)  # Change Monday to the desired day
# You can also specify the time using a 24-hour format, for example, "14:30" for 2:30 PM

# Keep the script running to allow scheduled tasks to execute
while True:
    schedule.run_pending()
    time.sleep(1)
