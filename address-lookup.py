from autoaddress20 import Autoaddress

api_key = "insert dev key here"        # Development key
#api_key = "insert prod key here"       # Production key

a = Autoaddress(api_key)
a.FindAddress("insert test address element here")
print(a.address)

