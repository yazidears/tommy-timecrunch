-- filepath: /Users/julianstosse/Tommy Timecrunsch backend/adDemoData.sql

-- Insert demo data into the User table
INSERT INTO user (username, email, password_hash, game_state, stress_level, budget, reputation, current_tick)
VALUES 
('john_doe', 'john@example.com', 'hashed_password_1', '{}', 10, 50000.0, 80, 5),
('jane_smith', 'jane@example.com', 'hashed_password_2', '{}', 5, 75000.0, 90, 3);

-- Insert demo data into the Project table
INSERT INTO project (name, description, start_date, end_date, budget, creator_id)
VALUES 
('Project Alpha', 'A top-secret project.', '2023-01-01', '2023-12-31', 100000.0, 1),
('Project Beta', 'A public-facing initiative.', '2023-06-01', '2023-11-30', 50000.0, 2);

-- Insert demo data into the ProjectParticipant table
INSERT INTO project_participant (project_id, user_id, role)
VALUES 
(1, 1, 'Manager'),
(1, 2, 'Developer'),
(2, 2, 'Manager');

-- Insert demo data into the Task table
INSERT INTO task (project_id, title, description, due_date, status, assignee_id)
VALUES 
(1, 'Design Database', 'Create the initial database schema.', '2023-02-01', 'In Progress', 1),
(1, 'Develop API', 'Build the REST API for the project.', '2023-03-01', 'To Do', 2),
(2, 'Marketing Campaign', 'Launch the marketing campaign.', '2023-07-01', 'To Do', 2);

-- Insert demo data into the Commit table
INSERT INTO "commit" (project_id, user_id, message, hash)
VALUES 
(1, 1, 'Initial commit with database schema.', 'abc123'),
(1, 2, 'Added API endpoints.', 'def456');

-- Insert demo data into the Devlog table
INSERT INTO devlog (project_id, user_id, title, content)
VALUES 
(1, 1, 'Database Design', 'Completed the initial database design.'),
(1, 2, 'API Development', 'Started working on API endpoints.');

-- Insert demo data into the Report table
INSERT INTO report (project_id, user_id, title, content)
VALUES 
(1, 1, 'Weekly Progress Report', 'Completed database design and started API development.'),
(2, 2, 'Marketing Update', 'Prepared materials for the upcoming campaign.');

-- Insert demo data into the Inbox table
INSERT INTO inbox (user_id)
VALUES 
(1),
(2);

-- Insert demo data into the Message table
INSERT INTO message (inbox_id, sender_id, recipient_id, subject, body)
VALUES 
(1, 2, 1, 'Welcome to Project Alpha', 'Looking forward to working with you on this project.'),
(2, 1, 2, 'API Development', 'Please update me on your progress.');

-- Insert demo data into the Receipt table
INSERT INTO receipt (project_id, user_id, store_name, item_name, amount, purchase_date, image_url)
VALUES 
(1, 1, 'Tech Store', 'Laptop', 1200.0, '2023-01-15', 'http://example.com/laptop.jpg'),
(2, 2, 'Office Supplies', 'Printer', 300.0, '2023-06-10', 'http://example.com/printer.jpg');

-- Insert demo data into the Stipend table
INSERT INTO stipend (project_id, user_id, amount, payment_date, description)
VALUES 
(1, 1, 2000.0, '2023-01-31', 'Monthly stipend for January.'),
(2, 2, 1500.0, '2023-06-30', 'Monthly stipend for June.');

-- Insert demo data into the Flight table
INSERT INTO flight (project_id, user_id, airline, flight_number, departure_airport, arrival_airport, departure_datetime, arrival_datetime, cost)
VALUES 
(1, 1, 'AirTech', 'AT123', 'JFK', 'LAX', '2023-02-01 08:00:00', '2023-02-01 11:00:00', 300.0),
(2, 2, 'SkyFly', 'SF456', 'ORD', 'SFO', '2023-06-15 09:00:00', '2023-06-15 12:00:00', 400.0);

-- Insert demo data into the Housing table
INSERT INTO housing (project_id, user_id, address, check_in_date, check_out_date, cost)
VALUES 
(1, 1, '123 Main St, Los Angeles, CA', '2023-02-01', '2023-02-10', 1000.0),
(2, 2, '456 Elm St, San Francisco, CA', '2023-06-15', '2023-06-20', 800.0);

-- Insert demo data into the AINPC table
INSERT INTO ai_npc (name, backstory, personality)
VALUES 
('Tommy', 'A quirky AI assistant.', 'Helpful and humorous'),
('Sophia', 'A serious AI with a knack for analytics.', 'Focused and precise');

-- Insert demo data into the Game table
INSERT INTO game (user_id, game_state)
VALUES 
(1, '{"level": 1, "score": 100}'),
(2, '{"level": 2, "score": 200}');