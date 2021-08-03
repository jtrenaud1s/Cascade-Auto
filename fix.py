import json
with open("input.json", "r") as f:
    dictt = json.load(f)

import requests

username = ''
password = ''

# I know, very bad way to handle authentication, Cascade problem putting credentials in a get request's query string...
# I could have opted for an API key had i had permission to generate one for myself in the CMS

requests.post(f"https://cms.semo.edu:8443/api/v1/edit/page/cedc474996c98f635de775fdf9148d64/?u={username}&p={password}", json=dictt)
