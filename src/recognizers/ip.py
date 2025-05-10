import socket
import requests

def is_ip(address: str) -> bool:
    """
    Check if the given string is a valid IP address.
    """
    try:
        socket.inet_aton(address)
        return True
    except socket.error:
        return False

def lookup_ip(ip: str) -> dict:
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        return {
            "ip": ip,
            "country": response.json()["country"],
            "region": response.json()["regionName"],
            "city": response.json()["city"],
            "zip": response.json()["zip"],
            "lat": response.json()["lat"],
            "lon": response.json()["lon"],
            "isp": response.json()["isp"],
            "org": response.json()["org"],
            "as": response.json()["as"],
            "query": response.json()["query"],
        }
    except requests.exceptions.RequestException:
        return None
        