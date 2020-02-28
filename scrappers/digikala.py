from bs4 import BeautifulSoup as soup
from urllib.request import urlopen,Request
import unicodecsv as csv
import io

#Getting Digikala page and make html and soup object.
URL = 'https://www.digikala.com/landing-page/?promotion_types[0]=incredible_offer&promotion_types[1]=promotion&promotion_times[0]=active&pageno=1&sortby=4'
HDR = {'User-Agent': 'Mozilla/5.0'}
REQ = Request(URL,headers=HDR)

html_page = urlopen(REQ)
bs = soup(html_page.read(),'html.parser')

def make_csv(item1,item2,item3):
    with open ('result.csv','w',encoding='utf-8') as f:
        csv_headers = 'Brand,Model,Price\n'
        f.write(csv_headers)
        f.write(item1 + "," + item2 + "," + item3 + "\n") 
        f.close()

def price_fixer(main_price,price_decimal):
    return main_price + price_decimal

def colon_remover(string):
    return string.replace(',','|')

def write_to_file(string):
    with open ('result.txt','w',encoding='utf-8') as f:
        f.write(string)

item_en_model = bs.find_all('div',{'class':'c-product-box__title-en'})
write_to_file(str(item_en_model))