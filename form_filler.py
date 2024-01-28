from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from faker import Faker

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

def generate_fake_data(num_entries, comments_column):
    fake = Faker()
    profiles = [fake.profile() for _ in range(num_entries)]

    df = pd.DataFrame(profiles, columns=['name', 'mail', 'address'])
    df['Phone number'] = [fake.phone_number() for _ in range(num_entries)]
    df[comments_column] = '-'
    df.rename(columns={'name': 'Name', 'mail': 'Email', 'address': 'Address'}, inplace=True)

    df.to_csv('fake_data.csv', index=False)

def print_dataframe_columns(df):
    for column in df.columns:
        print(column)

def main():
    try:
        print("Choose an option:")
        print("1. Fill form with existing data file")
        print("2. Generate fake data and fill form")
        option = input("Enter the option number: ").strip()

        if option == "1":
            # User Inputs for existing data file
            DATA_FILE_PATH = input("Enter the path to the data file (CSV): ").strip()

        elif option == "2":
            # User Inputs for generating fake data
            NUM_ENTRIES = int(input("Enter the number of fake data entries to generate: "))
            COMMENTS_COLUMN = input("Enter the column name for comments: ")
            generate_fake_data(NUM_ENTRIES, COMMENTS_COLUMN)
            DATA_FILE_PATH = 'fake_data.csv'

        else:
            print("Invalid option")
            return

        # Common User Inputs
        CHROME_DRIVER_PATH = input("Enter the path to the ChromeDriver executable: ").strip()
        FORM_WEBSITE = input("Enter the URL of the form: ").strip()
        SUBMIT_BUTTON_XPATH = input("Enter the XPath of the Submit button: ").strip()

        # Set up WebDriver
        driver = setup_driver(CHROME_DRIVER_PATH)

        # Read data from CSV
        df = pd.read_csv(DATA_FILE_PATH)
        print_dataframe_columns(df)

        # Iterate over data rows and fill the form
        for _, data_row in df.iterrows():
            fill_form(driver, data_row, FORM_WEBSITE, SUBMIT_BUTTON_XPATH)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
