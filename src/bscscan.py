import requests
import json
from bs4 import BeautifulSoup

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



    
    def get_socials(self, token):

    
        """
        Hits the BscScan website for the corresponding token and returns the social media links for the target token 
        """
        
        url = f"https://bscscan.com/token/{token}"
        
        r = requests.get(url)
        soup = BeautifulSoup(r.content, "html.parser")

        try:

            
            ul_socials = soup.find(class_="list-inline mb-0")
            
            links = []
            
            socials = {
                "token": token,
                "socials": links
                }
            
            for i in ul_socials:
                links.append((i.findChild("a")['href']))
                
            return socials
        except:
            return {"token": token,
            "socials": "No Socials"
            }

if __name__ == '__main__':

    test = BSCSCAN()
    print(test.get_socials('0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'))
    print(test.total_supply('0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82'))


