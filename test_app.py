from flask import Flask
from routes import create_routes
from config import app
from config import create_app

import random
import string

pytest_plugins = ["docker_compose"]

app = create_app()
create_routes(app)
client = app.test_client()

#------- helper -------
def login(client, username, password):
    return client.post('/', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def signup(client, username, password):
    return client.post('/signup', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.post('/logout', data={}, follow_redirects=True)

def generate_random_word():
    rword = ''.join(random.choice(string.ascii_letters) for i in range(10))
    return rword

#------- testing functions -------
def test_signup_1():
    mock_username = generate_random_word()
    mock_password = ''
    response = signup(client, mock_username, mock_password)
    assert response.status_code == 501

def test_signup_2():
    mock_username = 'test'
    mock_password = 'test'
    response = signup(client, mock_username, mock_password)
    response = signup(client, mock_username, mock_password)
    assert response.status_code == 503

def test_signup_3():
    mock_username = generate_random_word()
    mock_password = 'test'
    response = signup(client, mock_username, mock_password)
    assert response.status_code == 200

def test_login_1():
    mock_username = ''
    mock_password = 'test'
    response = login(client, mock_username, mock_password)
    assert response.status_code == 501

def test_login_2():
    mock_username = 'test'
    mock_password = ''
    response = login(client, mock_username, mock_password)
    assert response.status_code == 501

def test_login_3(): 
    mock_username = 'test'
    mock_password = 'test'+'x'
    response = login(client, mock_username, mock_password)
    assert response.status_code == 502

def test_login_4():
    mock_username = 'test'
    mock_password = 'test'
    response = login(client, mock_username, mock_password)
    assert response.status_code == 200
    logout(client)

def test_login_5():
    mock_username = generate_random_word()
    mock_password = 'test'
    response = login(client, mock_username, mock_password)
    assert response.status_code == 504

def test_logout_1():    
    mock_username = 'test'
    mock_password = 'test'
    response = login(client, mock_username, mock_password)
    assert response.status_code == 200

def test_logout_2(): 
    url = '/members'
    response = client.get(url)
    assert response.status_code == 200

    response = logout(client)
    assert response.status_code == 200

def test_endpoint_index():
    url = '/'
    response = client.get(url)
    assert response.status_code == 200

def tes_endpoint_signup():
    url = '/signup'
    response = client.get(url)
    assert response.status_code == 200

def test_endpoint_members_unauthorized():
    logout(client)
    url = '/members'
    response = client.get(url)
    assert response.status_code == 302
