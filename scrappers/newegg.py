from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

html_page = urlopen('https://www.newegg.com/Desktop-Graphics-Cards/SubCategory/ID-48/Page-1')
bs = soup(html_page.read(),'html.parser')

item_container = bs.findAll('div',{'class':'item-container'})

f = open('result.csv','w')
csv_headers = 'Brand,Model,Price'
f.write(csv_headers)

for product in item_container:
    item_model = product.find('a',{'class':'item-title'}).text
    item_brand = product.find('a',{'class':'item-brand'}).find('img')['title']
    item_price = product.find('li',{'class':'price-current'}).find('strong').text
    item_price_point = product.find('li',{'class':'price-current'}).find('sup').text
    f.write(item_brand.replace(',','/') +","+item_model.replace(',','/')+","+item_price+item_price_point+"\n")



