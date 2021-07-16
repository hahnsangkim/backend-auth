# kim-backend-1
## Deliverable
A web application that allows users to sign up for a website and then log in securely.
## Requirements
* Features
    ** A user signs up with an email address and password
    ** A user logins with an existing email address and password
    ** A user logs out
* endpoints
    ** `/` allows a user to login
    ** `/members` allows a user to log out
    ** `/signup` allows a user to sign up
* constraints
    ** `/members` is accessible to authenticated users only
    ** If user's login credentials are not valid, the user is informed
    ** A successful authentication redirects a user to the page of `\members`
       
10. The web app stores credentials in an SQL database and queries them from the database
11. The deliverable includes the SQL table creation scripts
12. The deliverable includes `Dockerfile` and `docker-compose.yml`
13. The web app starts via `docker-compose up -d`

# Web App
## Structure
- model in model.py
    - User
- templates
    - html files
## Instruction

### Run Web App
```bash
(flask) $ flask run
```

### Run Tester
```bash
(flask) $ pytest
========================= test session starts =========================
platform darwin -- Python 3.8.2, pytest-6.2.4, py-1.10.0, pluggy-0.13.1
rootdir: /Users/kim-backend-1
collected 6 items
test_app.py ......                                                [100%]
========================== 6 passed in 3.27s ==========================
```
## Reference
[Flask](https://flask.palletsprojects.com/en/2.0.x/quickstart/)
[Testing Flask Apps](https://flask.palletsprojects.com/en/1.1.x/testing/)
[DB Thread](https://stackoverflow.com/questions/48218065/programmingerror-sqlite-objects-created-in-a-thread-can-only-be-used-in-that-sa)


## Note
I spent x hours on this exercise.