from base64 import b64encode
from requests import request

from .constants import addressTable, addressType, buldingType

class Autoaddress:

    def __init__(self, api_key):
        self.base_url = "https://api.autoaddress.ie/2.0/"
        self.api_key = api_key
        print(f"A bungalow is building type {buldingType.BUNGALOW}")
        print(f"A residential address is address type {addressType.RESIDENTIAL_ADDRESS_POINT}")

    def request_response(self, method, url, end_point_headers, endpoint_payload):
        headers = {'User-Agent': 'svp_address_finder_app',
                   'Accept-Encoding': 'gzip, deflate', 
                   'Accept': '*/*', 
                   'Connection': 'keep-alive'}
        headers.update(end_point_headers)
        payload = {'key': self.api_key}
        payload.update(endpoint_payload)
        if method == "GET":
            response = request(method, url, headers=headers, params=payload)
        elif method == "POST":
            response = request(method, url, headers=headers, data=payload)
        return response
    
    def FindAddress(self, query_address, query_addressProfile="Demo5LineV2", query_vanityMode=True):
        url = self.base_url + "FindAddress"
        method = "GET"
        headers = {}
        payload = {"address": query_address,
                   "addressProfile": query_addressProfile,
                   "vanityMode": query_vanityMode}
        response = self.request_response(method, url, headers, payload)
        self.address = response.text

if __name__ == "__main__":
    print(f"A bungalow is building type {buldingType.BUNGALOW}")
    print(f"A residential address is address type {addressType.RESIDENTIAL_ADDRESS_POINT}")