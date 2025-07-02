import requests
import json

BASE_URL = "http://127.0.0.1:5000/api"

def print_response(response):
    """Prints the status code and JSON response."""
    print(f"Status Code: {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=2))
    except json.JSONDecodeError:
        print(response.text)
    print("-" * 20)

def test_register():
    """Tests the /register endpoint."""
    print("Testing POST /register")
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass"
    }
    response = requests.post(f"{BASE_URL}/register", json=data)
    print_response(response)
    if response.status_code == 201:
        return response.json()["user_id"]
    return None

def test_login(email="test@example.com", password="testpass"):
    """Tests the /login endpoint."""
    print("Testing POST /login")
    data = {"email": email, "password": password}
    response = requests.post(f"{BASE_URL}/login", json=data)
    print_response(response)
    if response.status_code == 200:
        return response.json()["token"]
    return None

def test_get_me(token):
    """Tests the /me endpoint."""
    print("Testing GET /me")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/me", headers=headers)
    print_response(response)

def test_logout(token):
    """Tests the /logout endpoint."""
    print("Testing POST /logout")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/logout", headers=headers)
    print_response(response)


def test_game_state(token):
    """Tests the /game/state endpoint."""
    print("Testing GET /game/state")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/game/state", headers=headers)
    print_response(response)

def test_game_action(token):
    """Tests the /game/action endpoint."""
    print("Testing POST /game/action")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "action_type": "some_action",
        "target_id": 1,
        "parameters": {"param1": "value1"}
    }
    response = requests.post(f"{BASE_URL}/game/action", json=data, headers=headers)
    print_response(response)

def test_save_game(token):
    """Tests the /game/save endpoint."""
    print("Testing POST /game/save")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/game/save", headers=headers)
    print_response(response)

def test_get_random_event(token):
    """Tests the /game/events/random endpoint."""
    print("Testing GET /game/events/random")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/game/events/random", headers=headers)
    print_response(response)


def test_get_participants(token):
    """Tests the /hackathons/1/participants endpoint."""
    print("Testing GET /hackathons/1/participants")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/hackathons/1/participants", headers=headers)
    print_response(response)

def test_create_participant(token):
    """Tests the /hackathons/1/participants endpoint."""
    print("Testing POST /hackathons/1/participants")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": "New Participant",
        "email": "participant@example.com",
        "github_username": "newbie",
        "skills": ["python", "flask"]
    }
    response = requests.post(f"{BASE_URL}/hackathons/1/participants", json=data, headers=headers)
    print_response(response)
    if response.status_code == 201:
        return response.json()["participant"]["id"]
    return None

def test_get_participant(token, participant_id):
    """Tests the /participants/:id endpoint."""
    print(f"Testing GET /participants/{participant_id}")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/participants/{participant_id}", headers=headers)
    print_response(response)

def test_update_participant(token, participant_id):
    """Tests the /participants/:id endpoint."""
    print(f"Testing PUT /participants/{participant_id}")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "name": "Updated Participant",
        "email": "updated@example.com",
        "status": "active",
        "housing_id": 1
    }
    response = requests.put(f"{BASE_URL}/participants/{participant_id}", json=data, headers=headers)
    print_response(response)

def test_delete_participant(token, participant_id):
    """Tests the /participants/:id endpoint."""
    print(f"Testing DELETE /participants/{participant_id}")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/participants/{participant_id}", headers=headers)
    print_response(response)


def test_get_housing_listings(token):
    """Tests the /housing/listings endpoint."""
    print("Testing GET /housing/listings")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/housing/listings", headers=headers)
    print_response(response)

def test_apply_for_housing(token, participant_id):
    """Tests the /housing/apply endpoint."""
    print("Testing POST /housing/apply")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "participant_id": participant_id,
        "housing_id": 1,
        "check_in_date": "2024-08-01",
        "check_out_date": "2024-08-10"
    }
    response = requests.post(f"{BASE_URL}/housing/apply", json=data, headers=headers)
    print_response(response)
    if response.status_code == 201:
        return response.json()["application_id"]
    return None

def test_get_housing_application(token, application_id):
    """Tests the /housing/applications/:id endpoint."""
    print(f"Testing GET /housing/applications/{application_id}")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/housing/applications/{application_id}", headers=headers)
    print_response(response)

def test_update_housing_application(token, application_id):
    """Tests the /housing/applications/:id endpoint."""
    print(f"Testing PUT /housing/applications/{application_id}")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "status": "approved",
        "check_in_date": "2024-08-01",
        "check_out_date": "2024-08-11"
    }
    response = requests.put(f"{BASE_URL}/housing/applications/{application_id}", json=data, headers=headers)
    print_response(response)

def test_wakatime_webhook(token):
    """Tests the /webhooks/wakatime endpoint."""
    print("Testing POST /webhooks/wakatime")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "participant_id": 1,
        "coding_time": 3600,
        "languages": ["python", "javascript"],
        "projects": ["tommy-timecrunch"]
    }
    response = requests.post(f"{BASE_URL}/webhooks/wakatime", json=data, headers=headers)
    print_response(response)

def test_get_commits(token, participant_id):
    """Tests the /participants/:id/commits endpoint."""
    print(f"Testing GET /participants/{participant_id}/commits")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/participants/{participant_id}/commits", headers=headers)
    print_response(response)

def test_get_devlogs(token, participant_id):
    """Tests the /participants/:id/devlogs endpoint."""
    print(f"Testing GET /participants/{participant_id}/devlogs")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/participants/{participant_id}/devlogs", headers=headers)
    print_response(response)

def test_create_devlog(token, participant_id):
    """Tests the /participants/:id/devlogs endpoint."""
    print(f"Testing POST /participants/{participant_id}/devlogs")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "title": "My First Devlog",
        "content": "This is the content of my first devlog."
    }
    response = requests.post(f"{BASE_URL}/participants/{participant_id}/devlogs", json=data, headers=headers)
    print_response(response)

def test_request_stipend(token, participant_id):
    """Tests the /stipends/request endpoint."""
    print("Testing POST /stipends/request")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "participant_id": participant_id,
        "amount": 500,
        "justification": "For travel expenses",
        "receipt_urls": ["http://example.com/receipt1.pdf"]
    }
    response = requests.post(f"{BASE_URL}/stipends/request", json=data, headers=headers)
    print_response(response)
    if response.status_code == 201:
        return response.json()["stipend_id"]
    return None

def test_get_stipend(token, stipend_id):
    """Tests the /stipends/:id endpoint."""
    print(f"Testing GET /stipends/{stipend_id}")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/stipends/{stipend_id}", headers=headers)
    print_response(response)

def test_approve_stipend(token, stipend_id):
    """Tests the /stipends/:id/approve endpoint."""
    print(f"Testing PUT /stipends/{stipend_id}/approve")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "status": "approved",
        "admin_notes": "Approved by admin."
    }
    response = requests.put(f"{BASE_URL}/stipends/{stipend_id}/approve", json=data, headers=headers)
    print_response(response)

def test_request_flight(token, participant_id):
    """Tests the /flights/request endpoint."""
    print("Testing POST /flights/request")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "participant_id": participant_id,
        "departure_city": "New York",
        "arrival_city": "San Francisco",
        "departure_date": "2024-08-15",
        "return_date": "2024-08-25",
        "estimated_cost": 800
    }
    response = requests.post(f"{BASE_URL}/flights/request", json=data, headers=headers)
    print_response(response)
    if response.status_code == 201:
        return response.json()["flight_id"]
    return None

def test_get_flight(token, flight_id):
    """Tests the /flights/:id endpoint."""
    print(f"Testing GET /flights/{flight_id}")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/flights/{flight_id}", headers=headers)
    print_response(response)

def test_create_receipt(token, participant_id):
    """Tests the /receipts endpoint."""
    print("Testing POST /receipts")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "participant_id": participant_id,
        "category": "food",
        "amount": 25.50,
        "description": "Lunch"
    }
    # This endpoint expects a file upload, which is more complex with requests.
    # We will just test the endpoint with JSON data for now.
    # In a real scenario, you would use multipart/form-data.
    files = {'file': ('receipt.txt', 'dummy content', 'text/plain')}
    response = requests.post(f"{BASE_URL}/receipts", data=data, headers=headers, files=files)
    print_response(response)
    if response.status_code == 201:
        return response.json()["receipt_id"]
    return None

def test_get_receipt(token, receipt_id):
    """Tests the /receipts/:id endpoint."""
    print(f"Testing GET /receipts/{receipt_id}")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/receipts/{receipt_id}", headers=headers)
    print_response(response)

def test_get_participant_receipts(token, participant_id):
    """Tests the /participants/:id/receipts endpoint."""
    print(f"Testing GET /participants/{participant_id}/receipts")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/participants/{participant_id}/receipts", headers=headers)
    print_response(response)

def test_create_project(token, participant_id):
    """Tests the /projects endpoint."""
    print("Testing POST /projects")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "participant_id": participant_id,
        "title": "My Awesome Project",
        "description": "A project to change the world.",
        "repository_url": "http://github.com/testuser/my-awesome-project"
    }
    response = requests.post(f"{BASE_URL}/projects", json=data, headers=headers)
    print_response(response)
    if response.status_code == 201:
        return response.json()["project_id"]
    return None

def test_get_project(token, project_id):
    """Tests the /projects/:id endpoint."""
    print(f"Testing GET /projects/{project_id}")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=headers)
    print_response(response)

def test_update_project(token, project_id):
    """Tests the /projects/:id endpoint."""
    print(f"Testing PUT /projects/{project_id}")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "title": "My Even More Awesome Project",
        "description": "An updated project description.",
        "repository_url": "http://github.com/testuser/my-even-more-awesome-project",
        "status": "in_progress"
    }
    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=data, headers=headers)
    print_response(response)

def test_delete_project(token, project_id):
    """Tests the /projects/:id endpoint."""
    print(f"Testing DELETE /projects/{project_id}")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/projects/{project_id}", headers=headers)
    print_response(response)

def test_ship_project(token, project_id):
    """Tests the /projects/:id/ship endpoint."""
    print(f"Testing POST /projects/{project_id}/ship")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(f"{BASE_URL}/projects/{project_id}/ship", headers=headers)
    print_response(response)

def test_get_shipping_info(token, project_id):
    """Tests the /projects/:id/ship endpoint."""
    print(f"Testing GET /projects/{project_id}/ship")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/projects/{project_id}/ship", headers=headers)
    print_response(response)

def test_ai_chat(token):
    """Tests the /ai/chat endpoint."""
    print("Testing POST /ai/chat")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "messages": [{"role": "user", "content": "Hello, world!"}],
        "model": "gpt-3.5-turbo",
        "temperature": 0.7
    }
    response = requests.post(f"{BASE_URL}/ai/chat", json=data, headers=headers)
    print_response(response)

def test_get_ai_model(token):
    """Tests the /ai/model endpoint."""
    print("Testing GET /ai/model")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/ai/model", headers=headers)
    print_response(response)

def test_get_npcs(token):
    """Tests the /npcs endpoint."""
    print("Testing GET /npcs")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/npcs", headers=headers)
    print_response(response)

def test_npc_chat(token):
    """Tests the /npc/:id/chat endpoint."""
    print("Testing POST /npc/1/chat")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "message": "Hello, NPC!",
        "context": "Just saying hi."
    }
    response = requests.post(f"{BASE_URL}/npc/1/chat", json=data, headers=headers)
    print_response(response)

def test_get_inbox(token):
    """Tests the /inbox endpoint."""
    print("Testing GET /inbox")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/inbox", headers=headers)
    print_response(response)

def test_get_leaderboard(token):
    """Tests the /leaderboard endpoint."""
    print("Testing GET /leaderboard")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/leaderboard", headers=headers)
    print_response(response)

def test_get_pdf_report(token):
    """Tests the /reports/pdf endpoint."""
    print("Testing GET /reports/pdf?hackathon=1")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/reports/pdf?hackathon=1", headers=headers)
    print_response(response)

def test_get_admin_events(token):
    """Tests the /admin/events endpoint."""
    print("Testing GET /admin/events")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/admin/events", headers=headers)
    print_response(response)

def test_create_admin_event(token):
    """Tests the /admin/events endpoint."""
    print("Testing POST /admin/events")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "event_type": "custom",
        "description": "A special admin-created event.",
        "severity": "high",
        "scheduled_at": "2024-08-20T12:00:00Z",
        "target_participants": [1, 2, 3]
    }
    response = requests.post(f"{BASE_URL}/admin/events", json=data, headers=headers)
    print_response(response)
    if response.status_code == 201:
        return response.json()["event_id"]
    return None

def test_delete_admin_event(token, event_id):
    """Tests the /admin/events/:id endpoint."""
    print(f"Testing DELETE /admin/events/{event_id}")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.delete(f"{BASE_URL}/admin/events/{event_id}", headers=headers)
    print_response(response)

def test_save_data(token, user_id):
    """Tests the /savedata/:userid endpoint."""
    print(f"Testing POST /savedata/{user_id}")
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "data_key": "some_key",
        "data_value": {"foo": "bar"},
        "metadata": {"source": "test_script"}
    }
    response = requests.post(f"{BASE_URL}/savedata/{user_id}", json=data, headers=headers)
    print_response(response)

def test_get_data(token, user_id):
    """Tests the /data/:userid endpoint."""
    print(f"Testing GET /data/{user_id}")
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{BASE_URL}/data/{user_id}", headers=headers)
    print_response(response)

if __name__ == "__main__":
    user_id = test_register()
    token = test_login()

    if token and user_id:
        test_get_me(token)
        test_game_state(token)
        test_game_action(token)
        test_save_game(token)
        test_get_random_event(token)
        test_get_participants(token)
        participant_id = test_create_participant(token)
        if participant_id:
            test_get_participant(token, participant_id)
            test_update_participant(token, participant_id)
            test_get_housing_listings(token)
            application_id = test_apply_for_housing(token, participant_id)
            if application_id:
                test_get_housing_application(token, application_id)
                test_update_housing_application(token, application_id)
            test_wakatime_webhook(token)
            test_get_commits(token, participant_id)
            test_get_devlogs(token, participant_id)
            test_create_devlog(token, participant_id)
            stipend_id = test_request_stipend(token, participant_id)
            if stipend_id:
                test_get_stipend(token, stipend_id)
                test_approve_stipend(token, stipend_id)
            flight_id = test_request_flight(token, participant_id)
            if flight_id:
                test_get_flight(token, flight_id)
            receipt_id = test_create_receipt(token, participant_id)
            if receipt_id:
                test_get_receipt(token, receipt_id)
            test_get_participant_receipts(token, participant_id)
            project_id = test_create_project(token, participant_id)
            if project_id:
                test_get_project(token, project_id)
                test_update_project(token, project_id)
                test_ship_project(token, project_id)
                test_get_shipping_info(token, project_id)
                test_delete_project(token, project_id)

            test_delete_participant(token, participant_id)

        test_ai_chat(token)
        test_get_ai_model(token)
        test_get_npcs(token)
        test_npc_chat(token)
        test_get_inbox(token)
        test_get_leaderboard(token)
        test_get_pdf_report(token)
        test_get_admin_events(token)
        event_id = test_create_admin_event(token)
        if event_id:
            test_delete_admin_event(token, event_id)
        test_save_data(token, user_id)
        test_get_data(token, user_id)

        test_logout(token)
