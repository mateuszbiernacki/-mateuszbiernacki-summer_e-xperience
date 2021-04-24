import requests as req
from flask import Flask, render_template
import json

flask_app = Flask('__name__', template_folder='templates/')


@flask_app.route('/')
def home():
    return render_template('index.html')


@flask_app.route('/numbers_of_star/<user>')
def count_stars_html(user):
    r = req.get(f'https://api.github.com/users/{user}/repos?per_page=100')
    list_of_repos = json.loads(r.text)
    repos_to_stars = []
    buff = ""
    sum_of_stars = 0
    for repo in list_of_repos:
        sum_of_stars += repo['stargazers_count']
        if repo['stargazers_count'] > 1:
            buff = buff + repo['name'] + ' - ' + str(repo['stargazers_count']) + ' stars'
        else:
            buff = buff + repo['name'] + ' - ' + str(repo['stargazers_count']) + ' star'
        repos_to_stars.append(buff)
        buff = ""
    return render_template('index.html', content=repos_to_stars,
                           name=user,
                           total_of_stars=str(sum_of_stars) + ' total')


@flask_app.route('/json/numbers_of_star/<user>')
def count_stars_json(user):
    r = req.get(f'https://api.github.com/users/{user}/repos?per_page=100')
    list_of_repos = json.loads(r.text)
    repos_to_stars = {}
    sum_of_stars = 0
    for repo in list_of_repos:
        repos_to_stars[repo['name']] = repo['stargazers_count']
        sum_of_stars += repo['stargazers_count']
    return json.dumps({'username': user,
                       'list_of_repos': repos_to_stars,
                       'sum_of_stars': sum_of_stars})


if __name__ == "__main__":
    flask_app.run()
