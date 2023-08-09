from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


def scrape(title, location):
    # Initialize the Chrome driver
    driver = webdriver.Chrome()

    # Go to Indeed's home page
    driver.get("https://www.indeed.com")

    # Find the input box for job title, enter the title
    title_input = driver.find_element(By.ID, "text-input-what")
    title_input.clear()
    title_input.send_keys(title)

    # Find the input box for job location, enter the location
    location_input = driver.find_element(By.ID, "text-input-where")
    location_input.clear()
    location_input.send_keys(location)

    # Find the search button and click it
    search_button = driver.find_element(By.CLASS_NAME, "yosegi-InlineWhatWhere-primaryButton")
    search_button.click()

    time.sleep(5)  # give the page some time to load

    indeed_jobs_src = driver.page_source
    soup = BeautifulSoup(indeed_jobs_src, 'lxml')

    print("Initializing...")

     # Assuming each job listing is in a <li> tag inside the 'jobsearch-ResultsList css-0' list
    job_listings = soup.findAll('li')

    print("Scraping...")

    for job in job_listings:
        # Replace 'job-title-class', 'company-class', and 'location-class' 
        # with actual class names from the Indeed website
        job_title = job.find('div', {'class': 'jobTitle css-1h4a4n5 eu4oa1w0'})
        company_name = job.find('div', {'class': 'companyName'})
        job_location = job.find('div', {'class': 'companyLocation'})
        
        print("Title:", job_title.text.strip() if job_title else "N/A")
        print("Company:", company_name.text.strip() if company_name else "N/A")
        print("Location:", job_location.text.strip() if job_location else "N/A")
        print("---------")

    # Close the driver
    driver.close()
