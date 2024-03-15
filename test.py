from better_web3 import Wallet


with open('wallets.txt', 'r') as file:
    wallets = [row.strip() for row in file]


with open('addresses.txt', 'w') as file:
    for wallet in wallets:
        address = Wallet.from_key(wallet).address
        file.write(f'{address}\n')