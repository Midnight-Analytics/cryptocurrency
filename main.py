from src import pancakeswap
from src.pancakeswap import PancakeSwap
from src.bscscan import BSCSCAN
from src.bitquery import BitQuery 


tokens = BitQuery().get_tokens(300)



for token in tokens:

    print(token)
    print("Pancake")
    print(PancakeSwap().get_token_price(token))
    print("Total Supply")
    print(BSCSCAN().total_supply(token))
    print("Socials")
    print(BSCSCAN().get_socials(token))

    print("""
        *************************
        End of token info 
        *************************
        """)
