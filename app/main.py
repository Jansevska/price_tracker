from selenium.webdriver import Remote, ChromeOptions  
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

AUTH = os.environ['AUTH']
SBR_WEBDRIVER = f'https://{AUTH}@brd.superproxy.io:9515'


def main():
    print('Connecting to Scraping Browser...')
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, 'goog', 'chrome')
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        print('Connected! Navigating to https://www.amazon.com/2021-Apple-10-2-inch-iPad-Wi-Fi/dp/B09G9FPHY6')
        driver.get('https://www.amazon.com/2021-Apple-10-2-inch-iPad-Wi-Fi/dp/B09G9FPHY6/ref=mp_s_a_1_1_sspa?crid=3C0GSCZB3YQT0&dib=eyJ2IjoiMSJ9.x37hw5scXMlLBGdXY-8OgzQ8AeAEcu3C1MleyqUbfbm-R1EqLMeiHh2twkyP3A8PDyhJG1166Mv0ZK4r-eBLPfZYG6uUbNxJdWdYKD8o8AwsGL2jfsd-SfzJMPNdvLrBUEoBccjwYQi6584H6n-AX2bPxlR22bZAsFGBMWiYCi2dXlm6OHLNLZb4GRNhSsg1mSlQ8BwSfmvV8nH-1yaRTA.8or8bAR-8upcdneSZJejnQdVwwJ-e_zD6mnueYBOADw&dib_tag=se&keywords=ipad&qid=1710724392&sprefix=ipad%2Caps%2C220&sr=8-1-spons&ufe=app_do%3Aamzn1.fos.f5122f16-c3e8-4386-bf32-63e904010ad0&sp_csd=d2lkZ2V0TmFtZT1zcF9waG9uZV9zZWFyY2hfYXRm&psc=1')
        print('Navigated! Waiting for <body> element...')
        # Use WebDriverWait to wait for the price element to be present on the page
        try:
            # Define the maximum wait time (for example, 5 seconds)
            wait = WebDriverWait(driver, 5)
            
            # Wait until the element identified by class name 'aok-offscreen' is present
            price_element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "aok-offscreen")))
            
            # Print the text attribute of the price element
            print(price_element.text)
            
        except Exception as e:
            print(f"An error occurred: {e}") 
            html = driver.page_source  
        print(html) 


if __name__ == '__main__':
    main()

        # price = driver.find_element(By.CLASS_NAME, "aok-offscreen")
        # print(price.text)
        # price_whole = driver.find_element(By.CLASS_NAME, "a-price-whole")
        # print(price_whole.text)