import requests
from bs4 import BeautifulSoup

class CoinMarketCap:
    BASE_URL = "https://coinmarketcap.com/currencies/"

    def get_coin_data(self, coin):
        url = f"{self.BASE_URL}{coin.lower()}/"
        response = requests.get(url)
        print("STATUS CODE"+str(response.status_code))
        if response.status_code != 200:
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        # price = soup.find("div", class_="priceValue___11gHJ").text.strip()
        # price_change = soup.find("span", class_="qe1dn9-1 RYkRM").text.strip()
        # market_cap = soup.find("div", class_="sc-16r8icm-0 sc-1teo54s-2 dMAvWt").text.strip()
        # market_cap_rank = soup.find("div", class_="sc-16r8icm-0 sc-1teo54s-4 gGIpIK").text.strip()
        # volume = soup.find("div", class_="sc-16r8icm-0 sc-1teo54s-5 hmfFHA").text.strip()
        # volume_rank = soup.find("div", class_="sc-16r8icm-0 sc-1teo54s-7 jVFBkU").text.strip()
        # volume_change = soup.find("span", class_="qe1dn9-1 RYkRM").text.strip()
        # circulating_supply = soup.find("div", class_="sc-16r8icm-0 sc-1teo54s-9 iworPT").text.strip()
        # total_supply = soup.find("div", class_="sc-16r8icm-0 sc-1teo54s-10 lbSCkg").text.strip()
        # diluted_market_cap = soup.find("div", class_="sc-16r8icm-0 sc-1teo54s-11 boYqDs").text.strip()
        # contract_name = "solana"
        # contract_address = "HLptm5e6rTgh4EKgDpYFrnRHbjpkMyVdEeREEa2G7rf9"
        # official_website = "https://dukocoin.com"
        # twitter_url = "https://twitter.com/dukocoin"
        # telegram_url = "https://t.me/+jlScZmFrQ8g2MDg8"

        # Building the data dictionary
        # 
        data = "hlo"

        return data

    def parse_data(self, soup):
        data = {
            'price': 0.0,  
            'price_change': 0.0,
            'market_cap': 0,
            'market_cap_rank': 0,
            'volume': 0,
            'volume_rank': 0,
            'volume_change': 0.0,
            'circulating_supply': 0,
            'total_supply': 0,
            'diluted_market_cap': 0,
            'contracts': [],
            'official_links': [],
            'socials': []
        }
        return data
