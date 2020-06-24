from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as Soup
#The Website
my_url = "https://dubai.dubizzle.com/en/property-for-sale/residential/?filters=(listed_by.value%3A%22LA%22)"
# ----------------------------------------------------------------------------------------------------------------------
#Uclient downloads the Url which is stored in the variable my_url
Uclient = UReq(my_url)
#This reads my HTML which has been downloaded
Html = Uclient.read()
#Closes the HTML to prevent the console from crashing
Uclient.close()
#-----------------------------------------------------------------------------------------------------------------------
# Parses the HTML
Page_soup = Soup(Html, "html.parser")
# Grabs each product
containers = Page_soup.findAll("div", {"class": "ListItem__Root-sc-1i3osc0-1 hMPXKC"})
container = containers[0]
#Creating the .csv file, the headers and the name of the file
#filename = "properties.csv"
#f = open(filename, "w")
#headers = "Property name, Location, Price, Bedrooms\n"
#f.write(headers)
#a for loop for scraping properties
for container in containers:
    property_name = container.div.img["alt"][27:]

    title_container = container.findAll("span")  # Location
    location = title_container[0].text

    property_price = (container.findAll("div", {"data-testid": "listing-price"}))
    price = property_price[0].text

    Bedroom = container.findAll("span", {"data-testid": "listing-key-fact"})
    numbedrooms= Bedroom[0].text

    #print(property_name)
    #print(location)
    #print(price)
    #print(numbedrooms)
    print(test)

#I tried to scrape the phone number from the modal box, it kept coming as square brackets, I even tried a different for loop but it didnt seem to work

    #f.write(property_name.replace(',','|') + ',' + location.replace(',','|') + ',' + price.replace(',','|') + ',' + numbedrooms + '\n')
#f.close()