import os
import subprocess
import time

# Function to execute an executable file in the background
def execute_file_in_background(file_path):
    try:
        # Execute the file in the background using subprocess
        subprocess.Popen([file_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"Executable file '{file_path}' started in the background.")
    except Exception as e:
        print(f"Error occurred while executing the file: {e}")

# Example usage
if __name__ == "__main__":
    file_path = "/path/to/executable/file"  # Specify the path to the executable file
    execute_file_in_background(file_path)

    # Optionally, wait for some time before exiting
    time.sleep(5)  # Wait for 5 seconds (adjust as needed)
