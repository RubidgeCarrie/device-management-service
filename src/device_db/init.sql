-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- -- Drop tables if they exist
-- DROP TABLE IF EXISTS security_cameras CASCADE;
-- DROP TABLE IF EXISTS thermostats CASCADE;
-- DROP TABLE IF EXISTS smart_lights CASCADE;
-- DROP TABLE IF EXISTS devices CASCADE;

DROP TYPE IF EXISTS device_types_enum;
DROP TYPE IF EXISTS device_status_enum;
DROP TYPE IF EXISTS smart_light_status_enum;
DROP TYPE IF EXISTS security_camera_status_enum;

-- Create Enums
CREATE TYPE device_types_enum AS ENUM ('smart_light', 'thermostat', 'security_camera');
CREATE TYPE device_status_enum AS ENUM ('ON', 'OFF');
CREATE TYPE smart_light_status_enum AS ENUM ('on', 'off');
CREATE TYPE security_camera_status_enum AS ENUM ('armed', 'disarmed');

CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    slug VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    hashed_password TEXT NOT NULL,
    is_superuser BOOLEAN DEFAULT FALSE
);

INSERT INTO "user" (username, slug, email, first_name, last_name, hashed_password, is_superuser) VALUES
('admin', 'admin', 'admin@example.com', 'Admin', 'User', '$2b$12$abcdefghijklmnopqrstuv', TRUE),
('johndoe', 'john-doe', 'johndoe@example.com', 'John', 'Doe', '$2b$12$mnopqrstuvabcdefghijkl', FALSE),
('janedoe', 'jane-doe', 'janedoe@example.com', 'Jane', 'Doe', '$2b$12$uvwxyzabcdefghijklmno', FALSE);


-- -- Create Devices Table
-- CREATE TABLE IF NOT EXISTS devices (
--     -- id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
--     id SERIAL PRIMARY KEY,
--     device_type device_types_enum NOT NULL,
--     -- ip_address INET NOT NULL,
--     registration_date TIMESTAMP DEFAULT NOW()
-- );

-- ----


-- Create devices table
CREATE TABLE device_register (
    id SERIAL PRIMARY KEY,
    device_type device_types_enum NOT NULL,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    is_online BOOLEAN DEFAULT NULL
);

-- Insert sample data
INSERT INTO device_register (device_type, registration_date, is_online) VALUES
    ('smart_light', CURRENT_TIMESTAMP, TRUE),
    ('thermostat', CURRENT_TIMESTAMP, FALSE),
    ('security_camera', CURRENT_TIMESTAMP, NULL);

--
-- -- Create Smart Lights Table
-- CREATE TABLE IF NOT EXISTS smart_lights (
--     -- id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
--     id SERIAL PRIMARY KEY,
--     device_id INT REFERENCES device_register(id) ON DELETE CASCADE,
--     -- is_online BOOLEAN NOT NULL DEFAULT TRUE,
--     status 
--     last_updated TIMESTAMP DEFAULT NOW(),
--     status smart_light_status_enum
-- );
-- BaseDevice table

-- SmartLights table
CREATE TABLE smart_lights (
    id SERIAL PRIMARY KEY,
    device_id INT NOT NULL,
    timestamp TIMESTAMP NOT NULL,
    status SMALLINT NOT NULL CHECK (status IN (0, 1)),
    FOREIGN KEY (device_id) REFERENCES device_register(id) ON DELETE CASCADE
);

-- Insert sample data with explicit timestamps
INSERT INTO smart_lights (device_id, timestamp, status) VALUES 
(1, '2025-03-10 12:00:00', 1),  -- Online
(2, '2025-03-10 13:30:00', 0),  -- Offline
(3, '2025-03-10 14:45:00', 1);  -- Online



-- -- Create Thermostats Table
-- CREATE TABLE IF NOT EXISTS thermostats (
--     -- id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
--     id SERIAL PRIMARY KEY,
--     device_id INT REFERENCES devices(id) ON DELETE CASCADE,
--     is_online BOOLEAN NOT NULL DEFAULT TRUE,
--     last_updated TIMESTAMP DEFAULT NOW(),
--     temperature INTEGER,
--     humidity INTEGER
-- );

-- -- Create Security Cameras Table
-- CREATE TABLE security_cameras (
--     id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
--     device_id UUID REFERENCES devices(id) ON DELETE CASCADE,
--     is_online BOOLEAN NOT NULL DEFAULT TRUE,
--     last_updated TIMESTAMP DEFAULT NOW(),
--     status security_camera_status_enum
-- );



-- Insert Fake Data into Devices Table
-- INSERT INTO devices (id, device_type, ip_address, registration_date) VALUES
--     ('550e8400-e29b-41d4-a716-446655440000', 'smart_light', '192.168.1.10', NOW()),
--     ('550e8400-e29b-41d4-a716-446655440001', 'thermostat', '192.168.1.11', NOW()),
--     ('550e8400-e29b-41d4-a716-446655440002', 'security_camera', '192.168.1.12', NOW());

-- INSERT INTO devices (id, device_type, ip_address, registration_date) VALUES
--     ('1', 'smart_light', '192.168.1.10', NOW()),
--     ('2', 'thermostat', '192.168.1.11', NOW()),
--     ('3', 'security_camera', '192.168.1.12', NOW());

-- Insert Fake Data into Smart Lights Table
-- INSERT INTO smart_lights (id, device_id, is_online, last_updated, status) VALUES
--     (1, 1, TRUE, NOW(), 'on'),
--     (2, 2, FALSE, NOW(), 'off');

-- -- Insert Fake Data into Thermostats Table
-- INSERT INTO thermostats (id, device_id, is_online, last_updated, temperature, humidity) VALUES
--     (gen_random_uuid(), '550e8400-e29b-41d4-a716-446655440001', TRUE, NOW(), 72, 40),
--     (gen_random_uuid(), '550e8400-e29b-41d4-a716-446655440001', FALSE, NOW(), 65, 50);

-- -- Insert Fake Data into Security Cameras Table
-- INSERT INTO security_cameras (id, device_id, is_online, last_updated, status) VALUES
--     (gen_random_uuid(), '550e8400-e29b-41d4-a716-446655440002', TRUE, NOW(), 'armed'),
--     (gen_random_uuid(), '550e8400-e29b-41d4-a716-446655440002', FALSE, NOW(), 'disarmed');
