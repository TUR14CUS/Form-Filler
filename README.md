# Selenium Form Filler

This Python script utilizes Selenium to automate the process of filling a web form with data from a CSV file. The script prompts the user for input, including the path to the ChromeDriver executable, the URL of the form, the path to the data file in CSV format, and the XPath of the Submit button.

## Prerequisites

- **ChromeDriver:** Ensure you have ChromeDriver installed. You can download it from [here](https://sites.google.com/chromium.org/driver/).

- **Python Libraries:** Make sure you have the necessary Python libraries installed. You can install them using the following:

  ```bash
  pip install selenium pandas
  ```

## How to Use

1. **Run the Script:**
   - Execute the script by running the Python file in your terminal or preferred Python environment:

     ```bash
     python form_filler.py
     ```

2. **Provide Inputs:**
   - Enter the requested information, including the path to the ChromeDriver executable, the URL of the form, the path to the CSV file containing the data, and the XPath of the Submit button.

3. **Automation:**
   - The script will launch a headless Chrome browser, read the data from the CSV file, and automate the process of filling the form on the provided website.

4. **Completion:**
   - Once the script completes or encounters an error, the Chrome browser will be closed, and the script will display relevant messages.

## Notes

- **Error Handling:**
  - The script includes basic error handling to catch and display any exceptions that might occur during execution.

- **Customization:**
  - You can customize the script by modifying variables such as `CHROME_DRIVER_PATH`, `FORM_WEBSITE`, `DATA_FILE_PATH`, and `SUBMIT_BUTTON_XPATH` based on your specific use case.

- **WebDriver Setup:**
  - Ensure that the version of ChromeDriver matches your Chrome browser version.

- **CSV Data Format:**
  - The script assumes that the data in the CSV file is organized with columns representing form fields and rows containing the corresponding data.

Feel free to adapt and modify the script according to your requirements!