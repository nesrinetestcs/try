from selenium import webdriver
import time
import os

# Function to open a web page in the background and wait for file download
def open_website_and_wait_for_download(url, download_directory):
    try:
        # Initialize Chrome WebDriver with headless mode
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_directory
        })
        driver = webdriver.Chrome(options=chrome_options)

        # Open the website triggering the file download
        driver.get(url)

        print(f"Website '{url}' opened in the background.")

        # Wait for 60 seconds (adjust as needed)
        time.sleep(60)

        # Check if the file has been downloaded
        files = os.listdir(download_directory)
        downloaded_files = [f for f in files if f.endswith(".zip")]  # Adjust file extension if needed

        if downloaded_files:
            print("File download completed. Downloaded files:")
            for file in downloaded_files:
                print(os.path.join(download_directory, file))
        else:
            print("No files were downloaded within the specified time.")

    except Exception as e:
        print(f"Error occurred while opening the website and waiting for download: {e}")
    finally:
        # Close the WebDriver
        driver.quit()

# Example usage
if __name__ == "__main__":
    url = "https://www.process-one.net/downloads/downloads-action.php?file=/20.12/ejabberd_20.12-0_amd64.deb"  # Example URL that triggers file download
    download_directory = "C:\\Users\\HP\Documents\\2EMP\\s2 mine"  # Specify the download directory
    open_website_and_wait_for_download(url, download_directory)
