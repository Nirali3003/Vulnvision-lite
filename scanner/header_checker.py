import requests

def check_headers(url):
    missing = []

    try:
        r = requests.get(url)
        headers = r.headers

        sec_headers = [
            "Content-Security-Policy",
            "X-Frame-Options",
            "X-XSS-Protection",
            "Strict-Transport-Security"
        ]

        for h in sec_headers:
            if h not in headers:
                print(h, "MISSING")
                missing.append(h)
            else:
                print(h, "OK")

    except:
        print("Error")

    return missing
