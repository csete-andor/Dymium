import socket
import requests

def fetchFrom(domain, file):
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"IP address of {domain}: {ip_address}")
    except socket.gaierror as e:
        print(f"Error resolving IP address for {domain}: {e}")
        ip_address = None
        return e
        

    if ip_address:
        url = f"http://{domain}/{file}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            file_data = response.text
            print("File data retrieved successfully:")
            return file_data, ip_address
        except requests.RequestException as e:
            print(f"Error fetching file data from {url}: {e}")
            return e