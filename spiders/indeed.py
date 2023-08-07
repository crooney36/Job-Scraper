from selenium import webdriver

def scrape(title, location):
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    # Go to Indeed's home page
    driver.get("https://www.indeed.com")

    # Find the input box for job title, enter the title
    title_input = driver.find_element_by_name("q")
    title_input.clear()
    title_input.send_keys(title)

    # Find the input box for job location, enter the location
    location_input = driver.find_element_by_name("l")
    location_input.clear()
    location_input.send_keys(location)

    # Find the search button and click it
    search_button = driver.find_element_by_class_name("icl-Button")
    search_button.click()

    # Scraping Logic Here TODO




    # Close the driver
    driver.close()
