# bccorp_scraper
A web scraper to obtain the information from BcCorporation website. 
This scraper is based in the next [UpWork project requirement](https://www.upwork.com/nx/jobs/search/details/~014d974183450d05c2?q=web%20scraping&sort=recency&page=3&pageTitle=Job%20Detail&_navType=slider&_modalInfo=%5B%7B%22navType%22%3A%22slider%22,%22title%22%3A%22Job%20Detail%22,%22modalId%22%3A%221656294582458%22%7D%5D).

## Technologies used:
* Python
* Requests module
* Logging module
* Zyte proxy manager
* pandas

## How to run:
1. git clone https://github.com/TUDz/bccorp_scraper.git
2. python3 -m venv venv (Generate a virtual environment)
3. source ven/bin/activate (Activate virtual environment)
4. python3 -m pip install -r requirements.txt (Install dependencies)

* **You should Configure ZYTE_KEY and Zyte Smart proxy Certificate in utils.py**. More info in [Zyte Smart proxy manager](https://www.zyte.com/smart-proxy-manager/)

![Alt text](./img/result.png "Result preview")
