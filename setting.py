class Value_EVM_Balance_Checker:

    '''
    Coins checker
    Chains : ethereum | optimism | bsc | polygon | arbitrum | avalanche | fantom | nova | zksync | polygon_zkevm | celo | gnosis | core | harmony | linea | base
    '''

    # Comment out the chain / token if you do not want to check the balance of that chain / token
    evm_tokens = {
        'bsc': [
            '', # BNB
            '0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d', # USDC
            '0x55d398326f99059ff775485246999027b3197955', # USDT
            # '0xe9e7cea3dedca5984780bafc599bd69add087d56', # BUSD
            # '0xB0b84D294e0C75A6abe60171b70edEb2EFd14A1B', # SnBNB
            ],
        'arbitrum': [
            '', # ETH
            '0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9', # USDT
            '0xFF970A61A04b1cA14834A43f5dE4533eBDDB5CC8', # USDC
            # '0x6694340fc020c5e6b96567843da2df01b2ce1eb6', # STG
            # '0x912ce59144191c1204e64559fe8253a0e49e6548', # ARB
            ],
        # 'optimism': [
        #     '', # ETH
        #     '0x7f5c764cbc14f9669b88837ca1490cca17c31607', # USDC
        #     '0x4200000000000000000000000000000000000042', # OP
        #     '0x94b008aa00579c1307b0ef2c499ad98a8ce58e58', # USDT
        #     ],
        # 'polygon': [
        #     '', # MATIC
        #     '0xc2132d05d31c914a87c6611c10748aeb04b58e8f', # USDT
        #     '0x2791bca1f2de4661ed88a30c99a7a9449aa84174', # USDC
        #     ],
        'avalanche': [
            '', # AVAX
            # '0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7', # USDT
            ],
        'ethereum': [
            '', # ETH
            '0xdac17f958d2ee523a2206206994597c13d831ec7', # USDT
            '0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', # USDC
            # '0xaf5191b0de278c7286d6c7cc6ab6bb8a73ba2cd6', # STG
            # '0xb131f4a55907b10d1f0a50d8ab8fa09ec342cd74', # MEME
            ],
        # 'zksync': [
        #     '', # ETH
        #     ],
        # 'nova': [
        #     '', # ETH
        #     ],
        # 'fantom': [
        #     '', # FTM
        #     ],
        # 'polygon_zkevm': [
        #     '', # ETH
        #     ],
        # 'celo': [
        #     '', # CELO
        #     ],
        # 'gnosis': [
        #     '', # xDAI
        #     ],
        # 'harmony': [
        #     '', # ONE
        #     ],
        # 'core': [
        #     '', # CORE
        #     ],
        # 'linea': [
        #     '', # ETH
        #     ],
        'base': [
            '', # ETH
            ],
        'scroll': [
            '', # ETH
            ],
        'mantle': [
        '', # MNT
        ],
    }

    min_token_balance = {
        'chain'     : 'avalanche',
        'coin'      : 'AVAX',
        'amount'    : 0.02 # If the balance is less than this amount, the wallet will be highlighted
    }

    min_value_balance = 0 # If the wallet balance in $ is less than this amount, the wallet will be highlighted