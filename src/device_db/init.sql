-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Drop existing tables and types if they exist
DROP TYPE IF EXISTS device_types_enum;
DROP TYPE IF EXISTS device_status_enum;
DROP TYPE IF EXISTS thermostat_status_enum;
DROP TYPE IF EXISTS security_camera_status_enum;

-- Create Enums
CREATE TYPE device_types_enum AS ENUM ('smart_light', 'thermostat', 'security_camera');
CREATE TYPE device_status_enum AS ENUM ('on', 'off');
CREATE TYPE thermostat_status_enum AS ENUM ('on', 'off');
CREATE TYPE security_camera_status_enum AS ENUM ('armed', 'disarmed', 'alarm', 'off');

-- Create device_register table
CREATE TABLE device_register (
    id SERIAL PRIMARY KEY,
    device_type device_types_enum NOT NULL,
    ip_address INET NOT NULL,
    mac_address VARCHAR(17) UNIQUE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
);

-- -- Create Thermostats Table
CREATE TABLE IF NOT EXISTS thermostats (
    id SERIAL PRIMARY KEY,
    device_id INT NOT NULL,
    temperature INTEGER,
    humidity INTEGER,
    timestamp TIMESTAMP DEFAULT NOW(),
    status thermostat_status_enum NOT NULL, 
    FOREIGN KEY (device_id) REFERENCES device_register(id) ON DELETE CASCADE
);

-- -- Create Security Cameras Table
CREATE TABLE IF NOT EXISTS security_cameras (
    id SERIAL PRIMARY KEY,
    device_id INT NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status security_camera_status_enum NOT NULL, 
    FOREIGN KEY (device_id) REFERENCES device_register(id) ON DELETE CASCADE
);
---------------------
-- Insert sample data
---------------------

INSERT INTO device_register (device_type, ip_address, mac_address, registration_date) VALUES
    ('smart_light', '192.168.1.10', '00:1b:63:84:45:e6', CURRENT_TIMESTAMP),
    ('thermostat', '192.168.1.11', '00-B0-D0-63-C2-26', CURRENT_TIMESTAMP),
    ('security_camera', '192.168.1.12', 'AA:BB:CC:DD:EE:03', CURRENT_TIMESTAMP);

INSERT INTO security_cameras (device_id, timestamp, status)
VALUES 
(3, '2025-03-12 12:30:00', 'armed'),
(3, '2025-03-12 14:45:00', 'disarmed'),
(3, '2025-03-12 16:20:00', 'off');

INSERT INTO thermostats (device_id, temperature, humidity, timestamp, status)
VALUES 
    (2, 22, 45, '2025-03-12 08:30:00', 'on'),
    (2, 20, 50, '2025-03-12 10:15:00', 'off'),
    (2, 24, 40, '2025-03-12 12:00:00', 'on'),
    (2, 21, 55, '2025-03-12 14:45:00', 'off'),
    (2, 23, 48, '2025-03-12 16:20:00', 'on');
