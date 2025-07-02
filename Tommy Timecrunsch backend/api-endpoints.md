# API ENDPOINTS

## 👤 USER + AUTH

### POST /api/register
**Returns:**
- user_id
- username
- email
- created_at

### POST /api/login
**Returns:**
- token
- user_id
- username
- expires_at

### GET /api/me
**Returns:**
- user_id
- username
- email
- game_state
- stress_level
- budget
- reputation
- current_tick

### GET /api/logout
**Returns:**
- success
- message

## 🎮 CORE GAME ENDPOINTS

### GET /api/game/state
**Returns:**
- tick
- time_remaining
- stress_level
- budget_used
- budget_total
- reputation
- active_events
- pending_actions

### POST /api/game/action
**Body:**
- action_type
- target_id
- parameters

**Returns:**
- success
- new_state
- consequences
- stress_change
- reputation_change

### POST /api/game/save
**Returns:**
- success
- saved_at
- tick

### GET /api/game/events/random
**Returns:**
- event_id
- event_type
- description
- severity
- participants_affected
- deadline

## 🧍 PARTICIPANTS

### GET /api/hackathons/:id/participants
**Returns:**
- participant_id
- name
- email
- github_username
- status
- stress_level
- commit_count
- housing_status

### POST /api/hackathons/:id/participants
**Body:**
- name
- email
- github_username
- skills

**Returns:**
- participant_id
- name
- email
- status
- created_at

### GET /api/participants/:id
**Returns:**
- participant_id
- name
- email
- github_username
- commit_count
- devlog_count
- housing_id
- stipend_amount
- flight_status
- stress_level
- last_active

### PUT /api/participants/:id
**Body:**
- name
- email
- status
- housing_id

**Returns:**
- participant_id
- updated_fields
- updated_at

### DELETE /api/participants/:id
**Returns:**
- success
- deleted_at

## 🏠 HOUSING

### GET /api/housing/listings
**Returns:**
- housing_id
- title
- description
- capacity
- occupied_spots
- lease_expiry
- price_per_night
- location

### POST /api/housing/apply
**Body:**
- participant_id
- housing_id
- check_in_date
- check_out_date

**Returns:**
- application_id
- status
- housing_id
- participant_id
- created_at

### GET /api/housing/applications/:id
**Returns:**
- application_id
- participant_id
- housing_id
- status
- check_in_date
- check_out_date
- created_at

### PUT /api/housing/applications/:id
**Body:**
- status
- check_in_date
- check_out_date

**Returns:**
- application_id
- status
- updated_at

## 💻 COMMITS + DEVLOGS

### POST /api/webhooks/wakatime
**Body:**
- participant_id
- coding_time
- languages
- projects

**Returns:**
- success
- processed_at

### GET /api/participants/:id/commits
**Returns:**
- commit_id
- message
- timestamp
- repository
- lines_added
- lines_removed

### GET /api/participants/:id/devlogs
**Returns:**
- devlog_id
- title
- content
- timestamp
- word_count
- sentiment

### POST /api/participants/:id/devlogs
**Body:**
- title
- content

**Returns:**
- devlog_id
- title
- content
- timestamp
- word_count

## 💶 STIPENDS + FLIGHTS

### POST /api/stipends/request
**Body:**
- participant_id
- amount
- justification
- receipt_urls

**Returns:**
- stipend_id
- participant_id
- amount
- status
- created_at

### GET /api/stipends/:id
**Returns:**
- stipend_id
- participant_id
- amount
- status
- justification
- receipt_urls
- approved_by
- approved_at

### PUT /api/stipends/:id/approve
**Body:**
- status
- admin_notes

**Returns:**
- stipend_id
- status
- approved_by
- approved_at

### POST /api/flights/request
**Body:**
- participant_id
- departure_city
- arrival_city
- departure_date
- return_date
- estimated_cost

**Returns:**
- flight_id
- participant_id
- departure_city
- arrival_city
- departure_date
- return_date
- status
- created_at

### GET /api/flights/:id
**Returns:**
- flight_id
- participant_id
- departure_city
- arrival_city
- departure_date
- return_date
- actual_cost
- status
- booking_reference

## 📎 RECEIPTS

### POST /api/receipts
**Body:**
- participant_id
- file
- category
- amount
- description

**Returns:**
- receipt_id
- participant_id
- filename
- category
- amount
- status
- uploaded_at

### GET /api/receipts/:id
**Returns:**
- receipt_id
- participant_id
- filename
- category
- amount
- status
- ai_validation
- flagged_reason
- uploaded_at

### GET /api/participants/:id/receipts
**Returns:**
- receipt_id
- filename
- category
- amount
- status
- ai_validation
- uploaded_at

## 📦 PROJECTS

### POST /api/projects
**Body:**
- participant_id
- title
- description
- repository_url

**Returns:**
- project_id
- participant_id
- title
- description
- repository_url
- status
- created_at

### GET /api/projects/:id
**Returns:**
- project_id
- participant_id
- title
- description
- repository_url
- status
- completion_percentage
- last_commit
- shipping_status

### PUT /api/projects/:id
**Body:**
- title
- description
- repository_url
- status

**Returns:**
- project_id
- updated_fields
- updated_at

### DELETE /api/projects/:id
**Returns:**
- success
- deleted_at

### POST /api/projects/:id/ship
**Returns:**
- project_id
- shipping_status
- tracking_number
- estimated_delivery
- shipped_at

### GET /api/projects/:id/ship
**Returns:**
- project_id
- shipping_status
- tracking_number
- current_location
- estimated_delivery
- shipped_at

## 💬 AI / NPC

### POST /api/ai/chat
**Body:**
- messages
- model
- temperature

**Returns:**
- response
- model_used
- tokens_used
- timestamp

### GET /api/ai/model
**Returns:**
- available_models
- default_model
- rate_limits

### GET /api/npcs
**Returns:**
- npc_id
- name
- role
- personality
- last_interaction
- memory_count

### POST /api/npc/:id/chat
**Body:**
- message
- context

**Returns:**
- npc_id
- response
- emotion
- timestamp
- memory_stored

## 📩 INBOX

### GET /api/inbox
**Returns:**
- email_id
- from_name
- from_email
- subject
- content
- priority
- read_status
- timestamp
- category

## 🔔 WEBSOCKETS

### /ws/notifications
**Pushes:**
- event_type
- message
- severity
- participant_id
- timestamp
- requires_action

## 📊 REPORTS

### GET /api/leaderboard
**Returns:**
- participant_id
- name
- score
- rank
- commit_count
- devlog_count
- reputation

### GET /api/reports/pdf?hackathon=:id
**Returns:**
- file_url
- generated_at
- report_type
- hackathon_id

## 🔒 ADMIN

### GET /api/admin/events
**Returns:**
- event_id
- event_type
- description
- severity
- scheduled_at
- executed_at
- participants_affected

### POST /api/admin/events
**Body:**
- event_type
- description
- severity
- scheduled_at
- target_participants

**Returns:**
- event_id
- event_type
- scheduled_at
- created_at

### DELETE /api/admin/events/:id
**Returns:**
- success
- deleted_at

## 💾 FRONTEND DATA

### POST /api/savedata/:userid
**Body:**
- data_key
- data_value
- metadata

**Returns:**
- success
- saved_at
- data_key

### GET /api/data/:userid
**Returns:**
- user_id
- data_key
- data_value
- metadata