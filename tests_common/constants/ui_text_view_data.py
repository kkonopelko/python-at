# Inventory page
INVENTORY_PAGE_TITLE_TEXT = "Products"

# Login page
USERNAME_ERROR_MESSAGE = "Epic sadface: Username is required"
PASSWORD_ERROR_MESSAGE = "Epic sadface: Password is required"
USERNAME_AND_PASSWORD_DONOT_MATCH_ERROR_MESSAGE = "Epic sadface: Username and password do not match any user in this service"
USER_LOCKED_OUT_ERROR_MESSAGE = "Epic sadface: Sorry, this user has been locked out."
USER_NOT_LOGGED_IN_ERROR_MESSAGE = lambda relativeUri: f"Epic sadface: You can only access '/{relativeUri}' when you are logged in."

# Checkout complete page
CHECKOUT_COMPLETE_HEADER_TEXT = "Thank you for your order!"
CHECKOUT_COMPLETE_TEXT = "Your order has been dispatched, and will arrive just as fast as the pony can get there!"

# Checkout overview page
PAYMENT_INFORMATION_TEXT = "SauceCard #31337"
SHIPPING_INFORMATION_TEXT = "Free Pony Express Delivery!"
ITEM_TOTAL_TEXT = lambda item_total: f"Item total: ${item_total:.2f}"
TAX_TEXT = lambda tax: f"Tax: ${tax:.2f}"
TOTAL = lambda item_total, tax: f"Total: ${item_total + tax:.2f}"

# Checkout information page
FIRST_NAME_ERROR_MESSAGE = "Error: First Name is required"
LAST_NAME_ERROR_MESSAGE = "Error: Last Name is required"
POSTAL_CODE_ERROR_MESSAGE = "Error: Postal Code is required"