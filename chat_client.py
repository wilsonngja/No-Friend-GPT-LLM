import requests
from requests.exceptions import RequestException
import json

# The endpoint you're sending the POST request to
url = 'http://127.0.0.1:8000/query_response/'


while True:
    query = input("Patient:")
    query_data = json.dumps({"text":query})

    try:
        res = requests.post(url, data=query_data)
        if res.status_code == 200:
            # Do something with the successful response
            json_response = res.json()  # This is a dictionary
            print("ChatDoctor: " + json_response["response"])
        else:   
            print(f"Error: {res.status_code}, {res.text}")
    except RequestException as e:
        print(f"Request failed: {e}")