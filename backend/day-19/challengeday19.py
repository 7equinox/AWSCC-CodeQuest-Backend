import requests, json

def get_data_from_api(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: received status code {response.status_code}")
        return None


def print_launch_details(data):
    print(f"Launch Name: {data['name']}")
    print(f"Launch Date (UTC): {data['date_utc']}")
    print(f"Rocket ID: {data['rocket']}")
    print(f"Success: {data['success']}")
    print("Crew Members:")
    for crew_member in data['crew']:
        print(f"  - Role: {crew_member['role']}, Crew ID: {crew_member['crew']}")
    print(f"Launchpad ID: {data['launchpad']}")
    print(f"Flight Number: {data['flight_number']}")
    print("Core Details:")
    for core in data['cores']:
        print(f"  - Core ID: {core['core']}")
        print(f"  - Flight: {core['flight']}")
        print(f"  - Gridfins: {core['gridfins']}")
        print(f"  - Legs: {core['legs']}")
        print(f"  - Reused: {core['reused']}")
        print(f"  - Landing Attempt: {core['landing_attempt']}")
        print(f"  - Landing Success: {core['landing_success']}")
        print(f"  - Landing Type: {core['landing_type']}")
        print(f"  - Landpad: {core['landpad']}")
    print(f"Webcast: {data['links']['webcast']}")
    print(f"Wikipedia: {data['links']['wikipedia']}")
    

# Get the data from the API
api_url = "https://api.spacexdata.com/v5/launches/latest"
data = get_data_from_api(api_url)

# If data was successfully retrieved, print the launch details
if data is not None:
    print_launch_details(data)