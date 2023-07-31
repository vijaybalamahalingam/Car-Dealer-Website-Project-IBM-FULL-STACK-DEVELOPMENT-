import requests
import json
# import related models here
from requests.auth import HTTPBasicAuth


# Create a `get_request` to make HTTP GET requests
import requests
import json
from .models import CarDealer
from requests.auth import HTTPBasicAuth

def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))


# Create a `post_request` to make HTTP POST requests
# e.g., response = requests.post(url, params=kwargs, json=payload)


# Create a get_dealers_from_cf method to get dealers from a cloud function
def get_dealers_from_cf(url, **kwargs):
    results = []
    # Call get_request with a URL parameter
    json_result = get_request(url)
    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result["rows"]
        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer["doc"]
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results

...
  params = dict()
  params["text"] = kwargs["text"]
  params["version"] = kwargs["version"]
  params["features"] = kwargs["features"]
  params["return_analyzed_text"] = kwargs["return_analyzed_text"]
  response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))
...


# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
import requests

class DealerReview:
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, sentiment, id):
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.sentiment = sentiment
        self.id = id

    def __str__(self):
        return f"Review by {self.name} for {self.dealership} - Sentiment: {self.sentiment}"

def get_dealer_reviews_from_cf(url, dealerId):
    def get_request(url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    reviews_data = get_request(f"{url}/reviews?dealerId={dealerId}")
    if not reviews_data:
        return []

    reviews = []
    for review_data in reviews_data:
        review = DealerReview(
            review_data['dealership'],
            review_data['name'],
            review_data['purchase'],
            review_data['review'],
            review_data['purchase_date'],
            review_data['car_make'],
            review_data['car_model'],
            review_data['car_year'],
            review_data['sentiment'],
            review_data['id']
        )
        reviews.append(review)

    return reviews

...
review_obj.sentiment = analyze_review_sentiments(review_obj.review)


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Assuming the DealerReview class is defined in another file

# Download the necessary resources for SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

def analyze_review_sentiments(dealerreview):
    # Initialize SentimentIntensityAnalyzer
    sia = SentimentIntensityAnalyzer()

    # Perform sentiment analysis on the review
    review_sentiment = sia.polarity_scores(dealerreview.review)

    # Get the sentiment score
    sentiment_score = review_sentiment['compound']

    # Assign sentiment label based on the compound score
    if sentiment_score >= 0.05:
        sentiment = 'Positive'
    elif sentiment_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    # Set the sentiment attribute of the DealerReview object
    dealerreview.sentiment = sentiment

    # new post_request(url, json_payload, **kwargs):
    
    import requests

def post_request(url, json_payload, **kwargs):
    response = requests.post(url, params=kwargs, json=json_payload)
    return response
    
    url = "https://api.example.com/create_review"
payload = {
    "dealership": "Example Dealer",
    "name": "John Doe",
    "purchase": True,
    "review": "Great experience!",
    "purchase_date": "2023-07-31",
    "car_make": "Toyota",
    "car_model": "Camry",
    "car_year": 2022,
    "sentiment": "Positive",
    "id": 12345
}
response = post_request(url, json_payload=payload, auth=("username", "password"))
print(response.status_code)
print(response.json())

