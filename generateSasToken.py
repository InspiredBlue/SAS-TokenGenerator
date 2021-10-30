from base64 import b64encode, b64decode
from hashlib import sha256
from time import time
from urllib import parse
from hmac import HMAC


def generate_sas_token(uri, key, policy_name, expiry=3600):
    ttl = time() + expiry
    sign_key = "%s\n%d" % ((parse.quote_plus(uri)), int(ttl))
    #print (sign_key)
    signature = b64encode(HMAC(b64decode(key), sign_key.encode('utf-8'), sha256).digest())

    rawtoken = {
        'sr' :  uri,
        'sig': signature,
        #'se' : str(int(ttl))
    }

    if policy_name is not None:
        rawtoken['skn'] = policy_name

    rawtoken['se'] = str(int(ttl))

    return 'SharedAccessSignature ' + parse.urlencode(rawtoken)

iothubaddress = " " # ID do IotHub
device_id = " " # ID do device 
shared_access_key = " " # Dentro da Connection String

resource_uri = iothubaddress + ".azure-devices.net" + "/" + "devices" + "/" +  device_id
policy_name = None # Either None / iothubowner / etc... 

uri = resource_uri
expiry = 3600 # In seconds
policy = None # Either None / iothubowner / etc... 

print (generate_sas_token(uri, shared_access_key, policy, expiry))