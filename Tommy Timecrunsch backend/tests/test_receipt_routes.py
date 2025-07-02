
import json

# Test for creating a receipt
def test_create_receipt(test_client, init_database):
    # This test needs a file to upload, which is not straightforward in this testing setup.
    # We will mock the file upload for now.
    response = test_client.post('/api/receipts', 
                                 data=dict(participant_id=1, category='test', amount=50, description='Test receipt'),
                                 content_type='multipart/form-data')
    assert response.status_code == 200
    assert 'receipt_id' in response.json

# Test for getting a receipt
def test_get_receipt(test_client, init_database):
    # This test assumes a receipt with id=1 exists
    response = test_client.get('/api/receipts/1')
    assert response.status_code == 200
    assert 'receipt_id' in response.json

# Test for getting receipts of a participant
def test_get_participant_receipts(test_client, init_database):
    # This test assumes a participant with id=1 exists
    response = test_client.get('/api/participants/1/receipts')
    assert response.status_code == 200
    assert isinstance(response.json, list)
