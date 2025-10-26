import requests
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def chrome_driver():
    # Automatically installs the right ChromeDriver version
    driver_path = ChromeDriverManager().install()
    print("Driver path:", driver_path)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")          # Run in headless mode (no GUI)
    options.add_argument("--no-sandbox")        # Required for WSL / Docker
    options.add_argument("--disable-dev-shm-usage")  # Prevents shared memory issues
    options.add_argument("--remote-debugging-port=9222")

    
    options.binary_location = "/usr/bin/google-chrome"

    # Safety: ensure driver binary is executable
    if not os.access(driver_path, os.X_OK):
        os.chmod(driver_path, 0o755)

    return webdriver.Chrome(service=ChromeService(driver_path), options=options)


# --- Extract Netflix Top 10 ---
def extract_data():
    url = "https://www.netflix.com/tudum/top10"
    r = requests.get(url)
    print("Request status:", r.status_code)

    driver = chrome_driver()
    driver.get(url)

    time.sleep(4)  # Wait for JS to load

    soup = BeautifulSoup(driver.page_source, 'html.parser')

    movie_names = [m.get_text() for m in soup.find_all('td', class_='title')]
    views_list = [v.get_text() for v in soup.find_all('td', class_='views')]
    runtime_list = [r.get_text() for r in soup.find_all('td', class_='desktop-only')]

    duration = runtime_list[::2]
    hours_played = runtime_list[1::2]

    import csv
    with open("netflix_top10.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Views", "Runtime", "Hours Viewed"])
        for movie, views, runtime, hour in zip(movie_names, views_list, duration, hours_played):
            writer.writerow([
                movie,
                views.replace(",", ""),
                runtime,
                hour.replace(",", "")
            ])

    driver.quit()
    print("Data extracted and saved to netflix_top10.csv")

