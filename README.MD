# Introduction
Automation framework with simple API and UI tests on Python.

TAF uses: 
 - test runner - PyTest
 - for API tests - requests lib
 - for UI tests - Selenium WebDriver
 - for logging -
 - for reporting - 

[Open API](https://todo.pixegami.io/docs#/) was used for api autotests.

## Prerequisites

Install [Python latest version](https://www.python.org/downloads/)

## Usefull commands

1. Create virtual env (at the begining of the project), also in VS Code make shure you are using python interpretator from venv, not global

`python -m venv venv`

2. Activate venv (at the begining of the line now you will see (venv))

`.\venv\Scripts\activate`

3. Create file with dependencies using package manager pip

`pip freeze > requirements.txt`

4. Show installed packages on your visrual env

`pip freeze`

5. For tests install pytest: `pip install pytest`

6. For running tests use:

`python -m pytest -v` or `pytest`