
import json

# Test for creating a project
def test_create_project(test_client, init_database):
    response = test_client.post('/api/projects', 
                                 data=json.dumps(dict(participant_id=1, title='Test Project', description='A test project', repository_url='http://github.com/test/project'))
                                 , content_type='application/json')
    assert response.status_code == 200
    assert 'project_id' in response.json

# Test for getting a project
def test_get_project(test_client, init_database):
    # This test assumes a project with id=1 exists
    response = test_client.get('/api/projects/1')
    assert response.status_code == 200
    assert 'project_id' in response.json

# Test for updating a project
def test_update_project(test_client, init_database):
    response = test_client.put('/api/projects/1', 
                                data=json.dumps(dict(title='Updated Project Title')),
                                content_type='application/json')
    assert response.status_code == 200
    assert 'updated_fields' in response.json

# Test for deleting a project
def test_delete_project(test_client, init_database):
    response = test_client.delete('/api/projects/1')
    assert response.status_code == 200
    assert 'success' in response.json

# Test for shipping a project
def test_ship_project(test_client, init_database):
    response = test_client.post('/api/projects/1/ship')
    assert response.status_code == 200
    assert 'shipping_status' in response.json

# Test for getting shipping status of a project
def test_get_ship_status(test_client, init_database):
    response = test_client.get('/api/projects/1/ship')
    assert response.status_code == 200
    assert 'shipping_status' in response.json
