from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup

import time


def scrape(title, location):

    # Make sure you have the ChromeDriver executable in your PATH or provide the path here
    driver = webdriver.Chrome()
    driver.maximize_window()

    wait = WebDriverWait(driver, 30)

    # Navigate to LinkedIn
    job_search_url = "https://www.linkedin.com/jobs/search"
    driver.get(job_search_url)

    # Wait for page to be interactive
    driver.execute_script("return document.readyState")

    # Scroll to the bottom of the page to load all job listings
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Find the Job Title search input and search for the job title
    search_input = wait.until(
        EC.presence_of_element_located((By.ID, "job-search-bar-keywords"))
    )
    # Find the Location search input and search for the location
    location_input = wait.until(
        EC.presence_of_element_located((By.ID, "job-search-bar-location"))
    )

    # Clear the input fields
    search_input.clear()
    location_input.clear()

    # Enter the job title and location
    search_input.send_keys(title)
    location_input.send_keys(location)
    location_input.send_keys(Keys.RETURN)

    # Wait for the search results to load
    wait.until(
        EC.presence_of_element_located(
            (By.CLASS_NAME, "jobs-search__results-list"))
    )

  # Determine the number of scrolls and scroll distance
    total_scrolls = 50
    scroll_distance = 300

    for _ in range(total_scrolls):
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        time.sleep(0.25)

    # Grab the page source
    linkedin_jobs_src = driver.page_source
    soup = BeautifulSoup(linkedin_jobs_src, "lxml")

    # Find the job listing fields
    job_title_html = soup.find_all('h3', class_='base-search-card__title')
    job_company_html = soup.find_all('h4', class_='base-search-card__subtitle')
    job_location_html = soup.find_all(
        'span', class_='job-search-card__location')

    # Create a list to store the job data
    job_data = []

    # iterate through the job listings and extract the job title, company and location using zip()
    for title_tag, company_tag, location_tag in zip(job_title_html, job_company_html, job_location_html):
        job_data.append({
            'title': title_tag.get_text(strip=True),
            'company': company_tag.get_text(strip=True),
            'location': location_tag.get_text(strip=True)
        })

    # for job_listing in job_listings:
    # Extract job details as before

    # Apply filtering logic (e.g., based on job_title or company)

    #     if some_filtering_logic:
    #         apply_button = job_listing.find_element_by_class_name("apply-button")
    #         apply_button.click()
    #         time.sleep(2)  # Give some time for the application process to complete
    print(job_data)

    driver.quit()
