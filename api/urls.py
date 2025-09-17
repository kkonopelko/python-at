#region Task Api URL's
BASE_URL = "https://todo.pixegami.io"

CREATE_TASK_URL = f"{BASE_URL}/create-task"
GET_TASK_BY_ID_URL = lambda id: f"{BASE_URL}/get-task/{id}"
#endregion

#region: Pet store Api URL's
PETSTORE_BASE_URL = "https://petstore.swagger.io/v2"

GET_PETS_BY_STATUS_URL = lambda status: f"{PETSTORE_BASE_URL}/pet/findByStatus?status={status}"
GET_PET_BY_ID_URL = lambda id: f"{PETSTORE_BASE_URL}/pet/{id}"
#endregion

