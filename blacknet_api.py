#this script lets you access the blacknet (BlackCoin IBO) API without a browser using the requests Python module

import requests
import sys

def getargs():
    print ('Number of arguments:', len(sys.argv), 'arguments.')
    print ('Argument List:', str(sys.argv))

    try:
        command = sys.argv[1]

        try:
            arg_array = sys.argv
            del arg_array[:2]
        except:
            arg_array = None

    except:

        entry = input("No argument detected, please insert command manually\n").split()
        command = entry[0]
        print ("entry",entry)
        print("command", command)

        try:
            arg_array = entry
            del arg_array[:1]
        except:
            arg_array = None

    print(command, arg_array)
    return command, arg_array

command, arg_array = getargs()


if command == "stake":
    mnemonic = " ".join(arg_array)
    parameter = "staker/start/{}".format(mnemonic)

elif command == "stakestop":
    mnemonic = " ".join(arg_array)
    parameter = "staker/stop/{}".format(mnemonic)

elif command == "mnemonicinfo":
    mnemonic = arg_array[0]
    parameter = "mnemonic/info/{}".format(mnemonic)



elif command == "getblock":
    hash = arg_array[0]
    try:
        txdetail = arg_array[1]
    except:
        txdetail = ""
    parameter = "blockdb/get/{}/{}".format(hash, txdetail)

elif command == "getblockhash":
    height = arg_array[0]
    parameter = "blockdb/getblockhash/{}".format(height)

elif command == "accinfo":
    address = arg_array[0]
    parameter = "ledger/get/{}".format(address)

elif command == "newacc":
    parameter = "account/generate"

elif command == "minfo":
    mnemonic = arg_array[0]
    parameter = "mnemonic/info/{}".format(mnemonic)

else:
    print('direct method')
    parameter = command

link = "http://localhost:8283/api/v1/{}".format(parameter)
print (link)

methods_get = "peerinfo","nodeinfo","ledger","txpool","getblock","getblockhash", "newacc"
methods_post = "stake","stakestop","minfo"

if command in methods_get:
    print("GET method")
    r = requests.get(link)
    print(r.text, r.status_code, r.reason)

if command in methods_post:
    print("POST method")
    r = requests.post(link)
    print(r.text, r.status_code, r.reason)
