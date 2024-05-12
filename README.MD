# Saucedemo Automated Testing Framework
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This is an example automated testing framework using Selenium WebDriver and Pytest.
The tests are written for the [Saucedemo Website](https://www.saucedemo.com/).

## Test Coverage

The functionality to be covered by the automated tests is detailed in the [check-list.md](check-list.md) file

## Technology Stack

The framework utilizes the following technologies and approaches:
- Page Object Model (POM) design pattern
- Faker for generating test data
- Allure reports for test reporting

## Getting Started

To use and run tests, follow these steps:

1. Clone the to your local machine using the following command:
```
git clone https://github.com/YuryHerasimau/saucedemo-autotesting.git
```
2. Navigate to the cloned repository directory on your local machine.
3. Install the required dependencies by running the following command:
```
pip install -r requirements.txt
```
4. Activate the virtual environment by running the appropriate command based on your operating system. For Windows, you can use:
```
source env/Scripts/activate
```
5. Finally, run the tests using pytest with the following command to generate Allure reports:
```
pytest --alluredir=%allure_result_folder% ./tests
```
After running the tests, serve the Allure report using the following command:
```
allure serve %allure_result_folder%
```