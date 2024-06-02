import requests
import sys 
import json 


if len(sys.argv) != 2:
    sys.exit()
    
    
    
res = requests.get(f'https://itunes.apple.com/search?entity=song&limit=100&term={sys.argv[1]}')


# json.dumps makes it prety 
o = res.json()
for result in o["results"]:
    print(result["trackName"])