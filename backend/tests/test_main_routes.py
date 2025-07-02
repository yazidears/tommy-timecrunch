
import json

# Test for user registration
def test_register(test_client, init_database):
    response = test_client.post('/api/register', 
                              data=json.dumps(dict(username='testuser', email='test@test.com', password='password')),
                              content_type='application/json')
    assert response.status_code == 201
    assert 'user_id' in response.json

# Test for user login
def test_login(test_client, init_database):
    # First, register a user
    test_client.post('/api/register', 
                     data=json.dumps(dict(username='testuser2', email='test2@test.com', password='password')),
                     content_type='application/json')
    # Then, login
    response = test_client.post('/api/login', 
                              data=json.dumps(dict(email='test2@test.com', password='password')),
                              content_type='application/json')
    assert response.status_code == 200
    assert 'token' in response.json

# Test for /api/me endpoint
def test_get_me(test_client, init_database):
    # Register and login to get a token
    test_client.post('/api/register', 
                     data=json.dumps(dict(username='testuser3', email='test3@test.com', password='password')),
                     content_type='application/json')
    login_response = test_client.post('/api/login', 
                                      data=json.dumps(dict(email='test3@test.com', password='password')),
                                      content_type='application/json')
    token = login_response.json['token']
    
    response = test_client.get('/api/me', headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 200
    assert response.json['username'] == 'testuser3'

# Test for logout
def test_logout(test_client, init_database):
    # Register and login to get a token
    test_client.post('/api/register', 
                     data=json.dumps(dict(username='testuser4', email='test4@test.com', password='password')),
                     content_type='application/json')
    login_response = test_client.post('/api/login', 
                                      data=json.dumps(dict(email='test4@test.com', password='password')),
                                      content_type='application/json')
    token = login_response.json['token']

    response = test_client.get('/api/logout', headers={"Authorization": f'Bearer {token}'})
    assert response.status_code == 200
    assert response.json['message'] == 'Successfully logged out'

# Test for saving data
def test_save_data(test_client, init_database):
    # Register a user and get user_id
    register_response = test_client.post('/api/register', 
                                           data=json.dumps(dict(username='testuser5', email='test5@test.com', password='password')),
                                           content_type='application/json')
    user_id = register_response.json['user_id']

    response = test_client.post(f'/api/savedata/{user_id}', 
                                data=json.dumps(dict(data_key='test_key', data_value='test_value')),
                                content_type='application/json')
    assert response.status_code == 200
    assert response.json['success'] == True

# Test for retrieving data
def test_get_data(test_client, init_database):
    # Register a user and get user_id
    register_response = test_client.post('/api/register', 
                                           data=json.dumps(dict(username='testuser6', email='test6@test.com', password='password')),
                                           content_type='application/json')
    user_id = register_response.json['user_id']

    # Save some data first
    test_client.post(f'/api/savedata/{user_id}', 
                     data=json.dumps(dict(data_key='test_key_2', data_value='test_value_2')),
                     content_type='application/json')

    response = test_client.get(f'/api/data/{user_id}?data_key=test_key_2')
    assert response.status_code == 200
    assert response.json['data_value'] == 'test_value_2'
