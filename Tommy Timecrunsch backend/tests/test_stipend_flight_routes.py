
import json

# Test for requesting a stipend
def test_request_stipend(test_client, init_database):
    response = test_client.post('/api/stipends/request', 
                                 data=json.dumps(dict(participant_id=1, amount=100, justification='Test', receipt_urls=['http://example.com/receipt.pdf']))
                                 , content_type='application/json')
    assert response.status_code == 200
    assert 'stipend_id' in response.json

# Test for getting a stipend
def test_get_stipend(test_client, init_database):
    # This test assumes a stipend with id=1 exists
    response = test_client.get('/api/stipends/1')
    assert response.status_code == 200
    assert 'stipend_id' in response.json

# Test for approving a stipend
def test_approve_stipend(test_client, init_database):
    response = test_client.put('/api/stipends/1/approve', 
                                data=json.dumps(dict(status='approved', admin_notes='Looks good')),
                                content_type='application/json')
    assert response.status_code == 200
    assert 'approved_by' in response.json

# Test for requesting a flight
def test_request_flight(test_client, init_database):
    response = test_client.post('/api/flights/request', 
                                 data=json.dumps(dict(participant_id=1, departure_city='Test City', arrival_city='Test City 2', departure_date='2025-07-01', return_date='2025-07-10', estimated_cost=500))
                                 , content_type='application/json')
    assert response.status_code == 200
    assert 'flight_id' in response.json

# Test for getting a flight
def test_get_flight(test_client, init_database):
    # This test assumes a flight with id=1 exists
    response = test_client.get('/api/flights/1')
    assert response.status_code == 200
    assert 'flight_id' in response.json
