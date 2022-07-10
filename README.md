# jumia_prices_scraper
A script that scrapes prices of specified products on jumia

## Project overview
[Webscraping](https://en.wikipedia.org/wiki/Web_scraping), web harvesting, or web data extraction is data scraping used for extracting data from websites.
The web scraping software may directly access the World Wide Web using the Hypertext Transfer Protocol or a web browser. 
While web scraping can be done manually by a software user, the term typically refers to automated processes implemented using a bot or web crawler. 
It is a form of copying in which specific data is gathered and copied from the web, typically into a central local database or spreadsheet, for later retrieval or analysis.

I built a simple script that scrapes data from an [eCommerce website](https://www.jumia.com.ng/). The script gets data for products including prices and links to the products.
This could be particularly useful during black fridays and treasure hunts.

The script is dynamic in that, it gets the website for the searched product and scrapes data for a specified number of pages.



## Technology, Packages and Libraries
- [Selenium](https://selenium-python.readthedocs.io/) Selenium Python bindings provide a convenient API to access Selenium WebDrivers like Firefox, Ie, Chrome, Remote etc. 
The current supported Python versions are 3.5 and above. I used selenium to access the html and scrape data
- [Pandas](https://pandas.pydata.org/docs/) for coverting the data to csv files.

## Using this code

To build your own version of this project, [Fork](https://help.github.com/en/articles/fork-a-repo) the project repository and [clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine.

- Run ` pip install -U selenium `
- Run ` pip install pandas ` 
- Run ` main.py `


