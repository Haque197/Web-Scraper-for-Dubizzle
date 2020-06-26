from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as Soup
from selenium import webdriver

# The Website
driver = webdriver.Firefox()
driver.get("https://dubai.dubizzle.com/en/property-for-sale/residential/?filters=(listed_by.value%3A%22LA%22)")
my_url = "https://dubai.dubizzle.com/en/property-for-sale/residential/?filters=(listed_by.value%3A%22LA%22)"
# ----------------------------------------------------------------------------------------------------------------------
# Uclient downloads the Url which is stored in the variable my_url
Uclient = UReq(my_url)
# This reads my HTML which has been downloaded
Html = Uclient.read()
# Closes the HTML to prevent the console from crashing
Uclient.close()
# -----------------------------------------------------------------------------------------------------------------------
# Parses the HTML
Page_soup = Soup(Html, "html.parser")
# Grabs each product
# mobile = driver.find_elements_by_xpath('//span[@class="call-modal__phone_number"]')
modals = driver.find_elements_by_xpath('//*[@data-testid="lpv-call-button"]')
closemodal = driver.find_elements_by_xpath('//*[@class="ContactModal__StyledCloseIcon-sc-1gd5uz6-9 dyqypU"]')
containers = Page_soup.findAll("div", {"class": "ListItem__Root-sc-1i3osc0-1 hMPXKC"})

# Creating the file, the headers and the name of the file
# filename = "properties.csv"
# f = open(filename, "w")
# headers = "Property name, Location, Price, Bedrooms\n"
# f.write(headers)
# a for loop for scraping properties

for c in containers:
    property_name = c.div.img["alt"][27:]

    title_container = c.findAll("span")  # Location
    location = title_container[0].text

    property_price = c.findAll("div", {"data-testid": "listing-price"})
    price = property_price[0].text

    Bedroom = c.findAll("span", {"data-testid": "listing-key-fact"})
    numbedrooms = Bedroom[0].text

for m in modals:
    # find the first button
    m.click()
    # find the phone number
    number = driver.find_elements_by_xpath('//*[@class="call-modal__phone_number"]')
    num = number[0].text
    #for c in closemodal:
       # c.click()








# print(property_name)
# print(location),
# print(price)
# print(numbedrooms)



# f.write(property_name.replace(',','|') + ',' + location.replace(',','|') + ',' + price.replace(',','|') + ',' + numbedrooms + '\n')
# f.close()
