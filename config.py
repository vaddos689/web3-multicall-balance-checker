import asyncio
from core.modules.utils.files import read_txt, load_json
from core.modules.utils.helpers import get_wallet_proxies

max_time_check_tx_status = 100  # seconds. If a transaction does not return a status within this time, it is considered executed


STR_DONE = '✅ '
STR_CANCEL = '❌ '

ERC20_ABI = load_json("core/modules/utils/contracts/erc20.json")
MULTICALL_ABI = load_json("core/modules/utils/contracts/multicall_abi.json")
WALLETS = read_txt("wallets.txt")
PROXIES = read_txt("proxies.txt")

WALLET_PROXIES = get_wallet_proxies(WALLETS, PROXIES)
