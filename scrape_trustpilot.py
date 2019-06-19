from bs4 import BeautifulSoup
import json
import requests
import pandas as pd

def parse_review(review): 
    name = review['author']['name']
    date = review['datePublished']
    headline = review['headline']
    review_body = review['reviewBody']
    review_rating = int(review['reviewRating']['ratingValue'])
    language = review['inLanguage']
    return {'name': name, 'date':date, 'headline':headline, 
    'review_body':review_body, 'review_rating':review_rating, 'language':language}

def extract_reviews(bs):
    source = bs.find('script', {'type':'application/ld+json'}).getText().replace(';','')
    review_data = json.loads(source)
    reviews_raw = [item for item in review_data[0]['review']]
    reviews = [parse_review(item) for item in reviews_raw]
    return reviews
    

def is_last_page(bs):
    next_link = bs.find('link', attrs = {'rel':'next'})
    if next_link is None:
        return True
    else:
        return False

def scrape_trustpilot(url, company, target_path = './'):
    i = 1
    query_url = 'http://' +url + '?page='+ str(i)
    bs = BeautifulSoup(requests.get(query_url).text, 'html.parser')
    
    all_reviews = []
    
    while not is_last_page(bs):
        # Extract Reviews
        all_reviews = all_reviews + extract_reviews(bs)
        
        # Load the next page
        i += 1
        query_url = 'http://' + url + '?page='+ str(i)
        bs = BeautifulSoup(requests.get(query_url).text, 'html.parser')
    else:
        all_reviews = all_reviews + extract_reviews(bs)
        
    all_reviews = pd.DataFrame.from_dict(all_reviews)
    all_reviews['company'] = company
    all_reviews.to_csv(target_path + company + '.csv', index = False)


# url = 'www.trustpilot.com/review/www.amazon.com'
# target_path = './'
# 
# scrape_trustpilot(url, 'amazon' ,target_path)
