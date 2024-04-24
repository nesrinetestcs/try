import subprocess
import sys


def install_selenium():
    try:
        # Use pip to install Selenium
        subprocess.check_call([sys.executable, "-m", "pip", "install", "selenium"])
        print("Selenium installed successfully.")
    except subprocess.CalledProcessError:
        print("Failed to install Selenium.")


# Function to open a web page in the background using Selenium
def open_web_page(url):
    try:
        # Import Selenium after installation
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options

        # Configure Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        # Initialize Chrome WebDriver with headless options
        driver = webdriver.Chrome(options=chrome_options)

        # Open the web page
        driver.get(url)

        # Optionally, you can perform further actions here, such as interacting with elements on the page

        # Close the WebDriver
        driver.quit()

        print(f"Web page '{url}' opened in the background.")
    except ImportError:
        print("Selenium is not installed. Installing...")
        install_selenium()
        print("Attempting to open the web page again...")
        open_web_page(url)
    except Exception as e:
        print(f"Error occurred while opening the web page: {e}")


# Example usage
if __name__ == "__main__":
    url = "https://www.process-one.net/downloads/downloads-action.php?file=/20.12/ejabberd_20.12-0_amd64.deb"
    open_web_page(url)
