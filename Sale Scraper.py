from urllib.request import urlopen as UReq
from bs4 import BeautifulSoup as Soup
from selenium import webdriver

#The Website
driver = webdriver.Firefox()
#Opens the website on firefox using the driver
driver.get("https://dubai.dubizzle.com/en/property-for-sale/residential/?filters=(listed_by.value%3A%22LA%22)")
#Downloads the website using BS4
my_url = ("https://dubai.dubizzle.com/en/property-for-sale/residential/?filters=(listed_by.value%3A%22LA%22)")
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
modals = driver.find_elements_by_xpath('//*[@data-testid="lpv-call-button"]')
containers = Page_soup.findAll("div", {"class": "ListItem__Root-sc-1i3osc0-1 hMPXKC"})

# Creating the file, the headers and the name of the file
filename = "sale.csv"
f = open(filename, "w")
headers = "Property name" + ';' + "Location" + ';' + "Price" + ';' + "Bedrooms" + ';' + "PhoneNumber" + "\n"
f.write(headers)
# a for loop for scraping properties
m = 0
for c in containers:
    
    #Finds the location of the listing
    title_container = c.findAll("span")
    location = title_container[0].text


    #Finds the price of the property
    property_price = c.findAll("div", {"data-testid": "listing-price"})
    price = property_price[0].text

    #Finds the number of bedrooms available within a property
    Bedroom = c.findAll("span", {"data-testid": "listing-key-fact"})
    numbedrooms = Bedroom[0].text

    # find the first button
    modals[m].click()
    driver.implicitly_wait(3)
    # Find the phone
    number = driver.find_elements_by_xpath('//*[@class="call-modal__phone_number"]')
    phonenum = number[0].text
    # Close the modal box
    close = driver.find_elements_by_xpath('//*[@class="ContactModal__StyledCloseIcon-sc-1gd5uz6-9 dyqypU"]')
    close[0].click()

    #Writes the scraped listings into an .csv file
    f.write(property_name + ';' + location + ';' + price + ';' + numbedrooms + ';' + phonenum + '\n')
    m = m+1

#closes the website
driver.close()
