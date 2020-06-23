#Web Scraper using BeautifulSoup By Arif Haque
from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as Soup

my_url= "https://dubai.dubizzle.com/en/property-for-sale/residential/?filters=(listed_by.value%3A%22LA%22)"
#Scraping the page
Uclient= UReq(my_url)
Html = Uclient.read()
Uclient.close()
#Parses the HTML
Page_soup = Soup(Html,"html.parser")
#Grabs each product
containers= Page_soup.findAll("div",{"class":"ListItem__Root-sc-1i3osc0-1 hMPXKC"} )
container = containers[0]
for container in containers:
 	property_name = container.div.img["alt"][27:]
 
 	title_container = container.findAll("span") #Location
	location = title_container[0].text
