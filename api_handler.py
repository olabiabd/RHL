import requests

class APIHandler:
    def __init__(self, base_url, api_key, subscription_key):
        self.base_url = base_url
        self.api_key = api_key
        self.subscription_key = subscription_key

    def get_headers(self, endpoint, method):
        headers = {
            "TT-Api-Key": self.api_key,
            "Cache-Control": "no-cache",
            "Ocp-Apim-Subscription-Key": self.subscription_key,
        }
        if method == "POST" and ("vehicles" in endpoint or "time" in endpoint):
            headers["Content-Type"] = "application/json-patch+json"
        elif method == "POST":
            headers["Content-Type"] = "application/json"
        return headers

    def request(self, endpoint, method="GET", data=None):
        url = f"{self.base_url}{endpoint}"
        headers = self.get_headers(endpoint, method)
        response = requests.request(method, url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()
