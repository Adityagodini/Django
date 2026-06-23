import requests
import json
BASE_URL = "http://127.0.0.1:8000/"
ENDPOINT = "api/"
def resource(id):
    data = requests.get(BASE_URL + ENDPOINT+id+'/')
    print(data)
    print(data.status_code)
    print(data.json())

id = input("Enter a id: ")
resource(id)
