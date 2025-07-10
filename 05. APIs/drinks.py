import requests
import json
from urllib import response

r = requests.get('https://api.chucknorris.io/jokes/categories')

# print(r.text)
# print(type(r.text)) - string
# print(r.json())
# print(type(r.json())) - dictionary
# print(r.json()['value'])

# querying the joke
# res = r.json()
# punchLine = res['value']
# print(f"I got a joke for you {punchLine}")

# querying endpoints
# list available categories
cats = r.json()
for category in cats:
    print(category)

userCategory = input("Enter the jokes category you want: ")
userRequest = requests.get(f'https://api.chucknorris.io/jokes/random?category={userCategory}')
userResponse = userRequest.json()
userJoke = userResponse['value']

print(f"Joke for {userCategory} category is: {userJoke}")