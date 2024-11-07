
## Table of Contents
- [Project Overview](#project_overview)
- [Prerequisites](#Prerequisites)
- [Usage](#Usage)
- [Structure](#Structure)

# Project Overview
This project introduces the basics of building a scraper from scratch by:

1. Querying an API to retrieve a list of countries and their past leaders.
2. Scraping Wikipedia to gather leader biographies.
3. Saving the data in JSON format for further processing.

# Prerequisites
Make sure you have the following:

1. Python 3.x installed.
2. pip for managing Python packages.


# Usage

This script will:
1. Retrieve a list of countries and their leaders from the API.
2. Extract biographical information from Wikipedia for each leader.
3. Save the output in a leaders.json file.
4. Check the Output: The scraped data will be stored in leaders.json. 

# Structure
The project has the following core components:

1. get_leaders(): A function that connects to the API, retrieves country and leader data, and calls helper functions to gather Wikipedia data.
2. get_first_paragraph(): Uses BeautifulSoup to scrape the first paragraph of a Wikipedia entry and clean it with regex.
3. leaders_scraper.py: Main script to run the entire scraping and saving process.
4. leaders.json: Output file storing the structured data for each country and leader.

