from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def get_total_pages():
    pages_total = bs.find('span',{'class':'list-tool-pagination-text'}).find('strong').text
    pages_total = int(pages_total[2:])
    return pages_total

file_name = "result.csv"
csv_headers = "Brand,Model,Price\n"
f = open(file_name,'w')
f.write(csv_headers)

page = 1
URL = "https://www.newegg.com/p/pl?N=100011693&Page=" + str(page)

page_html_urllib = urlopen(URL)
bs = soup(page_html_urllib.read(),'html.parser')

products = bs.findAll("div", {"class": "item-container"})

while page<get_total_pages():    
    for product in products:
        # This will get item brand 
        item_brand = product.find('a',{'class':'item-brand'}).find('img')['title']
        item_model = product.find('a',{'class':'item-title'}).text
        item_price = product.find('li',{'class':'price-current'}).find('strong').text
        item_price_sup = product.find('li',{'class':'price-current'}).find('sup').text
        f.write(item_brand + "," +item_model.replace(",","|") + "," + item_price + item_price_sup+"$" + "\n")
    page = page + 1
    print('Scraping Page {}'.format(page)+"\tDone...")

f.close()