import requests

def get_geolocation(api_key, ip):
    try:
        response = requests.get(f'http://api.ipstack.com/{ip}?access_key={api_key}')
        data = response.json()
        return data
    except Exception as e:
        print(f"Error getting geolocation: {e}")
        return None

def print_geolocation_info(geolocation_data):
    if geolocation_data:
        print(f'IP Address: {geolocation_data["ip"]}')
        print(f'Location: {geolocation_data["city"]}, {geolocation_data["region_name"]}, {geolocation_data["country_name"]}')
        print(f'Coordinates: {geolocation_data["latitude"]}, {geolocation_data["longitude"]}')
    else:
        print('Unable to fetch geolocation information.')

def main():
    # Replace 'YOUR_API_KEY' with your actual ipstack API key
    api_key = 'ff2b70110e09b32c788f2709f22a630a'

    # Replace 'YOUR_PUBLIC_IP' with the public IP address you want to check
    public_ip = '83.26.234.201'

    # Get geolocation based on IP address
    geolocation_data = get_geolocation(api_key, public_ip)

    # Print geolocation information
    print_geolocation_info(geolocation_data)

if __name__ == '__main__':
    main()
