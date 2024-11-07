##Table of Contents
Project Overview
Prerequisites
Usage
Structure


#Project Overview
This project introduces the basics of building a scraper from scratch by:

Querying an API to retrieve a list of countries and their past leaders.
Scraping Wikipedia to gather leader biographies.
Saving the data in JSON format for further processing.

#Prerequisites
Make sure you have the following:

Python 3.x installed.
pip for managing Python packages.

#Usage

This script will:
Retrieve a list of countries and their leaders from the API.
Extract biographical information from Wikipedia for each leader.
Save the output in a leaders.json file.
Check the Output: The scraped data will be stored in leaders.json. 

#Structure
The project has the following core components:

get_leaders(): A function that connects to the API, retrieves country and leader data, and calls helper functions to gather Wikipedia data.
get_first_paragraph(): Uses BeautifulSoup to scrape the first paragraph of a Wikipedia entry and clean it with regex.
leaders_scraper.py: Main script to run the entire scraping and saving process.
leaders.json: Output file storing the structured data for each country and leader.
To-Do and Extensions
