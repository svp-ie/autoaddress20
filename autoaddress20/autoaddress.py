from base64 import b64encode
from requests import request
from time import sleep

from .constants import addressTable, addressType, buldingType

class Autoaddress:

    def __init__(self, api_key, api_url="https://api.autoaddress.ie/2.0/"):
        self.base_url = api_url
        self.api_key = api_key
        self.delay = 0
        #print(f"A bungalow is building type {buldingType.BUNGALOW}")
        #print(f"A residential address is address type {addressType.RESIDENTIAL_ADDRESS_POINT}")

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
    
    def FindAddress(self, query_address, query_addressProfile="Demo5LineV2", query_vanityMode=True, query_AddressElements=False, query_Country="ie"):
        sleep(self.delay)
        url = self.base_url + "FindAddress"
        method = "GET"
        headers = {}
        payload = {"address": query_address,
                   "addressProfileName": query_addressProfile,
                   "vanityMode": query_vanityMode,
                   "addressElements": query_AddressElements,
                   "country": query_Country}
        response = self.request_response(method, url, headers, payload)
        if response.status_code == '429':
            self.delay =+ 0.1
            self.FindAddress(self, query_address, query_addressProfile=query_addressProfile, query_vanityMode=query_vanityMode, query_AddressElements=query_AddressElements, query_Country=query_Country)
        else:
            self.address = response.text

if __name__ == "__main__":
    #print(f"A bungalow is building type {buldingType.BUNGALOW}")
    #print(f"A residential address is address type {addressType.RESIDENTIAL_ADDRESS_POINT}")
    print("Running AutoAddress 2.0 API")