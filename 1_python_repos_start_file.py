import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print()
print(f"Status code: {r.status_code}")
print()


outfile = open('output.json', 'w')

response_dict = r.json()

json.dump(response_dict, outfile, indent=4)


list_of_repos = response_dict['items']

print(f"Number of Repositories: {len(list_of_repos)}")
print()

first_repo = list_of_repos[0]

#for key in first_repo:
#    print(key)

#print out the name of the FIRST repo
print(f"Name: {first_repo['name']}")
print(f"Name: {first_repo['owner']['login']}")
print(f"Stars: {first_repo['stargazers_count']}")
print(f"Repository: {first_repo['html_url']}")
print(f"Created: {first_repo['created_at']}")
print(f"Updated: {first_repo['updated_at']}")
print(f"Description: {first_repo['description']}")
# owner of the repo (login)
# 
# number of stars, repo URL
# 
# when it was created
# 
# when it was last updated, description



from plotly.graph_objs import Bar
from plotly import offline

repos, stars = [], []

for repo in list_of_repos[:10]:
#^  :10 is called splicing, starts at lower range and goes to 9
    repos.append(repo['name'])
    stars.append(repo['stargazers_count'])


data = [{
    "type":"bar",
    "x":repos,
    "y":stars,
    "marker":{
        "color":"rgb(60,100,150)",
        "line":{"width":1.5, "color":"rgb(25,25,25)"},
    },
    "opacity":0.6,
}]

my_layout = {
    "title":"Most-Starred Python Projects on GitHub",
    "xaxis":{"title":"Repository"},
    "yaxis":{"title":"Stars"}
}

fig = {"data":data, "layout":my_layout}

offline.plot(fig, filename="python_repos.html")
