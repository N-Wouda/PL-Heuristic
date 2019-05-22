import sys

import simplejson as json

from .adaptive_large_neighbourhood_search import \
    adaptive_large_neighbourhood_search


with open(f"experiments/{sys.argv[1]}/{sys.argv[2]}.json") as file:
    data = json.load(file)

result = adaptive_large_neighbourhood_search(data, 10000)

print(result.evaluate())