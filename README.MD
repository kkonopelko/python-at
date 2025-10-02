# Introduction
Test Automation project with simple API/E2E tests using Python and Playwright.
 - [Pet store open API](https://petstore.swagger.io/) is used for API testing.
 - [Web site](https://petstore.swagger.io/) is used for UI testing.

Languages and Frameworks: 
 - Python 3.13.7 as the programming language.
 - Pytest as the testing framework.
 - Playwright as the web browser automation framework using the Python binding.
 - for logging - ???
 - for reporting - ???

# Getting Started

## Installation

1. Install [Python latest version](https://www.python.org/downloads/)
2. Create/activate virtual environment (venv)
3. Install dependencies from requirements.txt file for venv: `pip install -r requirements.txt`
4. Install Playwright browsers for E2E tests: `playwright install`

## Run tests

1. Check `settings.json` file config
2. Activate venv (at the begining of the line now you will see (venv)): 
`.\venv\Scripts\activate` or `path to env folder\venv\Scripts\activate`
3. Run tests: `python -m pytest -v` or `pytest`
- run specific test: `pytest -v tests/api/test_product_endpoints.py::test_get_all_products_should_return_200`
- run tests from 1 file (fixture): `pytest -v tests/api/test_product_endpoints.py::TestProductEndpoints`
- run tests with category: `pytest -m api`