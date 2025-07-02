
import json

# Test for getting leaderboard
def test_get_leaderboard(test_client, init_database):
    response = test_client.get('/api/leaderboard')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Test for getting PDF report
def test_get_pdf_report(test_client, init_database):
    # This test assumes a hackathon with id=1 exists
    response = test_client.get('/api/reports/pdf?hackathon=1')
    assert response.status_code == 200
    assert 'file_url' in response.json
