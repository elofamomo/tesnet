from web3 import Web3
from eth_account import Account
import csv
Account.enable_unaudited_hdwallet_features()
num_wallet = int(input("Enter number of wallets: "))

for _ in range(num_wallet):
    acct, mnemonic = Account.create_with_mnemonic()

    fieldnames = ['phrase', 'address','private_key']
    rows = [
        {   
            'phrase':mnemonic,
            'address':acct.address,
            'private_key':acct.key.hex(),

        }
    ]

    with open('WalletData.csv', 'a', encoding='UTF8', newline='') as f1:
        writer = csv.DictWriter(f1, fieldnames=fieldnames)
        writer.writerows(rows)
    



