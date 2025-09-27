from config.config_manager import config

#region: Pet store Api URL's
PETSTORE_BASE_URL = config.store_api_base_url

PET_URL = f"{PETSTORE_BASE_URL}/pet"
GET_PETS_BY_STATUS_URL = lambda status: f"{PET_URL}/findByStatus?status={status}"
GET_PET_BY_ID_URL = lambda id: f"{PET_URL}/{id}"

STORE_ORDER_URL = f"{PETSTORE_BASE_URL}/store/order"
STORE_ORDER_BY_ID_URL = lambda id: f"{STORE_ORDER_URL}/{id}"
#endregion

#region: Users API service URL's
USERS_URL = "api/users"
USER_BY_ID_URL = lambda id:f"{USERS_URL}/{id}"
#endregion