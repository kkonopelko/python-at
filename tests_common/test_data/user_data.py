from models.user_credentials import UserCredentials

standard_user = UserCredentials(
    username="standard_user",
    password="secret_sauce"
)

locked_out_user = UserCredentials(
    username="locked_out_user",
    password="secret_sauce"
)