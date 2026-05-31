import os
import time
import requests

from bs4 import BeautifulSoup
from urllib.parse import urljoin

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# =========================================================
# AMC URLS
# =========================================================

AMC_URLS = {
    "HSBC_AMC":
    "https://www.assetmanagement.hsbc.co.in/en/mutual-funds/investor-resources?Date=&Cap=&Doc=notice-ads#&module-17=1",

    "Nippon_AMC":
    "https://mf.nipponindiaim.com/investor-service/quick-links/notice-addendum",

    "Birla_AMC":
    "https://mutualfund.adityabirlacapital.com/forms-and-downloads/addendums",

    "Axis_AMC":
    "https://www.axismf.com/downloads",

    "Quantum_AMC":
    "https://www.quantumamc.com/Download-document#headingOne"
}

# =========================================================
# DIRECTORY
# =========================================================

BASE_DIR = "AMC_Notices"

os.makedirs(BASE_DIR, exist_ok=True)

# =========================================================
# SELENIUM SETUP
# =========================================================

options = Options()

# Uncomment for hidden browser
# options.add_argument("--headless")

options.add_argument("--start-maximized")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# =========================================================
# DOWNLOAD FUNCTION
# =========================================================

def download_file(url, filepath):

    try:

        response = requests.get(url, timeout=60)

        if response.status_code == 200:

            with open(filepath, "wb") as file:
                file.write(response.content)

            print(f"Downloaded: {filepath}")

        else:

            print(f"Failed: {url}")

    except Exception as e:

        print(e)

# =========================================================
# AUTO SCROLL
# =========================================================

def scroll_page():

    last_height = driver.execute_script(
        "return document.body.scrollHeight"
    )

    while True:

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        time.sleep(2)

        new_height = driver.execute_script(
            "return document.body.scrollHeight"
        )

        if new_height == last_height:
            break

        last_height = new_height

# =========================================================
# SCRAPER
# =========================================================

def scrape_amc(amc_name, url):

    print(f"\nSCRAPING {amc_name}\n")

    amc_folder = os.path.join(BASE_DIR, amc_name)

    os.makedirs(amc_folder, exist_ok=True)

    driver.get(url)

    time.sleep(5)

    # Scroll entire page
    scroll_page()

    time.sleep(3)

    # Capture all links using Selenium
    elements = driver.find_elements(By.TAG_NAME, "a")

    pdf_links = []

    for element in elements:

        try:

            href = element.get_attribute("href")

            if href and ".pdf" in href.lower():

                full_url = urljoin(url, href)

                pdf_links.append(full_url)

        except:
            pass

    # Remove duplicates
    pdf_links = list(dict.fromkeys(pdf_links))

    print(f"TOTAL PDF LINKS FOUND: {len(pdf_links)}")

    # Take first/latest 12
    latest_12 = pdf_links[:12]

    print(f"DOWNLOADING: {len(latest_12)} PDFs")

    # Download
    for pdf_url in latest_12:

        filename = pdf_url.split("/")[-1]

        filepath = os.path.join(
            amc_folder,
            filename
        )

        download_file(pdf_url, filepath)

# =========================================================
# MAIN
# =========================================================

try:

    for amc_name, amc_url in AMC_URLS.items():

        scrape_amc(amc_name, amc_url)

finally:

    driver.quit()

print("\nALL AMC PDFs DOWNLOADED SUCCESSFULLY")