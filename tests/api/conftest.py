# this file is ussually used for pytest fixtures
# all code here will be accessible for tests in this root directory.
# use conftest.py for fixtures shared across multiple test files: global data seeding and clean up etc.

import pytest

@pytest.fixture(scope="session", autouse=True)
def before_all_tests_setup_teardown():
    print("Run once before all tests (session setup)")
    yield
    print("Run once after all tests (session teardown)")