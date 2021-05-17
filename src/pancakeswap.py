import requests


class PancakeSwap(object):

  def __init__(self):
    pass


  def get_token_price(self, token):


    url = f"https://api.pancakeswap.info/api/v2/tokens/{token}"

    r = requests.get(url)

    return r.json()

  

