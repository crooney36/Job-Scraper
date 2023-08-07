from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

import time


def scrape(title, location):

    # Make sure you have the ChromeDriver executable in your PATH or provide the path here
    driver = webdriver.Chrome()

    job_search_url = "https://www.linkedin.com/jobs/search/?keywords={title}&location={location}"
    driver.get(job_search_url)

    search_input = driver.find_element(By.ID, "job-search-bar-keywords")
    search_input.clear()
    search_input.send_keys(title)
    search_input.send_keys(Keys.RETURN)

    linkedin_jobs_src = driver.page_source
    soup = BeautifulSoup(linkedin_jobs_src, 'html')

    job_listings = driver.find_elements(
        By.CLASS_NAME, "jobs-search__results-list")

    for job_listing in job_listings:
        job_title = job_listing.find_element(
            By.CLASS_NAME, "base-search-card__title").text
        company = job_listing.find_element(
            By.CLASS_NAME, "base-search-card__subtitle").text

        # Click into the job listing to access the full job description view
        # job_listing.find_element(
        #     By.XPATH, "//*[@id='main-content']/section/ul/li").click()

        # Wait for the page to load
        time.sleep(2)

        # Find the show more button and click it
        # job_listing.find_element(
        #     By.CSS_SELECTOR, "button.show-more-less-html__button.show-more-less-button.show-more-less-html__button--more.\!ml-0\.5").click()

        # Wait for the page to load
        time.sleep(2)

        # Find the location element and extract the text
        location = job_listing.find_element(
            By.CLASS_NAME, "topcard__flavor topcard__flavor--bullet").text

        # Find the job description element and extract the text
        job_description = job_listing.find_element(
            By.CLASS_NAME, "description__text").text

        print("Job Title:", job_title)
        print("Company:", company)
        print("Location:", location)
        print("Description:", job_description)
        print("="*50)

        # Go back to the search results page to continue scraping
        driver.back()

        # Wait for the page to load
        time.sleep(2)

    # for job_listing in job_listings:
    # # Extract job details as before

    # # Apply filtering logic (e.g., based on job_title or company)

    #     if some_filtering_logic:
    #         apply_button = job_listing.find_element_by_class_name("apply-button")
    #         apply_button.click()
    #         time.sleep(2)  # Give some time for the application process to complete

    driver.quit()
