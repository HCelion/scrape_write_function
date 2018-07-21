# Scrape_write_function

Scrapes all of a company's reviews of TrustPilot and stores it as a tsv file in your R working directory.

The input the is the starting url of a company, e.g.
```
url <- 'https://www.trustpilot.com/review/www.amazon.com'
```

The second input is the label one wants to give the company within the scraped data frame, as well as the name of the file.

```
scrape_write(url, 'amazon')
```

It will take a couple of minutes, but unless the TrustPilot website has changed the data should be stored on your system.
