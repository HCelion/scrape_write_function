# Scrape_write_function

Due to changes in the website, I had to rewrite the scraper in Python, as R's json handling was not sufficient

The input the is the starting url of a company, e.g.
```
url <- 'https://www.trustpilot.com/review/www.amazon.com'
```

The second input is the label one wants to give the company within the scraped data frame, as well as the name of the file. The third input is the target folder in which the `.csv` file should be located.
After loading the script you can run for example

```
scrape_trustpilot(url, 'amazon' ,target_path)
```

It will take a couple of minutes, but unless the TrustPilot website has changed again, the data should be stored on your system. The scraper is not robustified against potential hangups. Also, it currently goes from page to page until it recognises the last page by its interface. If that changes, it can be that the scraper runs forever, rescraping the first site over and over again. 
