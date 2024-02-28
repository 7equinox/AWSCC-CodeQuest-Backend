import requests

api_endpoint = "https://jsonplaceholder.typicode.com/posts"

# set custom header
header = {
    "User-Agent": "MyApp/1.0",
}

# send the get request
response = requests.get(api_endpoint, headers=header)

# inspect the response
print(f"HTTP status code: {response.status_code}")
print("Response Headers: ")
for key, value in response.headers.items():
    print(f"{key}: {value}")
print(f"Response Content: {response.text}")

# prepare data for post request
data = {
    "title": "this is a new title",
    "body": "this is a new body"
}

# send a post request
post_response = requests.post(api_endpoint, json=data)

print(f"HTTP status code: {post_response.status_code}")
print(f"Response Content: {post_response.text}")