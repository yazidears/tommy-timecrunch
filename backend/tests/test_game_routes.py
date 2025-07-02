
import json

# Test for game state
def test_get_game_state(test_client, init_database):
    response = test_client.get('/api/game/state')
    assert response.status_code == 200
    assert 'tick' in response.json

# Test for game action
def test_game_action(test_client, init_database):
    response = test_client.post('/api/game/action', 
                               data=json.dumps(dict(action_type='test_action', target_id=1, parameters={})),
                               content_type='application/json')
    assert response.status_code == 200
    assert 'success' in response.json

# Test for saving the game
def test_save_game(test_client, init_database):
    response = test_client.post('/api/game/save')
    assert response.status_code == 200
    assert 'success' in response.json

# Test for random events
def test_get_random_event(test_client, init_database):
    response = test_client.get('/api/game/events/random')
    assert response.status_code == 200
    assert 'event_id' in response.json
