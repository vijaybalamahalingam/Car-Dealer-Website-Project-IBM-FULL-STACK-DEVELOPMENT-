from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
# def about(request):
# ...


# Create a `contact` view to return a static contact page
#def contact(request):

# sign up view
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up - Car Dealership</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-image: url('https://images.unsplash.com/photo-1485291571150-772bcfc10da5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=928&q=80'); /* Replace with the actual image filename */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .container {
            max-width: 400px;
            margin: 100px auto;
            padding: 20px;
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            text-align: center;
        }
        label,
        input {
            display: block;
            margin-bottom: 10px;
        }
        input[type="submit"] {
            background-color: #333;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Sign Up</h2>
        <form id="signupForm">
            <label for="firstName">First Name:</label>
            <input type="text" id="firstName" required>

            <label for="lastName">Last Name:</label>
            <input type="text" id="lastName" required>

            <label for="username">Username:</label>
            <input type="text" id="username" required>

            <label for="password">Password:</label>
            <input type="password" id="password" required>

            <input type="submit" value="Sign Up">
        </form>
    </div>
</body>
</html>




# Create a `login_request` view to handle sign in request
# def login_request(request):
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Car Dealership</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-image: url('https://images.unsplash.com/photo-1485291571150-772bcfc10da5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=928&q=80'); /* Replace with the actual image filename */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .container {
            max-width: 400px;
            margin: 100px auto;
            padding: 20px;
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            text-align: center;
        }
        label,
        input {
            display: block;
            margin-bottom: 10px;
        }
        input[type="submit"] {
            background-color: #333;
            color: #fff;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Login</h2>
        <form id="loginForm">
            <label for="username">Username:</label>
            <input type="text" id="username" required>

            <label for="password">Password:</label>
            <input type="password" id="password" required>

            <input type="submit" value="Login">
        </form>
    </div>

    <script>
          document.getElementById('loginForm').addEventListener('submit', function(event) {
            event.preventDefault();

            // Get form values
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            // Perform authentication check here (for demonstration purposes, we'll just show a message)
            if (username === 'exampleUser' && password === 'examplePassword') {
                alert('Login successful!'); // Replace with your actual authentication logic
            } else {
                alert('Invalid username or password. Please try again.'); // Replace with your actual authentication logic
            }
        });
    </script>
</body>
</html>

# Create a `logout_request` view to handle sign out request
# def logout_request(request):
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Logout - Car Dealership</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-image: url('https://images.unsplash.com/photo-1485291571150-772bcfc10da5?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=928&q=80'); /* Replace with the actual image filename */
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }
        .container {
            max-width: 400px;
            margin: 100px auto;
            padding: 20px;
            text-align: center;
            background-color: #fff;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            margin-bottom: 20px;
        }
        p {
            margin-bottom: 30px;
        }
        a {
            color: #333;
            text-decoration: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>Logout</h2>
        <p>Are you sure you want to log out?</p>
        <a href="login.html">Logout</a> 
    </div>
</body>
</html>


# Create a `registration_request` view to handle sign up request
# def registration_request(request):
# ...

# Update the `get_dealerships` view to render the index page with a list of dealerships

def get_dealerships(request):
    if request.method == "GET":
        url = "your-cloud-function-domain/dealerships/dealer-get"
        # Get dealers from the URL
        dealerships = get_dealers_from_cf(url)
        # Concat all dealer's short name
        dealer_names = ' '.join([dealer.short_name for dealer in dealerships])
        # Return a list of dealer short name
        return HttpResponse(dealer_names)

# Create a `get_dealer_details` view to render the reviews of a dealer

def get_dealer_reviews_from_cf():
    # Sample implementation, replace this with your actual method to get reviews.
    return [
        {'review_id': 1, 'text': 'Great service!', 'rating': 5},
        {'review_id': 2, 'text': 'Very helpful staff.', 'rating': 4},
        {'review_id': 3, 'text': 'Could be better.', 'rating': 3},
    ]

# Create an empty context dictionary.
context = {}

# Get the reviews from the get_dealer_reviews_from_cf method.
reviews = get_dealer_reviews_from_cf()

# Append the reviews list to the context dictionary.
context['reviews'] = reviews

# Now you can access the reviews from the context dictionary.
print(context['reviews'])

from django.shortcuts import render
import requests

class DealerReview:
    # DealerReview class definition here...

def get_request(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def get_dealer_reviews_from_cf(dealer_id):
    url = f"your_cloud_function_endpoint"  # Replace with your cloud function endpoint
    reviews_data = get_request(f"{url}/reviews?dealerId={dealer_id}")
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

def get_dealer_details(request, dealer_id):
    dealer_reviews = get_dealer_reviews_from_cf(dealer_id)
    # Do any other processing with dealer_reviews data if needed
    return render(request, 'dealer_details.html', {'dealer_reviews': dealer_reviews})



# new def add_review(request, dealer_id): method to handle review post request

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

# Assuming the DealerReview class is defined in another file
from .models import DealerReview

@login_required
def add_review(request, dealer_id):
    if request.method == 'POST':
        user = request.user

        # Check if the user is authenticated
        if not user.is_authenticated:
            return render(request, 'error.html', {'error_message': 'Only authenticated users can post reviews.'})

        # Get the dealer information from the cloud function or database
        # Replace "your_cloud_function_endpoint" with the actual endpoint URL of your cloud function or database
        url = f"your_cloud_function_endpoint/reviews/{dealer_id}"
        response = requests.get(url)

        if response.status_code != 200:
            return render(request, 'error.html', {'error_message': 'Dealer not found.'})

        dealer_info = response.json()

        # Create a dictionary object called review to append review details
        review = {
            'time': '2023-07-31',  # Replace with the actual time of the review
            'name': user.username,
            'dealership': dealer_info['dealership'],
            'review': request.POST.get('review', ''),
            'purchase': True if request.POST.get('purchase', '') == 'True' else False,
            # Add any other attributes you defined in your review-post cloud function or database here
        }

        # Create a new DealerReview object and save it to the database
        new_review = DealerReview(**review)
        new_review.save()

        return render(request, 'review_added.html', {'new_review': new_review})
    else:
        return render(request, 'add_review.html', {'dealer_id': dealer_id})


# dictionary object called json_payload
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DealerReview
from .restapis import post_request

@login_required
def add_review(request, dealer_id):
    if request.method == 'POST':
        user = request.user

        # Check if the user is authenticated
        if not user.is_authenticated:
            return render(request, 'error.html', {'error_message': 'Only authenticated users can post reviews.'})

        # Get the dealer information from the cloud function or database
        # Replace "your_cloud_function_endpoint" with the actual endpoint URL of your cloud function or database
        url = f"your_cloud_function_endpoint/reviews/{dealer_id}"
        response = requests.get(url)

        if response.status_code != 200:
            return render(request, 'error.html', {'error_message': 'Dealer not found.'})

        dealer_info = response.json()

        # Create a dictionary object called review to append review details
        review = {
            'time': '2023-07-31',  # Replace with the actual time of the review
            'name': user.username,
            'dealership': dealer_info['dealership'],
            'review': request.POST.get('review', ''),
            'purchase': True if request.POST.get('purchase', '') == 'True' else False,
            # Add any other attributes you defined in your review-post cloud function or database here
        }

        # Create another dictionary object called json_payload with the key "review"
        json_payload = {"review": review}

        # Call the post_request method with the payload
        post_response = post_request(url, json_payload, dealerId=dealer_id)

        # Return the result of post_request to the add_review view method
        return render(request, 'post_response.html', {'post_response': post_response.json()})
    else:
        return render(request, 'add_review.html', {'dealer_id': dealer_id})




# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...
