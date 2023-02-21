# Selenium/Python Test Script
This repository contains sample code for automated testing using Selenium and Python. The test script logs into https://www.saucedemo.com/ using valid and invalid credentials and verifies the login outcome.

# Requirements
Python 3.7 or later
pip (Python package installer)
Chrome browser
# Installation
Clone this repository to your local machine.
Open the terminal or command prompt and navigate to the cloned repository directory.
Run the following command to install the required Python packages:
```
pip install -r requirements.txt
```
# Usage
In the terminal, navigate to the cloned repository directory.
Run the following command to execute the test script:
```
pytest test_login.py
```
# Configuration
The conftest.py file contains the configuration settings for the test script, including the base URL for the website being tested. If necessary, modify the base_url variable in this file to match the URL of the website you are testing.

# Test Cases
The test script includes two test cases:

`test_valid_login` - Logs into the website using valid credentials and verifies successful login.
`test_invalid_login` - Attempts to log into the website using invalid credentials and verifies that an error message is displayed.
# Reporting
The test results are automatically saved to an HTML report, which can be found in the reports folder after the test execution. The report includes details about the test execution, including test case status, execution time, and any error messages.

# Contributors
Kodjo Semeglo - Creator and maintainer of this repository.
License
This project is licensed under the MIT License.
