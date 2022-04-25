# Sara Łukasik 25.04.2022 r.

from github import GithubException
from flask import Flask, request, jsonify
from git_menager import git_profile

app = Flask(__name__)
app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True


@app.route('/find_git_user', methods=["GET"])
def find_git_user():
    """
        return:
            JSON with Github user data or error message
    """
    login = request.args.get('login', None)
    if login:
        try:
            user_result = git_profile(login)
        except GithubException:
            return 'User not found'
        only_data = request.args.get('only_data', 0)
        only_repos = request.args.get('only_repos', 0)

        if only_data:
            if only_repos:
                return 'No data to show with only_repos and only_data arguments'
            json_data = jsonify(user_result['user_data'])
        elif only_repos:
            json_data = jsonify(user_result['user_repos'])
        else:
            json_data = jsonify(user_result)

        return json_data
    else:
        return '''[ERROR] To obtain data enter "/find_git_user?login=[login]" where [login] is valid GitHub login '''


if __name__ == '__main__':
    app.run(debug=False)
