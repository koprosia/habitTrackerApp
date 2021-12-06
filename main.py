import requests
from datetime import datetime

USER_NAME = "yuhuhu123123"
TOKEN = "dshaldiauhelfueba"
GRAPH_ID = "graph1"
TODAY_DATE = datetime.now().strftime("%Y%m%d")

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": USER_NAME,
    "username": TOKEN,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Reading Graph",
    "unit": "Pages",
    "type": "int",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

post_pixel_config = {
    "date": TODAY_DATE,
    "quantity": "20"
}

post_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
# response = requests.post(url=post_pixel_endpoint, json=post_pixel_config, headers=headers)
# print(response.text)

put_pixel_config = {
    "quantity": "100"
}

put_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{TODAY_DATE}"
# response = requests.put(url=put_pixel_endpoint, json = put_pixel_config, headers=headers)
# print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{TODAY_DATE}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)