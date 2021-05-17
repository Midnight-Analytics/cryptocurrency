import requests
import json

class BSCSCAN(object):


  def __init__(self):
    

    with open('keys.json') as f:
      self.API_KEY = json.load(f)['bscscan']


  def total_supply(self, token):
      """
      Gets the total token supply from the BSCSCAN API
      """
      url = f"https://api.bscscan.com/api?module=stats&action=tokensupply&contractaddress={token}&apikey={self.API_KEY}"
          
      data = requests.get(url)
      data = data.json()
      
      if data['status'] == '1':
          
          return data['result']
      else:
          return "Bad Call"

