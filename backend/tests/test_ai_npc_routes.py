
import json

# Test for AI chat
def test_ai_chat(test_client, init_database):
    response = test_client.post('/api/ai/chat', 
                                 data=json.dumps(dict(messages=[{'role': 'user', 'content': 'Hello'}], model='test_model', temperature=0.7))
                                 , content_type='application/json')
    assert response.status_code == 200
    assert 'response' in response.json

# Test for getting AI models
def test_get_ai_models(test_client, init_database):
    response = test_client.get('/api/ai/model')
    assert response.status_code == 200
    assert 'available_models' in response.json

# Test for getting NPCs
def test_get_npcs(test_client, init_database):
    response = test_client.get('/api/npcs')
    assert response.status_code == 200
    assert isinstance(response.json, list)

# Test for chatting with an NPC
def test_npc_chat(test_client, init_database):
    # This test assumes an NPC with id=1 exists
    response = test_client.post('/api/npc/1/chat', 
                                 data=json.dumps(dict(message='Hello NPC', context={})),
                                 content_type='application/json')
    assert response.status_code == 200
    assert 'response' in response.json
