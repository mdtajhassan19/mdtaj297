
import requests

url = 'https://reqres.in/api/users'
body = {
    "name": "morpheus",
    "job": "leader"
}
header = 'application/json'
status_code = 201

response = requests.post(url, json=body, verify=False)
print(f"{response.status_code} Is response code.")
assert status_code == response.status_code

