import requests
import datetime as dt

TOKEN = 'chili895'
USERNAME = 'chili895'
GRAPH_ID = 'graph1'
TODAY = dt.datetime.now()

pixela_endpoint = 'https://pixe.la/v1/users'
user_param = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes',
}

#response = requests.post(pixela_endpoint, json=user_param)


graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'
graph_param = {
    "id": GRAPH_ID,
    'name': 'Cycling Graph',
    'unit': 'KM',
    'type': 'float',
    'color': 'ajisai',
}

headers = {
    'X-USER-TOKEN': TOKEN
}

#response = requests.post(graph_endpoint, json=graph_param, headers=headers)


post_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}'
post_param = {
    'date': TODAY.strftime("%Y%m%d"),
    'quantity': 10,
}
response = requests.post(post_endpoint, json=post_param, headers=headers)
print(response.text)

