import schedule
import time
import os

# Function to open the file
def open_file():
    file_path = "/path/to/your/file.txt"  # Specify the path to your file
    os.system(f"start {file_path}")  # Open the file using the default application

# Schedule the task to run on a specific day
schedule.every().monday.at("10:00").do(open_file)  # Change "monday" to the desired day and adjust the time

# Keep the script running to allow scheduled tasks to execute
while True:
    schedule.run_pending()
    time.sleep(1)
