# Import required libraries
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants
LOG_FILE = "website_activity.log"
MONITOR_INTERVAL = 5  # in seconds

# Create a new instance of Chrome in headless mode
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def log_website_activity(url, title, duration):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} | URL: {url} | Title: {title} | Duration: {duration} seconds\n"
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

def monitor_browser_activity():
    current_url = None
    start_time = time.time()

    while True:
        try:
            new_url = driver.current_url
            if new_url != current_url:
                if current_url:
                    end_time = time.time()
                    duration = round(end_time - start_time)
                    log_website_activity(current_url, driver.title, duration)
                    start_time = end_time

                current_url = new_url

            time.sleep(MONITOR_INTERVAL)

        except Exception as e:
            # Handle exceptions gracefully and continue monitoring
            print(f"Error: {e}")

if __name__ == "__main__":
    try:
        # Start monitoring
        monitor_browser_activity()
    except KeyboardInterrupt:
        # Gracefully close the browser and exit on KeyboardInterrupt (Ctrl+C)
        driver.quit()
        print("Monitoring stopped.")
