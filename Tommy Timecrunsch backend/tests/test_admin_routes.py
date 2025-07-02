
import json

# Test for getting admin events
def test_get_admin_events(test_client, init_database):
    response = test_client.get('/api/admin/events')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Test for creating an admin event
def test_create_admin_event(test_client, init_database):
    response = test_client.post('/api/admin/events', 
                                 data=json.dumps(dict(event_type='test_event', description='A test event', severity='low', scheduled_at='2025-07-01T12:00:00', target_participants=[]))
                                 , content_type='application/json')
    assert response.status_code == 200
    assert 'event_id' in response.json

# Test for deleting an admin event
def test_delete_admin_event(test_client, init_database):
    # This test assumes an event with id=1 exists
    response = test_client.delete('/api/admin/events/1')
    assert response.status_code == 200
    assert 'success' in response.json
