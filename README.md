# kim-backend-1
## Deliverable
A web application that allows users to sign up for a website and then log in securely.
## Requirements
* Features
    * A user signs up with an email address and password
    * A user logins with an existing email address and password
    * A user logs out
* Endpoints
    * `/` allows a user to login
    * `/members` allows a user to log out
    * `/signup` allows a user to sign up
* Constraints
    * `/members` is accessible to authenticated users only
    * If user's login credentials are not valid, the user is informed
    * A successful authentication redirects a user to the page of `\members`
* Miscellaneous
    * The web app stores credentials in an SQL database and queries them from the database
    * The deliverable includes the SQL table creation scripts - included, no need to run explicitly
    * The deliverable includes `Dockerfile` and `docker-compose.yml`
    * The web app starts via `docker-compose up -d`

# Web App
## Folder Structure
- app.py: Maintain a server
- config.py: Create a session and a login manager
- model.py: Define a User schema and create the table
- routes.py: Handle all endpoints
- templates
    - base.html: an html frame
    - index.html: login form
    - signup.html: signup form
    - members.html: a page for authenticated users
    - warning.html: a warning page
- Dockerfile: docker container description
- docker-compose.yml: docker-compose description
- requirements.txt: installed packages
- users.db: An SQL DB (Can start from scratch with it removed)

## Instruction
```bash
$ git clone https://github.com/hahnsangkim/kim-backend-1.git
$ cd kim-backend-1
(kim-backend-1) $ docker-compose build
```

### Run Web App
```bash
(kim-backend-1) $ docker-compose up -d
```

Put the URL in your browser
```
0.0.0.0:5000
```

### Use Cases
1. Try with random usernames and passwords for login
2. Try with either of username and password missing for login
3. Create credentials with a username and password for signup
4. Create credentials with the same username for signup
5. Log in with the right username and password, directing you to the `/members` page
6. Log out and go to the `/members` endpoint

### Stop Web App
You can stop running the app by commanding
```
$ docker-compose stop
```


### Run PyTest on the docker containers
```bash
(kim-backend-1) $ pytest --use-running-containers
========================= test session starts =========================
platform darwin -- Python 3.8.2, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/kim-backend-1
collected 12 items
test_app.py ......                                                [100%]
========================== 12 passed in 0.68s ==========================
```
## References
- [Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
- [Testing Flask Apps](https://flask.palletsprojects.com/en/1.1.x/testing/)
- [pytest on docker compose](https://github.com/pytest-docker-compose/pytest-docker-compose)
- [Troubleshoot-DB Thread](https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa) 
- [Troubleshoot-session handler](https://docs.sqlalchemy.org/en/13/faq/sessions.html#this-session-s-transaction-has-been-rolled-back-due-to-a-previous-exception-during-flush-or-similar)
- [Bootstrap template](https://getbootstrap.com/docs/5.0/getting-started/introduction/)

## Note
Spent 10 - 12 hours on this exercise.