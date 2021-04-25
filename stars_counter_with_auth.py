import requests as req
from flask import Flask, render_template
import json

flask_app = Flask('__name__', template_folder='templates/')
auth_file = open('auth.json')
auth_data = json.loads(auth_file.read().encode('utf-8'))


@flask_app.route('/')
def home():
    return render_template('index.html')


@flask_app.route('/numbers_of_star/<user>')
def count_stars_html(user):
    r = req.get(f'https://api.github.com/users/{user}', auth=(auth_data['username'], auth_data['token']))
    user_info = json.loads(r.text)
    repos_to_stars = []
    buff = ""
    sum_of_stars = 0
    repos_numbers = 0
    for page_number in range(int(user_info['public_repos']/100) + 2):
        r = req.get(f'https://api.github.com/users/{user}/repos?page={page_number}&per_page=100',
                    auth=(auth_data['username'], auth_data['token']))
        list_of_repos = json.loads(r.text)
        for repo in list_of_repos:
            repos_numbers += 1
            sum_of_stars += repo['stargazers_count']
            if repo['stargazers_count'] > 1:
                buff = buff + repo['name'] + ' - ' + str(repo['stargazers_count']) + ' stars'
            else:
                buff = buff + repo['name'] + ' - ' + str(repo['stargazers_count']) + ' star'
            repos_to_stars.append(buff)
            buff = ""
    return render_template('index.html', content=repos_to_stars,
                           name=user,
                           total_of_stars=str(sum_of_stars) + ' total from ' + str(repos_numbers) + ' repos')


@flask_app.route('/json/numbers_of_star/<user>')
def count_stars_json(user):
    r = req.get(f'https://api.github.com/users/{user}', auth=(auth_data['username'], auth_data['token']))
    user_info = json.loads(r.text)
    repos_to_stars = {}
    sum_of_stars = 0
    for page_number in range(int(user_info['public_repos'] / 100) + 2):
        r = req.get(f'https://api.github.com/users/{user}/repos?per_page=100&page={page_number}',
                    auth=(auth_data['username'], auth_data['token']))
        list_of_repos = json.loads(r.text)
        for repo in list_of_repos:
            repos_to_stars[repo['name']] = repo['stargazers_count']
            sum_of_stars += repo['stargazers_count']
    return json.dumps({'username': user,
                       'list_of_repos': repos_to_stars,
                       'sum_of_stars': sum_of_stars})


if __name__ == "__main__":
    flask_app.run()
