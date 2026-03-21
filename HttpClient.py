import time
import requests
 
class HttpClient:
    def __init__(self, retries=3, backoff=1):
        self.retries = retries
        self.backoff = backoff

    def get(self, url):
        for attempt in range(self.retries):
            try:
                resp = requests.get(url)

            except requests.RequestException:
                time.sleep(self.backoff)
                continue

            else:
                if resp.status_code == 200:
                    return resp
                
                time.sleep(self.backoff)


        return None
                

            

if __name__ == "__main__":
    client = HttpClient(retries=3, backoff=0.5)
    resp = client.get("https://jsonplaceholder.typicode.com/posts/1")
    
    if resp:
        print(f"OK: {resp.status_code}")
    else:
        print("FAILED after all retries")