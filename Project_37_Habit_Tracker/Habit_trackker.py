import requests
import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
USERNAME = "jojo7siva"
TOKEN = "ksjijwjndwndwdw"

# TODO 1 : Creating Pixela account
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)



# TODO 2 : Create a graph definition

GRAPH_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs"
GRAPH_ID = "graph1"
graph_params = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}

# cycling_graph1_response = requests.post(url=GRAPH_ENDPOINT, json=graph_params, headers=headers)
# print(cycling_graph1_response.text)



# TODO 3 : Posting values to graph
today = datetime.datetime.now()
ADD_PIXEL_ENDPOINT = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
pixel_params = {
    "date": today.strftime('%Y%m%d'),
    "quantity": input("How many kilometers did you cycle today?: ")
}
add_response = requests.post(url=ADD_PIXEL_ENDPOINT, json=pixel_params, headers=headers)
print(add_response.text)

