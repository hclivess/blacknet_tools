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

elif command == "transfer":
    mnemonic = " ".join(arg_array[0:10])
    fee = arg_array[11]
    amount = arg_array[12]
    to = arg_array[13]
    try:
        message = arg_array[14]
    except:
        message = ""
    try:
        encrypted = arg_array[15]
    except:
        encrypted = ""
    parameter = "transfer/{}/{}/{}/{}/{}/{}".format(mnemonic, fee,amount,to,message,encrypted)

elif command == "burn":
    mnemonic = " ".join(arg_array[0:10])
    fee = arg_array[11]
    amount = arg_array[12]
    message = arg_array[13]
    parameter = "burn/{}/{}/{}/{}".format(mnemonic, fee,amount,message)

elif command == "lease":
    mnemonic = " ".join(arg_array[0:10])
    fee = arg_array[11]
    amount = arg_array[12]
    to = arg_array[13]
    parameter = "lease/{}/{}/{}/{}".format(mnemonic, fee,amount,to)

elif command == "clease":
    mnemonic = " ".join(arg_array[0:10])
    fee = arg_array[11]
    amount = arg_array[12]
    to = arg_array[13]
    height = arg_array[14]
    parameter = "cancellease/{}/{}/{}/{}/{}".format(mnemonic, fee,amount,to,height)

elif command == "sign":
    mnemonic = " ".join(arg_array[0:10])
    message = arg_array[11]
    parameter = "signmessage/{}/{}".format(mnemonic, message)

elif command == "verify":
    mnemonic = " ".join(arg_array[0:10])
    account = arg_array[11]
    signature = arg_array[12]
    message = arg_array[13]
    parameter = "verifymessage/{}/{}/{}".format(account,signature, message)

elif command == "addpeer":
    address = arg_array[0]
    try:
        port = arg_array[1]
    except:
        port = ""

    parameter = "addpeer/{}/{}".format(address,port)

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

methods_get = "peerinfo","nodeinfo","ledger","txpool","getblock","getblockhash", "newacc","verify","addpeer"
methods_post = "stake","stakestop","minfo","transfer","burn","lease","clease","sign"

if command in methods_get:
    print("GET method")
    r = requests.get(link)
    print(r.text, r.status_code, r.reason)

if command in methods_post:
    print("POST method")
    r = requests.post(link)
    print(r.text, r.status_code, r.reason)
