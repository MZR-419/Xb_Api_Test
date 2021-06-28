from utils import Method
import json
from utils.read_Ini import *
from utils import encryptJson
from utils.Method import ApiRequest
import re
import requests

def get_token():
    url = token_url
    data = encryptJson.EncryptJson.encryptJson(passkey,token_data)
    r=ApiRequest().post_method(url = url, data=data)
    print(r)
    token = r['data']['token']
    return token


dd = get_token()
print(dd)