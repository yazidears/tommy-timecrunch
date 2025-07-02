import requests
import json

BASE_URL = "http://127.0.0.1:5000/api"

def print_response(response):
    print(f"Status Code: {response.status_code}")
    try:
        print(f"Response JSON: {json.dumps(response.json(), indent=2)}")
    except json.JSONDecodeError:
        print(f"Response Text: {response.text}")
    print("-"*20)


# --- USER + AUTH ---
def test_user_auth():
    print("--- Testing User + Auth Endpoints ---")
    # Register
    print("Testing POST /api/register")
    register_data = {
        "username": "testuser",
        "password": "password",
        "email": "test@example.com"
    }
    response = requests.post(f"{BASE_URL}/register", json=register_data)
    print_response(response)
    user_id = response.json().get('user_id')

    # Login
    print("Testing POST /api/login")
    login_data = {
        "username": "testuser",
        "password": "password"
    }
    response = requests.post(f"{BASE_URL}/login", json=login_data)
    print_response(response)
    token = response.json().get('token')

    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Get Me
    print("Testing GET /api/me")
    response = requests.get(f"{BASE_URL}/me", headers=headers)
    print_response(response)

    # Logout
    print("Testing GET /api/logout")
    response = requests.get(f"{BASE_URL}/logout", headers=headers)
    print_response(response)

# --- CORE GAME ENDPOINTS ---
def test_game_endpoints(headers):
    print("--- Testing Core Game Endpoints ---")
    # Get Game State
    print("Testing GET /api/game/state")
    response = requests.get(f"{BASE_URL}/game/state", headers=headers)
    print_response(response)

    # Post Game Action
    print("Testing POST /api/game/action")
    action_data = {
        "action_type": "some_action",
        "target_id": 1,
        "parameters": {}
    }
    response = requests.post(f"{BASE_URL}/game/action", json=action_data, headers=headers)
    print_response(response)

    # Save Game
    print("Testing POST /api/game/save")
    response = requests.post(f"{BASE_URL}/game/save", headers=headers)
    print_response(response)

    # Get Random Event
    print("Testing GET /api/game/events/random")
    response = requests.get(f"{BASE_URL}/game/events/random", headers=headers)
    print_response(response)

# --- PARTICIPANTS ---
def test_participant_endpoints(headers):
    print("--- Testing Participant Endpoints ---")
    # This assumes a hackathon with id=1 exists
    hackathon_id = 1

    # Get Participants
    print(f"Testing GET /api/hackathons/{hackathon_id}/participants")
    response = requests.get(f"{BASE_URL}/hackathons/{hackathon_id}/participants", headers=headers)
    print_response(response)

    # Create Participant
    print(f"Testing POST /api/hackathons/{hackathon_id}/participants")
    participant_data = {
        "name": "Test Participant",
        "email": "participant@example.com",
        "github_username": "testparticipant",
        "skills": ["python", "flask"]
    }
    response = requests.post(f"{BASE_URL}/hackathons/{hackathon_id}/participants", json=participant_data, headers=headers)
    print_response(response)
    participant_id = response.json().get('participant_id')

    if not participant_id:
        print("Could not get participant_id, skipping remaining participant tests.")
        return

    # Get Participant by ID
    print(f"Testing GET /api/participants/{participant_id}")
    response = requests.get(f"{BASE_URL}/participants/{participant_id}", headers=headers)
    print_response(response)

    # Update Participant
    print(f"Testing PUT /api/participants/{participant_id}")
    update_data = {
        "name": "Updated Participant Name"
    }
    response = requests.put(f"{BASE_URL}/participants/{participant_id}", json=update_data, headers=headers)
    print_response(response)

    # Delete Participant
    print(f"Testing DELETE /api/participants/{participant_id}")
    response = requests.delete(f"{BASE_URL}/participants/{participant_id}", headers=headers)
    print_response(response)

# --- HOUSING ---
def test_housing_endpoints(headers):
    print("--- Testing Housing Endpoints ---")
    # Get Housing Listings
    print("Testing GET /api/housing/listings")
    response = requests.get(f"{BASE_URL}/housing/listings", headers=headers)
    print_response(response)

    # Apply for Housing
    print("Testing POST /api/housing/apply")
    # This assumes a participant and housing listing exist
    apply_data = {
        "participant_id": 1, # Assuming participant with id 1 exists
        "housing_id": 1, # Assuming housing with id 1 exists
        "check_in_date": "2024-01-01",
        "check_out_date": "2024-01-10"
    }
    response = requests.post(f"{BASE_URL}/housing/apply", json=apply_data, headers=headers)
    print_response(response)
    application_id = response.json().get('application_id')

    if not application_id:
        print("Could not get application_id, skipping remaining housing tests.")
        return

    # Get Housing Application
    print(f"Testing GET /api/housing/applications/{application_id}")
    response = requests.get(f"{BASE_URL}/housing/applications/{application_id}", headers=headers)
    print_response(response)

    # Update Housing Application
    print(f"Testing PUT /api/housing/applications/{application_id}")
    update_data = {
        "status": "approved"
    }
    response = requests.put(f"{BASE_URL}/housing/applications/{application_id}", json=update_data, headers=headers)
    print_response(response)

# --- COMMITS + DEVLOGS ---
def test_commit_devlog_endpoints(headers):
    print("--- Testing Commits + Devlogs Endpoints ---")
    # This assumes a participant with id=1 exists
    participant_id = 1

    # Get Commits
    print(f"Testing GET /api/participants/{participant_id}/commits")
    response = requests.get(f"{BASE_URL}/participants/{participant_id}/commits", headers=headers)
    print_response(response)

    # Get Devlogs
    print(f"Testing GET /api/participants/{participant_id}/devlogs")
    response = requests.get(f"{BASE_URL}/participants/{participant_id}/devlogs", headers=headers)
    print_response(response)

    # Create Devlog
    print(f"Testing POST /api/participants/{participant_id}/devlogs")
    devlog_data = {
        "title": "My First Devlog",
        "content": "This is the content of my first devlog."
    }
    response = requests.post(f"{BASE_URL}/participants/{participant_id}/devlogs", json=devlog_data, headers=headers)
    print_response(response)

# --- STIPENDS + FLIGHTS ---
def test_stipend_flight_endpoints(headers):
    print("--- Testing Stipends + Flights Endpoints ---")
    # This assumes a participant with id=1 exists
    participant_id = 1

    # Request Stipend
    print("Testing POST /api/stipends/request")
    stipend_data = {
        "participant_id": participant_id,
        "amount": 500,
        "justification": "For project supplies"
    }
    response = requests.post(f"{BASE_URL}/stipends/request", json=stipend_data, headers=headers)
    print_response(response)
    stipend_id = response.json().get('stipend_id')

    if stipend_id:
        # Get Stipend
        print(f"Testing GET /api/stipends/{stipend_id}")
        response = requests.get(f"{BASE_URL}/stipends/{stipend_id}", headers=headers)
        print_response(response)

        # Approve Stipend
        print(f"Testing PUT /api/stipends/{stipend_id}/approve")
        approve_data = {"status": "approved"}
        response = requests.put(f"{BASE_URL}/stipends/{stipend_id}/approve", json=approve_data, headers=headers)
        print_response(response)

    # Request Flight
    print("Testing POST /api/flights/request")
    flight_data = {
        "participant_id": participant_id,
        "departure_city": "SFO",
        "arrival_city": "JFK",
        "departure_date": "2024-08-01",
        "return_date": "2024-08-15"
    }
    response = requests.post(f"{BASE_URL}/flights/request", json=flight_data, headers=headers)
    print_response(response)
    flight_id = response.json().get('flight_id')

    if flight_id:
        # Get Flight
        print(f"Testing GET /api/flights/{flight_id}")
        response = requests.get(f"{BASE_URL}/flights/{flight_id}", headers=headers)
        print_response(response)

# --- RECEIPTS ---
def test_receipt_endpoints(headers):
    print("--- Testing Receipts Endpoints ---")
    # This assumes a participant with id=1 exists
    participant_id = 1

    # Create Receipt (mocking file upload)
    print("Testing POST /api/receipts")
    receipt_data = {
        "participant_id": participant_id,
        "category": "food",
        "amount": 25.50,
        "description": "Team lunch"
    }
    # In a real scenario, you would use files={'file': open('receipt.jpg', 'rb')}
    response = requests.post(f"{BASE_URL}/receipts", json=receipt_data, headers=headers)
    print_response(response)
    receipt_id = response.json().get('receipt_id')

    if receipt_id:
        # Get Receipt
        print(f"Testing GET /api/receipts/{receipt_id}")
        response = requests.get(f"{BASE_URL}/receipts/{receipt_id}", headers=headers)
        print_response(response)

    # Get Participant Receipts
    print(f"Testing GET /api/participants/{participant_id}/receipts")
    response = requests.get(f"{BASE_URL}/participants/{participant_id}/receipts", headers=headers)
    print_response(response)


# --- PROJECTS ---
def test_project_endpoints(headers):
    print("--- Testing Projects Endpoints ---")
    # This assumes a participant with id=1 exists
    participant_id = 1

    # Create Project
    print("Testing POST /api/projects")
    project_data = {
        "participant_id": participant_id,
        "title": "My Awesome Project",
        "description": "A project to change the world",
        "repository_url": "https://github.com/user/repo"
    }
    response = requests.post(f"{BASE_URL}/projects", json=project_data, headers=headers)
    print_response(response)
    project_id = response.json().get('project_id')

    if not project_id:
        print("Could not get project_id, skipping remaining project tests.")
        return

    # Get Project
    print(f"Testing GET /api/projects/{project_id}")
    response = requests.get(f"{BASE_URL}/projects/{project_id}", headers=headers)
    print_response(response)

    # Update Project
    print(f"Testing PUT /api/projects/{project_id}")
    update_data = {"title": "My Even More Awesome Project"}
    response = requests.put(f"{BASE_URL}/projects/{project_id}", json=update_data, headers=headers)
    print_response(response)

    # Ship Project
    print(f"Testing POST /api/projects/{project_id}/ship")
    response = requests.post(f"{BASE_URL}/projects/{project_id}/ship", headers=headers)
    print_response(response)

    # Get Shipping Info
    print(f"Testing GET /api/projects/{project_id}/ship")
    response = requests.get(f"{BASE_URL}/projects/{project_id}/ship", headers=headers)
    print_response(response)

    # Delete Project
    print(f"Testing DELETE /api/projects/{project_id}")
    response = requests.delete(f"{BASE_URL}/projects/{project_id}", headers=headers)
    print_response(response)


# --- AI / NPC ---
def test_ai_npc_endpoints(headers):
    print("--- Testing AI / NPC Endpoints ---")

    # AI Chat
    print("Testing POST /api/ai/chat")
    chat_data = {
        "messages": [{"role": "user", "content": "Hello, world!"}]
    }
    response = requests.post(f"{BASE_URL}/ai/chat", json=chat_data, headers=headers)
    print_response(response)

    # Get AI Model
    print("Testing GET /api/ai/model")
    response = requests.get(f"{BASE_URL}/ai/model", headers=headers)
    print_response(response)

    # Get NPCs
    print("Testing GET /api/npcs")
    response = requests.get(f"{BASE_URL}/npcs", headers=headers)
    print_response(response)

    # NPC Chat
    print("Testing POST /api/npc/1/chat") # Assumes NPC with id 1 exists
    npc_chat_data = {
        "message": "How are you?"
    }
    response = requests.post(f"{BASE_URL}/npc/1/chat", json=npc_chat_data, headers=headers)
    print_response(response)

# --- INBOX ---
def test_inbox_endpoints(headers):
    print("--- Testing Inbox Endpoints ---")
    print("Testing GET /api/inbox")
    response = requests.get(f"{BASE_URL}/inbox", headers=headers)
    print_response(response)

# --- REPORTS ---
def test_report_endpoints(headers):
    print("--- Testing Reports Endpoints ---")
    # Get Leaderboard
    print("Testing GET /api/leaderboard")
    response = requests.get(f"{BASE_URL}/leaderboard", headers=headers)
    print_response(response)

    # Get PDF Report
    print("Testing GET /api/reports/pdf?hackathon=1") # Assumes hackathon with id 1 exists
    response = requests.get(f"{BASE_URL}/reports/pdf?hackathon=1", headers=headers)
    print_response(response)

# --- ADMIN ---
def test_admin_endpoints(headers):
    print("--- Testing Admin Endpoints ---")
    # Get Admin Events
    print("Testing GET /api/admin/events")
    response = requests.get(f"{BASE_URL}/admin/events", headers=headers)
    print_response(response)

    # Create Admin Event
    print("Testing POST /api/admin/events")
    event_data = {
        "event_type": "global_announcement",
        "description": "This is a test announcement.",
        "severity": "low"
    }
    response = requests.post(f"{BASE_URL}/admin/events", json=event_data, headers=headers)
    print_response(response)
    event_id = response.json().get('event_id')

    if event_id:
        # Delete Admin Event
        print(f"Testing DELETE /api/admin/events/{event_id}")
        response = requests.delete(f"{BASE_URL}/admin/events/{event_id}", headers=headers)
        print_response(response)

if __name__ == "__main__":
    # It's better to get a token once and pass it to the test functions
    print("--- Initializing Test Script ---")
    register_data = {
        "username": "mainuser",
        "password": "password123",
        "email": "main@example.com"
    }
    requests.post(f"{BASE_URL}/register", json=register_data) # Register a user to be sure one exists

    login_data = {
        "username": "mainuser",
        "password": "password123"
    }
    login_response = requests.post(f"{BASE_URL}/login", json=login_data)
    token = login_response.json().get('token')
    headers = {"Authorization": f"Bearer {token}"}

    test_user_auth()
    test_game_endpoints(headers)
    test_participant_endpoints(headers)
    test_housing_endpoints(headers)
    test_commit_devlog_endpoints(headers)
    test_stipend_flight_endpoints(headers)
    test_receipt_endpoints(headers)
    test_project_endpoints(headers)
    test_ai_npc_endpoints(headers)
    test_inbox_endpoints(headers)
    test_report_endpoints(headers)
    test_admin_endpoints(headers)
