from bs4 import BeautifulSoup
import requests
from csv import writer
import time

def product():
    url = "https://www.jumia.co.ke/mlp-tech-week/?source=STB_TW_GEN"
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    conts = soup.find_all("article", class_ = "prd _fb col c-prd")
    
    with open("jumia_scraps.csv", 'w') as f:
        writes = writer(f)
        headers = ['product_name', 'brand name', 'price', 'discount', 'number of reviews', 'ratings']
        writes.writerow(headers)
        for cont in conts:
            product_name = cont.find("h3", class_ ='name').text
            brand_name = cont.find("h3", class_ ='name').text.split()[0]
            price = cont.find("div", class_ = 'prc').text
            discount = cont.find("div", class_='bdg _dsct _sm')
            if discount is not None:
                disc = discount.text.strip()
            else:
                disc = "unknown"
            number_of_reviews = cont.find("div", class_= "rev").contents[-1].strip()
            ratings = cont.find("div", class_ = "stars _s").text
            info = [product_name, brand_name, price, disc, number_of_reviews, ratings]
            writes.writerow(info)

if __name__ == '__main__':
    while True:
        product()
        time.sleep(600)