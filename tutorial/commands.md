## Usefull commands for start

If you do not use venv for a long time and want to update libraries it is recommended to delete existing venv and create new and restore dependencies.

1. Remove manually venv and pycache from solution folder
2. Create virtual env (at the begining of the project), also in VS Code make shure you are using python interpretator from venv, not global

`python -m venv venv`

3. Activate venv (at the begining of the line now you will see (venv))

`.\venv\Scripts\activate` or `path to env folder\venv\Scripts\activate`

- Deactivate your venv (at the end of working with proj, exit): `deactivate`

. Install dependencies from requirements.txt file for newly created venv: `pip install -r requirements.txt`


### Pip commands:
- Update pip installer: `python -m pip install --upgrade pip`
- Reinstall dependencies (after updating them manually in the file) inside venv: `python -m pip install -r requirements.txt --upgrade`

- Create file with dependencies using package manager pip: `pip freeze > requirements.txt`
- Show installed packages on your virtual env: `pip freeze`
- For tests install pytest: `pip install pytest`

- For running tests use: `python -m pytest -v` or `pytest`