#this script lets you access the blacknet (BlackCoin IBO) API without a browser using the requests Python module

import requests
command = input("Select command ")

if command == "stake":
    mnemonic = input("Enter mnemonic ")
    parameter = "staker/start/{}".format(mnemonic)

elif command == "mnemonicinfo":
    mnemonic = input("Enter mnemonic ")
    parameter = "mnemonic/info/{}".format(mnemonic)

else:
    parameter = command

link = "http://localhost:8283/api/v1/{}".format(parameter)
print (link)

methods_get = "peerinfo","nodeinfo","ledger","txpool"
methods_post = "stake","mnemonicinfo"

if command in methods_get:
    print("GET method")
    r = requests.get(link)
    print(r.text, r.status_code, r.reason)

if command in methods_post:
    print("POST method")
    r = requests.post(link)
    print(r.text, r.status_code, r.reason)
