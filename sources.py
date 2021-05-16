#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
from config import BSCSCAN_API_KEY

class BitQuery(object):


  def __init__(self):


    # Query returns the latest 1000 tokens created with a pairing on PancakeSwap
    self.query = """
            {
              ethereum(network: bsc) {
                arguments(
                  smartContractAddress: {is: "0xBCfCcbde45cE874adCB698cC183deBcF17952812"}
                  smartContractEvent: {is: "PairCreated"}
                  argument: {not: "pair"}
                  options: {desc: "block.height", limit: 1000}
                ) {
                  block {
                    height
                    timestamp {
                      unixtime
            }}
                  reference {
                    address
                    smartContract {
                      currency {
                        name
            }}}}}}
            """

    self.results = self.run_query(self.query)
    self.coins = self.filter_WBNB(self.results)



  def run_query(self, query=None):  
      """
      A simple function to use requests.post to make the API call.
      """

      if query is None:
        query = self.query



      headers = {'X-API-KEY': BSCSCAN_API_KEY}
      request = requests.post('https://graphql.bitquery.io/',
                              json={'query': query}, headers=headers)
      if request.status_code == 200:
        print(request.status_code)
        return request.json()
          
      else:
        raise Exception('Query failed and return code is {}.      {}'.format(request.status_code,
                          query))


  def filter_WBNB(self, data=None):


    if data is None:
      data = self.data

    blocks = data['data']['ethereum']['arguments']
    
    filtered = [x for x in blocks if x['reference']['smartContract']['currency']['name'] != 'Wrapped BNB']
    
    addresses = [x['reference']['address'] for x in filtered]
    return addresses




class BSCSCAN(object):


  def total_supply(token, API_KEY):
      """
      Gets the total token supply from the BSCSCAN API
      """
      url = f"https://api.bscscan.com/api?module=stats&action=tokensupply&contractaddress={token}&apikey={API_KEY}"
          
      data = requests.get(url)
      data = data.json()
      
      if data['status'] == '1':
          
          return data['result']
      else:
          return "Bad Call"



class PancakeSwap(object):

  pass


if __name__ == '__main__':

  inst = BitQuery()
  print(inst.coins)

  