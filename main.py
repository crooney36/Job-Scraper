import argparse
from spiders import indeed, linkedin


def main():

    # Parse arguments from command line input and run the appropriate scraper.
    parser = argparse.ArgumentParser(description='Job search scraper.')
    parser.add_argument('-t', '--title', type=str, required=True,
                        help='Job title to search for.')
    parser.add_argument('-l', '--location', type=str, required=True,
                        help='Location to search in.')
    parser.add_argument('-s', '--site', type=str, required=True,
                        choices=['indeed', 'linkedin'],
                        help='Website to scrape.')

    args = parser.parse_args()

    # Assign arguments to variables.
    title = args.title
    location = args.location
    site = args.site

    # Run the appropriate scraper.
    if site == 'indeed':
        indeed.scrape(title, location)
    elif site == 'linkedin':
        linkedin.scrape(title, location)


if __name__ == "__main__":
    main()
