#this script lets you access the blacknet (BlackCoin IBO) API without a browser using the requests Python module

import requests
import sys

class Interface():
    def __init__(self):
        self.post = False
        self.arg_array = None
        self.link = None
        self.parameter = None
        self.command = None
        self.r = None

    def getargs(self):
        print ('Number of arguments:', len(sys.argv), 'arguments.')
        print ('Argument List:', str(sys.argv))

        try:
            self.command = sys.argv[1]

            try:
                self.arg_array = sys.argv
                del self.arg_array[:2]
            except:
                self.arg_array = None

        except:

            entry = input("No argument detected, please insert command manually\n").split()
            self.command = entry[0]
            print ("entry",entry)
            print("self.command", self.command)

            try:
                self.arg_array = entry
                del self.arg_array[:1]
            except:
                self.arg_array = None


    def go(self):

        if self.command == "stake":
            self.post = True
            mnemonic = " ".join(self.arg_array)
            self.parameter = "staker/start/{}".format(mnemonic)

        elif self.command == "stakestop":
            self.post = True
            mnemonic = " ".join(self.arg_array)
            self.parameter = "staker/stop/{}".format(mnemonic)

        elif self.command == "mnemonicinfo":
            mnemonic = self.arg_array[0]
            self.parameter = "mnemonic/info/{}".format(mnemonic)



        elif self.command == "getblock":
            hash = self.arg_array[0]
            try:
                txdetail = self.arg_array[1]
            except:
                txdetail = ""
            self.parameter = "blockdb/get/{}/{}".format(hash, txdetail)

        elif self.command == "getblockhash":
            height = self.arg_array[0]
            self.parameter = "blockdb/getblockhash/{}".format(height)

        elif self.command == "accinfo":
            address = self.arg_array[0]
            self.parameter = "ledger/get/{}".format(address)

        elif self.command == "transfer":
            self.post = True
            mnemonic = " ".join(self.arg_array[0:10])
            fee = self.arg_array[11]
            amount = self.arg_array[12]
            to = self.arg_array[13]
            try:
                message = self.arg_array[14]
            except:
                message = ""
            try:
                encrypted = self.arg_array[15]
            except:
                encrypted = ""
            self.parameter = "transfer/{}/{}/{}/{}/{}/{}".format(mnemonic, fee,amount,to,message,encrypted)

        elif self.command == "burn":
            self.post = True
            mnemonic = " ".join(self.arg_array[0:10])
            fee = self.arg_array[11]
            amount = self.arg_array[12]
            message = self.arg_array[13]
            self.parameter = "burn/{}/{}/{}/{}".format(mnemonic, fee,amount,message)

        elif self.command == "lease":
            self.post = True
            mnemonic = " ".join(self.arg_array[0:10])
            fee = self.arg_array[11]
            amount = self.arg_array[12]
            to = self.arg_array[13]
            self.parameter = "lease/{}/{}/{}/{}".format(mnemonic, fee,amount,to)

        elif self.command == "clease":
            self.post = True
            mnemonic = " ".join(self.arg_array[0:10])
            fee = self.arg_array[11]
            amount = self.arg_array[12]
            to = self.arg_array[13]
            height = self.arg_array[14]
            self.parameter = "cancellease/{}/{}/{}/{}/{}".format(mnemonic, fee,amount,to,height)

        elif self.command == "sign":
            self.post = True
            mnemonic = " ".join(self.arg_array[0:10])
            message = self.arg_array[11]
            self.parameter = "signmessage/{}/{}".format(mnemonic, message)

        elif self.command == "verify":
            account = self.arg_array[11]
            signature = self.arg_array[12]
            message = self.arg_array[13]
            self.parameter = "verifymessage/{}/{}/{}".format(account,signature, message)

        elif self.command == "addpeer":
            address = self.arg_array[0]
            try:
                port = self.arg_array[1]
            except:
                port = ""

            self.parameter = "addpeer/{}/{}".format(address,port)

        elif self.command == "newacc":
            self.parameter = "account/generate"

        elif self.command == "minfo":
            self.post = True
            mnemonic = self.arg_array[0]
            self.parameter = "mnemonic/info/{}".format(mnemonic)

        else:
            print('direct method')
            self.parameter = self.command

        self.link = "http://localhost:8283/api/v1/{}".format(self.parameter)
        print (self.link)

        if self.post:
            print("POST method")
            self.r = requests.post(self.link)

        else:
            print("GET method")
            self.r = requests.get(self.link)

        #text
        #status_code
        #reason


if __name__ == "__main__":
    interface = Interface()
    interface.getargs()
    interface.go()
    print (interface.r.text)
