import requests
import json
from config import *

import urllib.request


searchTerm = "Tom"

imageSearch = "https://www.googleapis.com/customsearch/v1?q=" + searchTerm + "&cx=014352846413195953642%3Aa2jzsrhjiqo&fileType=jpg&imgType=news&num=1&searchType=image&key=" + apiKey
contents = urllib.request.urlopen(imageSearch).read()
results = json.loads(contents)
url = results["items"][0]["link"]

print(url)