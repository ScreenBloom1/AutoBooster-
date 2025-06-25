import requests

url = "https://prod-api.lolz.live/threads//bump"

headers = {"accept": "application/json"}

response = requests.post(url, headers=headers)

print(response.text)
