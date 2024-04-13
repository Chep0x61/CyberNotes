import requests

def try_endpoint(ip):
    urls = [
        "/robots.txt",
        "/sitemap.xml",
        "/sitemap"
    ]

    for endpoint in urls:
        url = f"http://{ip}{endpoint}"
        try:
            response = requests.head(url)
            if response.status_code == 200:
                print(f"\033[0;32m 200 {endpoint} File Found => {url} \033[0m")  # Green
            else:
                print(f"\033[0;31m {response.status_code} {endpoint} File Not Found\033[0m")  # Red
        except requests.RequestException as e:
            print(f"\033[0;31m{url}: Error during request: {e}\033[0m")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "<ip_address:port>")
        sys.exit(1)

    ip = sys.argv[1]
    try_endpoint(ip)
