import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

USERNAME = "YOUR-USERNAME"
TOKEN = "YOUR-TOKEN"
GRAPH_ID = "YOUR-GRAPH-ID"

HEADER = {
    "X-USER-TOKEN": TOKEN
}

today_date = datetime.now().strftime("%Y%m%d")

# TODO 1.To create a user
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

# TODO 2.To Create a New Graph
# GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
# graph_config = {
#     "id": GRAPH_ID,
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "kuro",
# }
#
# response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADER)
# print(response.text)

# TODO 3.To Post a PIXEL on Graph
# PIXEL_POST_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
# post_config = {
#     "date": today_date,
#     "quantity": input("How many Kilometers did you cycle today? "),
# }
#
# response = requests.post(url=PIXEL_POST_ENDPOINT, json=post_config, headers=HEADER)
# print(response.text)

# TODO 4.To Update a Pixel using PUT method
# PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
# update_config = {
#     "quantity": "9.75",
# }
#
# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=update_config, headers=HEADER)
# print(response.text)

# TODO 5.To Delete a Pixel
# PIXEL_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
#
# response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=HEADER)
# print(response.text)


