import requests
import os
import time 
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def chrome_driver():
    driver_path = ChromeDriverManager().install()
    print("Driver path:", driver_path)

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")   # Run in headless mode
    options.add_argument("--no-sandbox") # Bypass OS security

    # Check if it's actually executable
    if not os.access(driver_path, os.X_OK):
        print("❌ Not executable. Trying to locate the real binary.")
        for root, dirs, files in os.walk(os.path.dirname(driver_path)):
            for file in files:
                if "chromedriver" in file and not file.endswith(".chromedriver"):
                    potential_path = os.path.join(root, file)
                    print("✅ Found likely candidate:", potential_path)
                    driver_path = potential_path
                    break

    return webdriver.Chrome(service=ChromeService(driver_path), options=options)

url = "https://www.netflix.com/tudum/top10"

r = requests.get(url)
print(r.status_code)

driver = chrome_driver()
driver.get(url)

def extract_data():
    movie_names = []
    views_list = []
    runtime_list = []

    driver.get(url)

    time.sleep(4)

    structure = driver.page_source

    soup = BeautifulSoup(structure, 'html.parser')

    movies = soup.find_all('td', class_='title')
    for movie in movies:
        title = movie.get_text()
        movie_names.append(title)

    views = soup.find_all('td', class_='views')
    for view in views:
        view_count = view.get_text()
        views_list.append(view_count)

    runtimes = soup.find_all('td', class_='desktop-only')
    for runtime in runtimes:
        run_time = runtime.get_text()
        runtime_list.append(run_time)

    duration = runtime_list[::2]
    hours_played= runtime_list[1::2]

    # save as csv
    import csv

    with open("netflix_top10.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Title", "Views", "Runtime", "Hours Viewed"])
        for movie, views, runtime, hour in zip(movie_names, views_list, duration, hours_played):
            views_int = views.replace(",", "")
            hour_int = hour.replace(",", "")
            writer.writerow([movie, views_int, runtime, hour_int])

    driver.quit()

    """with open("netflix_top10.csv", "w") as f:
        f.write("Title,Views,Runtime,Hours Viewed\n")
        for movie, views, runtime, hour in zip(movie_names, views_list, duration, hours_played):
            views_int = views.replace(",", "")
            hour_int = hour.replace(",", "")
            f.write(f"{movie},{views_int},{runtime},{hour_int}\n")

    driver.quit()"""
#extract_data()
    print("Data extracted and saved to netflix_top10.csv")
   

