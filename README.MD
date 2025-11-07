# Introduction
Test automation framework with:
- API/E2E tests using Python and Playwright;
- CI (GitHub Actions) workflow, executing tests in parallel, generating a detailed test report published as an artifact;

 [Pet store open API](https://petstore.swagger.io/) is used for API testing.
 [Sause Demo site](https://www.saucedemo.com/) is used for UI testing.

# Getting Started

## Prerequisites

- Install [Python latest version](https://www.python.org/downloads/)

## Installation
1. Clone the repository: `git clone <repository-url>`
2. Navigate to the project directory: `cd <project-directory>`
3. Create/activate virtual environment (venv) 
4. Install dependencies from requirements.txt file for venv: `pip install -r requirements.txt`
5. Install Playwright browsers for E2E tests: `playwright install`

## Run tests

Run tests: `python -m pytest -v` or `pytest`
- run specific test: `pytest -v tests/api/test_product_endpoints.py::test_get_all_products_should_return_200`
- run tests from 1 file (fixture): `pytest -v tests/api/test_product_endpoints.py::TestProductEndpoints`
- run tests with category: `pytest -m api`

## Configuration

For local debugging update `driver_settings` section in `config/settings.json` file with the following content:

```json
"driver_settings": {
        "headless": false,
        "slow_mo": 500
    }
```

## Tests output

1. Test result report generates and published on CI by using pytest-html lib (HTML report/JUnit XML)
2. Playwright debug artifacts for failed tests (traces, screenshots, videos)