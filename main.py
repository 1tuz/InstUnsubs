import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get the Instagram API access token from the environment variables
access_token = os.getenv("INSTAGRAM_ACCESS_TOKEN")

# Get the list of accounts you're subscribed to
subscriptions_response = requests.get(f'https://api.instagram.com/v1/users/self/follows?access_token={access_token}')
subscriptions = subscriptions_response.json()['data']
subscription_ids = [subscription['id'] for subscription in subscriptions]

# Get the list of accounts that subscribe to you
followers_response = requests.get(f'https://api.instagram.com/v1/users/self/followed-by?access_token={access_token}')
followers = followers_response.json()['data']
follower_ids = [follower['id'] for follower in followers]

# Get the list of accounts you're subscribed to but they're not subscribed back to you
not_subscribed_back_ids = set(subscription_ids) - set(follower_ids)
not_subscribed_back = [subscription for subscription in subscriptions if subscription['id'] in not_subscribed_back_ids]

# Print the list of accounts
print('Accounts you\'re subscribed to but they\'re not subscribed back to you:')
for account in not_subscribed_back:
    print(f'- {account["username"]}')
