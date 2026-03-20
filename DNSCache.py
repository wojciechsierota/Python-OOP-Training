import socket
import time

class DnsCache:
    def __init__(self, ttl):
        self.ttl = ttl
        self._cache = {}


    def lookup(self, domain):
        now = time.time()
        if domain in self._cache:
            cached_ip, expiry = self._cache[domain]
            if expiry > now:
                print(f"DEBUG: Cache hit for {domain}")
                return cached_ip
            
        try:
            ip = socket.gethostbyname(domain)
            expiry = now + self.ttl
            self._cache[domain] = (ip, expiry)
            return ip
        
        except socket.gaierror:
            return None
 
if __name__ == "__main__":
    cache = DnsCache(ttl=5)
    ip1 = cache.lookup("example.com")
    print(ip1)
    time.sleep(1)
    ip2 = cache.lookup("example.com")
    print(ip2)
    time.sleep(5)
    ip3 = cache.lookup("example.com")
    print(ip3)

    