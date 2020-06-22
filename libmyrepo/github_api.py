import requests


def search_avatar(user):
    """
    Search for a user's avatar on Github
    :param user: str with the username on github
    :return: srt with avatar link
    """
    url = f'https://api.github.com/users/{user}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


def repos(user):
    url = f'https://api.github.com/users/{user}/repos'
    resp = requests.get(url)
    print(resp.json())
    name_and_url = ''
    for i, value in enumerate(resp.json(), 0):
        name = value['name']
        html_url = value['html_url']
        name_and_url += f'name: {name} | url: {html_url}\n'
    return name_and_url


if __name__ == '__main__':
    print(repos('enosteteo'))
