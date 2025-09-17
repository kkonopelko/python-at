# Introduction
Automation framework with simple API and UI tests on Python.

TAF uses: 
 - test runner - PyTest
 - for API tests - requests lib
 - for UI tests - Playwrite
 - for logging - ???
 - for reporting - ???

[Open API](https://todo.pixegami.io/docs#/) was used for api autotests.
[Fake store open API](https://fakestoreapi.com/docs) is used for API testing.
[Pet store open API](https://petstore.swagger.io/) is used for API testing.

## Prerequisites

Install [Python latest version](https://www.python.org/downloads/)

## Usefull commands:

- For running tests use: `python -m pytest -v` or `pytest`
- run specific test: `pytest -v tests/api/test_product_endpoints.py::test_get_all_products_should_return_200`
- run tests from 1 file (fixture): `pytest -v tests/api/test_product_endpoints.py::TestProductEndpoints`