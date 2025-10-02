from pages.login_page import LoginPage

def test_valid_login(browser_context):

    # arrange
    user_credentials = {
        "username": "standard_user",
        "password": "secret_sauce"
    }

    page = browser_context.new_page()
    login_page = LoginPage(page)

    # Navigate to login page
    login_page.load()

    # Perform login
    login_page.login(user_credentials["username"], user_credentials["password"])

    # Verify success
    success_message = login_page.get_success_message()
    assert "Logged In Successfully" in success_message