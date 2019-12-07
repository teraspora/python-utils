# list_repos.py

# Script to list the Github repos of a given user, with their urls
# Author: John Lynch (@teraspora)
# July 27th 2019

import json

username = input('\u001B[31mEnter username:\n    \u001B[0m')

url = f'https://api.github.com/users/{username}/repos'
repos = json.loads(urlopen(url).read())

for repo in repos:
    print(f'{repo["name"]} - {repo["html_url"]}')
