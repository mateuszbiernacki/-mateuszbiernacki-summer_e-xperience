import requests as req
from flask import Flask
import json

flask_app = Flask('__name__')


@flask_app.route('/numbers_of_star/<user>')
def count_stars(user):
    r = req.get(f'https://api.github.com/users/{user}/repos')
    list_of_repos = json.loads(r.text)
    repos_to_stars = {}
    sum_of_stars = 0
    for repo in list_of_repos:
        repos_to_stars[repo['name']] = repo['stargazers_count']
        sum_of_stars += repo['stargazers_count']
    flask_app.run()
    return json.dumps({'username': user,
                       'list_of_repos': repos_to_stars,
                       'sum_of_stars': sum_of_stars})