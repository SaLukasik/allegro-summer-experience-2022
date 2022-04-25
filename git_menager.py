# Sara Łukasik 25.04.2022 r.

from github import Github


def git_profile(username: str) -> dict:
    """

    Args:
        username: Login of GitHub user
    Returns:
        Dictionary containing:
            dictionary with login, name, bio and languages (dictionary of used languages).
            dictionary of user's repositories with user_languages (dictionary of languages used in repo)
    """

    g = Github()
    user = g.get_user(username)
    user_data = {'login': user.login, 'name': user.name, 'bio': user.bio}

    user_repos = {}
    user_languages = {}
    for repo in user.get_repos():
        repo_languages = repo.get_languages()
        user_repos[repo.name] = repo_languages

        for i in repo_languages:
            if i in user_languages:
                user_languages[i] = user_languages[i] + repo_languages[i]
            else:
                user_languages[i] = repo_languages[i]

    user_data['languages'] = user_languages
    user_result = {'user_data': user_data, 'user_repos': user_repos}

    return user_result
