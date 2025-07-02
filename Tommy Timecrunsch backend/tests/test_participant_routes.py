
import json

# Test for getting participants of a hackathon
def test_get_hackathon_participants(test_client, init_database):
    # This test assumes a hackathon with id=1 exists
    response = test_client.get('/api/hackathons/1/participants')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Test for creating a participant in a hackathon
def test_create_hackathon_participant(test_client, init_database):
    response = test_client.post('/api/hackathons/1/participants', 
                                 data=json.dumps(dict(name='test_participant', email='participant@test.com', github_username='test_git')),
                                 content_type='application/json')
    assert response.status_code == 201
    assert 'participant_id' in response.json

# Test for getting a specific participant
def test_get_participant(test_client, init_database):
    # This test assumes a participant with id=1 exists
    response = test_client.get('/api/participants/1')
    assert response.status_code == 200
    assert 'participant_id' in response.json

# Test for updating a participant
def test_update_participant(test_client, init_database):
    response = test_client.put('/api/participants/1', 
                                data=json.dumps(dict(name='updated_name')),
                                content_type='application/json')
    assert response.status_code == 200
    assert 'updated_fields' in response.json

# Test for deleting a participant
def test_delete_participant(test_client, init_database):
    response = test_client.delete('/api/participants/1')
    assert response.status_code == 200
    assert 'success' in response.json
