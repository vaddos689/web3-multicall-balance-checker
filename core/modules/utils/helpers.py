import math

from eth_account import Account


def get_wallet_proxies(wallets, proxies):
    return {wallet: proxy for wallet, proxy in zip(wallets, proxies)}


def decimalToInt(qty, decimal):
    return float(qty / 10**decimal)


def round_to(num, digits=3):
    try:
        if num == 0: return 0
        scale = int(-math.floor(math.log10(abs(num - int(num))))) + digits - 1
        if scale < digits: scale = digits
        return round(num, scale)
    except:
        return num


def is_private_key(key):
    try:
        return Account().from_key(key).address
    except:
        return False
