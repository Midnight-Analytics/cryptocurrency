import requests


class PancakeSwap(object):

  def __init__(self):
    pass


  def get_token_price(self, address):


    url = f"https://api.pancakeswap.info/api/v2/tokens/{address}"

    r = requests.get(url)

    return r.json()

  

if __name__ == '__main__':

  token = "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82"
  print(PancakeSwap().get_token_price(token))