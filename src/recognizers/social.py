import requests
from typing import Dict
import time
import random

def lookup_social(username: str) -> Dict[str, str]:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'DNT': '1',
    }

    services = {
        "Dev.To": {
            "url": f"https://dev.to/{username}",
            "exists_pattern": lambda r: r.status_code == 200 and "This account doesn't exist" not in r.text
        },
        "Instagram": {
            "url": f"https://www.instagram.com/{username}/",
            "exists_pattern": lambda r: r.status_code == 200 and "Sorry, this page isn't available." not in r.text
        },
        "GitHub": {
            "url": f"https://github.com/{username}",
            "exists_pattern": lambda r: r.status_code == 200
        },
        "Reddit": {
            "url": f"https://www.reddit.com/user/{username}/about.json",
            "exists_pattern": lambda r: r.status_code == 200 and "error" not in r.json()
        },
        "Youtube": {
            "url": f"https://www.youtube.com/@{username}",
            "exists_pattern": lambda r: r.status_code == 200 and "This page isn't available" not in r.text
        }
    }

    results = {}
    session = requests.Session()
    
    for site, config in services.items():
        try:
            time.sleep(random.uniform(0.5, 1.5))
            
            response = session.get(
                config["url"],
                headers=headers,
                timeout=10,
                allow_redirects=True
            )
            
            exists = config["exists_pattern"](response)
            results[site] = "yes" if exists else "no"
            
        except requests.RequestException as e:
            results[site] = f"error: {str(e)}"
        except Exception as e:
            results[site] = f"error: unexpected - {str(e)}"
    
    return results
