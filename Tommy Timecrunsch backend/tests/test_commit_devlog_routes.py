
import json

# Test for wakatime webhook
def test_wakatime_webhook(test_client, init_database):
    response = test_client.post('/api/webhooks/wakatime', 
                                 data=json.dumps(dict(participant_id=1, coding_time=100, languages=['python'], projects=['test_project']))
                                 , content_type='application/json')
    assert response.status_code == 200
    assert 'success' in response.json

# Test for getting commits of a participant
def test_get_participant_commits(test_client, init_database):
    # This test assumes a participant with id=1 exists
    response = test_client.get('/api/participants/1/commits')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Test for getting devlogs of a participant
def test_get_participant_devlogs(test_client, init_database):
    # This test assumes a participant with id=1 exists
    response = test_client.get('/api/participants/1/devlogs')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Test for creating a devlog for a participant
def test_create_participant_devlog(test_client, init_database):
    response = test_client.post('/api/participants/1/devlogs', 
                                 data=json.dumps(dict(title='Test Devlog', content='This is a test devlog.')),
                                 content_type='application/json')
    assert response.status_code == 200
    assert 'devlog_id' in response.json
