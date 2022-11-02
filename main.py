from rental_search_handler import RentalSearchHandler
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep

zillow_search_url = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.66679775790395%2C%22east%22%3A-72.97490322665395%2C%22south%22%3A39.99634482557994%2C%22north%22%3A41.09412251223541%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A569389%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D"
chrome_driver_path = "C:/Development/chromedriver.exe"
form_link = "https://forms.gle/HjK5KnVu3GvFVrJ29"

zillow_search_handler = RentalSearchHandler(zillow_search_url)
addresses = zillow_search_handler.get_addresses()
prices = zillow_search_handler.get_prices()
property_links = zillow_search_handler.get_place_links()
print(len(property_links))
driver = webdriver.Chrome(service=Service(chrome_driver_path))

for i in range(len(addresses)):
    driver.get(form_link)
    sleep(1)
    questions = (driver.find_elements("class name", "whsOnd"))
    questions[0].send_keys(addresses[i])
    questions[1].send_keys(prices[i])
    questions[2].send_keys(property_links[i])
    submit = driver.find_element("class name", "NPEfkd")
    submit.click()
    sleep(1)
