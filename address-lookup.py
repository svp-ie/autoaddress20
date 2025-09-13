from autoaddress20 import Autoaddress
from os import getenv
from dotenv import load_dotenv

load_dotenv()
api_key = getenv('AUTOADDRESS_APIKEY_DEV')        # Development key
#api_key = getenv('AUTOADDRESS_APIKEY_PROD')      # Production key

a = Autoaddress(api_key)
a.FindAddress(getenv('TEST_ADDRESS'))
print(a.address)

