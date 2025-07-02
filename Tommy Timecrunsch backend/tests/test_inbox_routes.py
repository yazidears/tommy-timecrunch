
import json

# Test for getting inbox
def test_get_inbox(test_client, init_database):
    response = test_client.get('/api/inbox')
    assert response.status_code == 200
    assert isinstance(response.json, list)
