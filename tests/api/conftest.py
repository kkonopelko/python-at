# this file is ussually used for pytest fixtures
# all code here will be accessible from all test files in this folder
# define here fixtures with scope for: common login for all tests before and after run, data setup and clean up etc.

import pytest

@pytest.fixture(scope="session", autouse=True)
def before_all_tests_setup_teardown():
    print("Run once before all tests (session setup)")
    yield
    print("Run once after all tests (session teardown)")