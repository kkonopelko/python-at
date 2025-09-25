# Introduction
Automation framework with simple API/UI tests on Python for learning purpose.
 - [Pet store open API](https://petstore.swagger.io/) is used for API testing.
 - [Web site](https://petstore.swagger.io/) is used for UI testing.

TAF libraries/frameworks: 
 - test runner - PyTest
 - for API tests - requests lib
 - for UI tests - Playwrite
 - for logging - ???
 - for reporting - ???


# Getting Started

## Prerequisites

Install [Python latest version](https://www.python.org/downloads/)

## Run tests

1. Activate venv (at the begining of the line now you will see (venv)): 
`.\venv\Scripts\activate` or `path to env folder\venv\Scripts\activate`

2. Run tests: `python -m pytest -v` or `pytest`
- run specific test: `pytest -v tests/api/test_product_endpoints.py::test_get_all_products_should_return_200`
- run tests from 1 file (fixture): `pytest -v tests/api/test_product_endpoints.py::TestProductEndpoints`
- run tests with category: `pytest -m category_name`