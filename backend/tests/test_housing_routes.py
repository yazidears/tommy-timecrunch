
import json

# Test for getting housing listings
def test_get_housing_listings(test_client, init_database):
    response = test_client.get('/api/housing/listings')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Test for applying for housing
def test_apply_for_housing(test_client, init_database):
    # This test assumes a participant with id=1 and housing with id=1 exist
    response = test_client.post('/api/housing/apply', 
                                 data=json.dumps(dict(participant_id=1, housing_id=1, check_in_date='2025-07-01', check_out_date='2025-07-10')),
                                 content_type='application/json')
    assert response.status_code == 200
    assert 'application_id' in response.json

# Test for getting a housing application
def test_get_housing_application(test_client, init_database):
    # This test assumes an application with id=1 exists
    response = test_client.get('/api/housing/applications/1')
    assert response.status_code == 200
    assert 'application_id' in response.json

# Test for updating a housing application
def test_update_housing_application(test_client, init_database):
    response = test_client.put('/api/housing/applications/1', 
                                data=json.dumps(dict(status='approved')),
                                content_type='application/json')
    assert response.status_code == 200
    assert 'updated_at' in response.json
