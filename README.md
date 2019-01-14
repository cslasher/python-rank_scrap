# Rank Scraper

Python scraper to retrieve the top selling products from a certain site

## Description

This scraper parse the current best selling product list from the front page "Best selling billboard" block. Display results in the console, then provides user with the option to save the results as a csv file or an excel file.

## Getting Started

### Prerequisites

- Python 3.6+
- [Webdriver for Chrome](http://chromedriver.chromium.org/) 2.45+ - Installed and path configured

### Modules Used

- [Selenium](https://www.seleniumhq.org/) - Browser automation
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) - Page parsing
- [PANDAS](https://pandas.pydata.org/) - Data processing
- [Tabulate](https://pypi.org/project/tabulate/) - Format data in console
- [wcwidth](https://pypi.org/project/wcwidth/) - Helper for CJK chars

### Installing

Installing modules

```
pip install -r requirements.txt
```

### Usage

```
python app.py
```

## Authors

- **Edwin Liu** - _Initial work_ - [cslasher](https://github.com/cslasher)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
