import json
import requests

URL = "https://jsonplaceholder.typicode.com/posts?_limit=10"

source = requests.get(url=URL)
data = source.json()
# print(data)
for post in data:
    print(post)

# Dumping the data from the api into the file
with open('posts.json', 'w') as f:
    json.dump(data, f, indent=2)
