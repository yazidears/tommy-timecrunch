🧠 JULIAN’S FULL BACKEND SPEC

Project: Tommy Timecrunch
Tech: Python + Flask + Threads + AI + Chaos
Goal: Real-time multiplayer simulation where the player acts as an overworked hackathon organizer trying to manage an international remote + in-person program. Backend must simulate users, generate chaos, handle time pressure, and keep everything alive without frontend input.

⸻

⚙️ SERVER ARCHITECTURE

🔁 1. GAME LOOP ENGINE (runs every 10 seconds)
    •    Automatically advances game state for all users
    •    Checks deadlines, stress, finances, commitments
    •    Triggers random events and unexpected drama
    •    Injects new participants and incidents without user input
    •    Runs in background (threading or APScheduler)

🧠 2. GLOBAL STATE MANAGER
    •    Stores the entire universe:

{
  "users": {},
  "participants": {},
  "hackathons": {},
  "housing": [],
  "flights": [],
  "stipends": [],
  "receipts": [],
  "npcs": {},
  "emails": {},
  "logs": [],
  "tick": 19283
}



⸻

👤 USER + AUTH
    •    POST /api/register – email, username, password (hash w/ bcrypt)
    •    POST /api/login – issue JWT/session
    •    GET /api/me – return session user + game state
    •    GET /api/logout – invalidate token/session

⸻

🛠️ CORE GAME ENDPOINTS

🎮 Game Logic
    •    GET /api/game/state – full current state snapshot (time, stress, budget)
    •    POST /api/game/action – submit an action (approve, assign, reject, etc.)
    •    POST /api/game/save – save state (auto or manual)
    •    GET /api/game/events/random – trigger random event

⏱️ Simulation Engine
    •    Autogenerate participants every few ticks
    •    Auto-expire leases, receipts, commitments
    •    Track rep/stress/time stats per player
    •    Introduce unpredictable chaos:
    •    network outage
    •    developer goes missing
    •    fake complaint
    •    lawsuit threat
    •    missing stipend

⸻

🧍 PARTICIPANTS (REAL + SIMULATED)
    •    GET /api/hackathons/:id/participants
    •    POST /api/hackathons/:id/participants
    •    GET /api/participants/:id
    •    PUT /api/participants/:id
    •    DELETE /api/participants/:id

Additional logic:
    •    Autogenerate participants every 60 seconds
    •    Assign:
    •    fake GitHub/WakaTime stats
    •    complaints, praise, or drama
    •    broken flights, fake receipts

⸻

🏠 HOUSING SIMULATION
    •    GET /api/housing/listings
    •    POST /api/housing/apply
    •    GET /api/housing/applications/:id
    •    PUT /api/housing/applications/:id

Extra logic:
    •    Every house has limited time lease
    •    Generate housing dynamically via AI
    •    Expire leases → create chaos if participant is unhoused
    •    Handle oversubscription = lawsuits

⸻

💻 COMMIT + DEVLOG TRACKING
    •    POST /api/webhooks/wakatime – fake webhook parser
    •    GET /api/participants/:id/commits
    •    GET /api/participants/:id/devlogs
    •    POST /api/participants/:id/devlogs

Game logic:
    •    Missing devlogs = drops rep
    •    No commits = red alert
    •    Streaks = bonuses / praise

⸻

💶 STIPENDS & FLIGHTS
    •    POST /api/stipends/request
    •    GET /api/stipends/:id
    •    PUT /api/stipends/:id/approve
    •    POST /api/flights/request
    •    GET /api/flights/:id

Game logic:
    •    Auto-deny suspicious requests
    •    Trigger fraud events
    •    Calculate total budget used vs left

⸻

📎 RECEIPT VALIDATION
    •    POST /api/receipts – file upload
    •    GET /api/receipts/:id
    •    GET /api/participants/:id/receipts

Backend logic:
    •    Classify receipts by AI:
    •    valid, duplicated, fake, missing
    •    Add approval flag
    •    Flag any user with 2+ suspicious receipts

⸻

📦 PROJECT SUBMISSION & SHIPPING
    •    POST /api/projects
    •    GET /api/projects/:id
    •    PUT /api/projects/:id
    •    DELETE /api/projects/:id
    •    POST /api/projects/:id/ship
    •    GET /api/projects/:id/ship

Backend logic:
    •    Block shipping if project not finished
    •    Track shipping status (simulated)
    •    Force 2 phases: pre-SF and post-SF

⸻

💬 AI / NPC INTEGRATION

🔗 Proxy endpoints:
    •    POST /api/ai/chat – forward to https://ai.hackclub.com/chat/completions
    •    GET /api/ai/model – forward to /model

💬 AI Use Cases:
    •    Generate:
    •    NPC responses
    •    Complaint messages
    •    Housing descriptions
    •    Threats and compliments
    •    Summary reports
    •    Add NPC memory:
    •    GET /api/npcs
    •    POST /api/npc/:id/chat

⸻

📩 INBOX / EMAIL ENGINE
    •    GET /api/inbox – list of emails from participants, AI, NPCs
    •    Each tick: generate 1-3 random inbox messages
    •    e.g., “WHERE IS MY STIPEND”
    •    “hi tommy i am being bullied”

⸻

🔔 REAL-TIME WEBSOCKETS

(If using Flask-SocketIO)
    •    /ws/notifications – push:
    •    events
    •    NPC messages
    •    legal threats
    •    receipts flagged
    •    panic alerts

⸻

📊 LEADERBOARD / REPORTING
    •    GET /api/leaderboard
    •    GET /api/reports/pdf?hackathon=:id

⸻

🔒 ADMIN
    •    GET /api/admin/events
    •    POST /api/admin/events
    •    DELETE /api/admin/events/:id

⸻

📁 FILES & ASSETS
    •    /uploads/ – receipts, project files
    •    /assets/ – NPC avatars, housing images

⸻

🧨 SERVER BEHAVIOR (REQUIRED)
    •    Game should continue with or without frontend connected
    •    Simulated participants MUST keep doing stuff:
    •    committing
    •    asking for help
    •    causing issues
    •    Server should self-destruct if overloaded
    •    Everything must be customizable in JSON
    •    Logs must track everything

⸻
ANOTHER THING> for the Frontend side of things, I may use some data, so a field in the database when being asked for the user endpoint, there should be a /savedata/(userid) for POST and /data/(userid) for future features that happen on frontend but have to be saved.