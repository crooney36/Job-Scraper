import argparse
from job_search_scraper.spiders import indeed, linkedin

def main():
    parser = argparse.ArgumentParser(description='Job search scraper.')
    parser.add_argument('-t', '--title', type=str, required=True,
                        help='Job title to search for.')
    parser.add_argument('-l', '--location', type=str, required=True,
                        help='Location to search in.')
    parser.add_argument('-s', '--site', type=str, required=True,
                        choices=['indeed', 'linkedin'],
                        help='Website to scrape.')

    args = parser.parse_args()

    title = args.title
    location = args.location
    site = args.site

    if site == 'indeed':
        indeed.scrape(title, location)
    elif site == 'linkedin':
        linkedin.scrape(title, location)

if __name__ == "__main__":
    main()
