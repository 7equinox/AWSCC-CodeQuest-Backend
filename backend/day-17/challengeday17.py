import requests

base_url = "https://jsonplaceholder.typicode.com/"

resource_path = "posts"

response = requests.get(base_url + resource_path)

print("Request successful") if response.status_code == 200 else print("Request failed")

print()

# list of posts
print(response.json()) if response.status_code == 200 else print("cannot print response")