# Allegro-Summer-Experience-2022
Simple Github API created for Allegro Summer Experience 2022.\
Author: Sara Lukasik\
Email: sa.lukasik@student.uw.edu.pl
### Requirements
Dependencies can be installed with pip
```
python3 -m pip install -r requirements.txt
```
### How to run
Run with
```
python3 web_app.py
```
Now you can acces API with localhost.

### How to use
To find data about a user with Github login 'abc123' look at:\
http://127.0.0.1:5000/find_git_user?login=abc123 

To get only data about users repositories look at:\
http://127.0.0.1:5000/find_git_user?login=abc123&only_repos=1

To get only data about users login, name, bio and programming languages look at:\
http://127.0.0.1:5000/find_git_user?login=abc123&only_data=1

Using only_data=1 and &only_repos=1 at the same time will result in error message.
