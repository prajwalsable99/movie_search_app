import json
import requests
from pprint import PrettyPrinter
my_key="b21437b2"
text1="inception "
url = 'http://www.omdbapi.com/?apikey=b21437b2&t='+text1
response=requests.get(url).json()

pp=PrettyPrinter()
# pp.pprint(response)
img_url=response['Poster']
title=response['Title']
story=response['Plot']
rating=response['imdbRating']
director=response['Director']

res= {'i_url':img_url,'title':title,'story':story,'rating':rating,'director':director}
print(res)

from firebase import firebase



