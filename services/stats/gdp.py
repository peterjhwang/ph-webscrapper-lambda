from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = "/opt/headless-chromium"
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
DRIVER = webdriver.Chrome("/opt/chromedriver", options=chrome_options)


def selenium_get_gdp_url(year: str, month: str) -> str:
    url = f"https://www.stats.govt.nz/information-releases/gross-domestic-product-{month}-{year}-quarter"
    DRIVER.get(url)
    csv_url = ""
    for el in DRIVER.find_elements(
        by=By.XPATH, value='//div[@class="block-document__container"]/a'
    ):
        temp_url = el.get_attribute("href")
        if "csv" in temp_url and "visualisation" in temp_url:
            csv_url = temp_url
            break
    return csv_url
