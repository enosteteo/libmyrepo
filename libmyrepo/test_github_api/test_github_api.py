import pytest
from unittest.mock import Mock

from libmyrepo import github_api


@pytest.fixture()
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/41688460?v=4'
    resp_mock.json.return_value = {'avatar_url': url}
    get_mock = mocker.patch('libmyrepo.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


@pytest.fixture()
def repo_url(mocker):
    resp_mock = Mock()
    url = 'https://github.com/enosteteo/AbstractFactory'
    resp_mock.json.return_value = [{'id': 224452993, 'node_id': 'MDEwOlJlcG9zaXRvcnkyMjQ0NTI5OTM=',
                                    'name': 'AbstractFactory', 'full_name': 'enosteteo/AbstractFactory',
                                    'html_url': 'https://github.com/enosteteo/AbstractFactory'}]
    get_mock = mocker.patch('libmyrepo.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_search_avatar(avatar_url):
    url = github_api.search_avatar('enosteteo')
    assert 'https://avatars3.githubusercontent.com/u/41688460?v=4' == url


def test_search_avatar_integracao():
    url = github_api.search_avatar('enosteteo')
    assert 'https://avatars3.githubusercontent.com/u/41688460?v=4' == url


def test_get_repos(repo_url):
    url = github_api.repos('enosteteo')
    assert 'name: AbstractFactory | url: https://github.com/enosteteo/AbstractFactory\n' == url


def test_get_repos_integracao():
    url = github_api.repos('enosteteo')
    assert 'name: AbstractFactory | url: https://github.com/enosteteo/AbstractFactory\n'  in url
