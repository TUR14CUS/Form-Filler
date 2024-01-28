from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def setup_driver(driver_path):
    service = Service(executable_path=driver_path)
    return webdriver.Chrome(service=service)

def fill_form(driver, data_row, form_website, submit_button_xpath):
    driver.get(form_website)
    wait = WebDriverWait(driver, 10)

    for column, value in data_row.items():
        input_selector = f'div[data-params*="{column}"] input, div[data-params*="{column}"] textarea'
        text_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, input_selector)))
        text_input.send_keys(value)

    submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, submit_button_xpath)))
    submit_button.click()

def main():
    try:
        # User Inputs
        CHROME_DRIVER_PATH = input("Enter the path to the ChromeDriver executable: ").strip()
        FORM_WEBSITE = input("Enter the URL of the form: ").strip()
        DATA_FILE_PATH = input("Enter the path to the data file (CSV): ").strip()
        SUBMIT_BUTTON_XPATH = input("Enter the XPath of the Submit button: ").strip()

        # Set up WebDriver
        driver = setup_driver(CHROME_DRIVER_PATH)

        # Read data from CSV
        df = pd.read_csv(DATA_FILE_PATH)

        # Iterate over data rows and fill the form
        for _, data_row in df.iterrows():
            fill_form(driver, data_row, FORM_WEBSITE, SUBMIT_BUTTON_XPATH)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
