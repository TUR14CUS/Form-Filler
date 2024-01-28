# Selenium Form Filler

This Python script automates the process of filling a web form using Selenium. The script provides two options for the user: filling the form with existing data or generating fake data and then filling the form.

## Prerequisites

- **Python**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/).

- **ChromeDriver**: Download the ChromeDriver executable compatible with your Chrome browser version. You can find it [here](https://sites.google.com/chromium.org/driver/).

- **Dependencies**: Install the required Python packages using the following command:

  ```bash
  pip install selenium pandas faker
  ```

## Usage

1. **Run the Script:**

   Open a terminal and run the script by executing the following command:

   ```bash
   python form_filler.py
   ```

2. **Choose an Option:**

   The script will prompt you to choose an option:
   - Option 1: Fill the form with existing data from a CSV file.
   - Option 2: Generate fake data, fill the form, and save it to a CSV file.

3. **Provide Input:**

   - If you chose Option 1, enter the path to the existing CSV file containing the data.
   - If you chose Option 2, provide the number of fake data entries to generate and the column name for comments.

4. **Enter Details:**

   Input the path to the ChromeDriver executable, the URL of the form, and the XPath of the Submit button.

5. **Automated Form Filling:**

   The script will launch a Chrome browser, open the specified form, and fill it with the provided data.

## Important Notes

- Ensure that you have a stable internet connection and that the form elements are accessible using the provided XPath.

- If the form has additional or different fields, adjust the script accordingly.

- The script will print the columns of the data frame for your reference.

Feel free to modify the script to suit your specific requirements!