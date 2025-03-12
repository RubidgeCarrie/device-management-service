-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Drop existing tables and types if they exist
DROP TYPE IF EXISTS device_types_enum;
DROP TYPE IF EXISTS device_status_enum;
DROP TYPE IF EXISTS smart_light_status_enum;
DROP TYPE IF EXISTS security_camera_status_enum;

-- Create Enums
CREATE TYPE device_types_enum AS ENUM ('smart_light', 'thermostat', 'security_camera');
CREATE TYPE device_status_enum AS ENUM ('on', 'off');
CREATE TYPE smart_light_status_enum AS ENUM ('on', 'off');
CREATE TYPE security_camera_status_enum AS ENUM ('armed', 'disarmed', 'alarm', 'off');

-- Create device_register table
CREATE TABLE device_register (
    id SERIAL PRIMARY KEY,
    device_type device_types_enum NOT NULL,
    ip_address INET NOT NULL,
    mac_address VARCHAR(17) UNIQUE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- Insert sample data with explicit timestamps
INSERT INTO device_register (device_type, ip_address, mac_address, registration_date) VALUES
    ('smart_light', '192.168.1.10', '00:1b:63:84:45:e6', CURRENT_TIMESTAMP),
    ('thermostat', '192.168.1.11', '00-B0-D0-63-C2-26', CURRENT_TIMESTAMP),
    ('security_camera', '192.168.1.12', 'AA:BB:CC:DD:EE:03', CURRENT_TIMESTAMP);


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

CREATE TABLE IF NOT EXISTS smart_lights (
    id SERIAL PRIMARY KEY,
    device_id INT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(20) NOT NULL, 
    FOREIGN KEY (device_id) REFERENCES device_register(id) ON DELETE CASCADE
);

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
INSERT INTO smart_lights (device_id, timestamp, status)
VALUES 
(0, '2025-03-12 10:00:00', 'on'),
(0, '2025-03-12 12:30:00', 'off'),
(0, '2025-03-12 14:45:00', 'on'),
(0, '2025-03-12 16:20:00', 'off');

