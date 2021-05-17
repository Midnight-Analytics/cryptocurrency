import requests
import json



class BitQuery(object):


  def __init__(self):
    

    with open('keys.json') as f:
      self.API_KEY = json.load(f)['bitquery']


    self.results = self.run_query()
    self.coins = self.filter_WBNB(self.results)



  def run_query(self, volume=10):  
      """
      A simple function to use requests.post to make the API call.
      """

      query = """
            {
              ethereum(network: bsc) {
                arguments(
                  smartContractAddress: {is: "0xBCfCcbde45cE874adCB698cC183deBcF17952812"}
                  smartContractEvent: {is: "PairCreated"}
                  argument: {not: "pair"}
                  options: {desc: "block.height", limit: """ + str(volume) + """}
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



      headers = {'X-API-KEY': self.API_KEY}
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


if __name__ == '__main__':

  test = BitQuery()