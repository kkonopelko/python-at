#region: Pet store Api URL's
PETSTORE_BASE_URL = "https://petstore.swagger.io/v2"

PET_URL = f"{PETSTORE_BASE_URL}/pet"
GET_PETS_BY_STATUS_URL = lambda status: f"{PET_URL}/findByStatus?status={status}"
GET_PET_BY_ID_URL = lambda id: f"{PET_URL}/{id}"

STORE_ORDER_URL = f"{PETSTORE_BASE_URL}/store/order"
STORE_ORDER_BY_ID_URL = lambda id: f"{STORE_ORDER_URL}/{id}"
#endregion