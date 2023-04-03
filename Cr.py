import requests
import json

# set the access token for the GitHub API
access_token = 'YOUR_ACCESS_TOKEN'

# set the API endpoint for the pull requests
api_endpoint = 'https://api.github.com/repos/{owner}/{repo}/pulls'

# set the parameters for the API request
params = {
    'state': 'open',
    'sort': 'created',
    'direction': 'desc'
}

# add the access token to the request headers
headers = {
    'Authorization': f'token {access_token}'
}

# send the API request to fetch the pull requests
response = requests.get(api_endpoint.format(owner='OWNER_USERNAME', repo='REPO_NAME'), params=params, headers=headers)

# parse the response JSON data
data = json.loads(response.text)

# print the pull requests
for pr in data:
    print(pr['title'], pr['html_url'], pr['user']['login'])
