import json
import tkinter as tk
import requests
import os

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master

        self.grid()
        self.create_widgets()


    def create_widgets(self):
        """
        self.mnemonic_label = tk.Label(self)
        self.mnemonic_label["text"] = "Mnemonic: "
        self.mnemonic_label.pack(side="top")

        self.mnemonic = tk.Label(self)
        self.mnemonic["text"] = wallet.mnemonic
        #self.address["command"] = self.say_hi
        self.mnemonic.pack(side="top")
        """

        self.address_label = tk.Label(self)
        self.address_label["text"] = "Address: "
        self.address_label.grid(row=0, column=0, sticky='', pady=5, padx=5)

        self.address = tk.Label(self)
        self.address["text"] = wallet.address
        #self.address["command"] = self.say_hi
        self.address.grid(row=0, column=1, sticky='W', pady=5, padx=5)

        self.publickey_label = tk.Label(self)
        self.publickey_label["text"] = "Public Key: "
        self.publickey_label.grid(row=2, column=0, sticky='', pady=5, padx=5)

        self.publickey = tk.Label(self)
        self.publickey["text"] = wallet.publickey
        #self.address["command"] = self.say_hi
        self.publickey.grid(row=2, column=1, sticky='W', pady=5, padx=5)

        self.balance_label = tk.Label(self)
        self.balance_label["text"] = "Balance: "
        self.balance_label.grid(row=4, column=0, sticky='', pady=5, padx=5)

        self.balance = tk.Label(self)
        self.balance["text"] = wallet.balance
        #self.address["command"] = self.say_hi
        self.balance.grid(row=4, column=1, sticky='W', pady=5, padx=5)

        self.recipient_label = tk.Label(self)
        self.recipient_label["text"] = "Recipient: "
        self.recipient_label.grid(row=5, column=0, sticky='', pady=5, padx=5)
        self.recipient_value = tk.StringVar()
        self.recipient_value.set(wallet.address)
        self.recipient = tk.Entry(self, textvariable=self.recipient_value, width=70)
        self.recipient.grid(row=5, column=1, sticky='W', pady=5, padx=5)

        self.amount_label = tk.Label(self)
        self.amount_label["text"] = "Amount: "
        self.amount_label.grid(row=6, column=0, sticky='', pady=5, padx=5)
        self.amount_label = tk.StringVar()
        self.amount_label.set(0)
        self.amount = tk.Entry(self, textvariable=self.amount_label, width=70)
        self.amount.grid(row=6, column=1, sticky='W', pady=5, padx=5)
        #self.address["command"] = self.say_hi

        self.send = tk.Button(self, text="transfer", fg="green",
                              command=operations.send)
        self.send.grid(row=7, column=1, sticky='WE', pady=5, padx=5)

        self.stake = tk.Button(self, text="Stake", fg="green",
                              command=operations.stake)
        self.stake.grid(row=8, column=1, sticky='WE', pady=5, padx=5)

        self.stop_stake = tk.Button(self, text="Stop Staking", fg="green",
                              command=operations.stopstake)
        self.stop_stake.grid(row=9, column=1, sticky='WE', pady=5, padx=5)

        self.refresh = tk.Button(self, text="refresh", fg="red",
                              command=operations.refresh)
        self.refresh.grid(row=10, column=1, sticky='WE', pady=5, padx=5)

        self.quit = tk.Button(self, text="quit", fg="red",
                              command=self.master.destroy)
        self.quit.grid(row=11, column=1, sticky='WE', pady=5, padx=5)



class Wallet():
    def __init__(self):

        if not os.path.exists("secret.json"):
            self.generate()

        with open("secret.json", 'r') as keyfile:
            self.wallet = json.loads(keyfile.read())

        self.mnemonic = self.wallet['mnemonic']
        self.address = self.wallet['address']
        self.publickey = self.wallet['publicKey']

        self.getbalance()

    def generate(self):
        with open("secret.json", 'w') as keyfile:
            keyfile.write(operations.newacc())

    def getbalance(self):
        try:
            self.balance_request = json.loads(requests.get("http://localhost:8283/api/v1/ledger/get/{}".format(self.address)).text)
            self.seq = self.balance_request["seq"]
            self.balance = self.balance_request["balance"]
            self.staking_balance = self.balance_request["stakingBalance"]
        except:
            self.seq = 0
            self.balance = 0
            self.staking_balance = 0

class Operations():
    def send(self):
        print(requests.post("http://localhost:8283/api/v1/transfer/{}/{}/{}/{}".format(wallet.mnemonic,100000,app.amount.get(),app.recipient.get())).text)
    def stake(self):
        print(requests.post("http://localhost:8283/api/v1/staker/start/{}".format(wallet.mnemonic)).text)
    def stopstake(self):
        print(requests.post("http://localhost:8283/api/v1/staker/start/{}".format(wallet.mnemonic)).text)
    def newacc(self):
        result = requests.get("http://localhost:8283/api/v1/account/generate").text
        return result
    def refresh(self):
        wallet.getbalance()
        app.balance["text"] = wallet.balance


if __name__ == "__main__":
    root = tk.Tk()
    root.wm_title("Blacknet API Wallet")
    operations = Operations()
    wallet = Wallet()
    app = Application(master=root)


    app.mainloop()


