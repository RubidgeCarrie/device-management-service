-- Drop tables if they exist
DROP TABLE IF EXISTS security_cameras CASCADE;
DROP TABLE IF EXISTS thermostats CASCADE;
DROP TABLE IF EXISTS smart_lights CASCADE;
DROP TABLE IF EXISTS devices CASCADE;

-- Drop enums if they exist
DROP TYPE IF EXISTS device_types_enum;
DROP TYPE IF EXISTS device_status_enum;
DROP TYPE IF EXISTS smart_light_status_enum;
DROP TYPE IF EXISTS security_camera_status_enum;

-- Create Enums
CREATE TYPE device_types_enum AS ENUM ('smart_lights', 'thermostats', 'secuirty_cameras');
CREATE TYPE device_status_enum AS ENUM ('ON', 'OFF');
CREATE TYPE smart_light_status_enum AS ENUM ('on', 'off');
CREATE TYPE security_camera_status_enum AS ENUM ('armed', 'disarmed');

-- Create Devices Table
CREATE TABLE devices (
    id SERIAL PRIMARY KEY,
    device_type device_types_enum NOT NULL,
    ip_address INET NOT NULL,
    is_online BOOLEAN NOT NULL
);

-- Create Smart Lights Table
CREATE TABLE smart_lights (
    id SERIAL PRIMARY KEY,
    device_id INTEGER REFERENCES devices(id) ON DELETE CASCADE,
    last_updated TIMESTAMP,
    status smart_light_status_enum
);

-- Create Thermostats Table
CREATE TABLE thermostats (
    id SERIAL PRIMARY KEY,
    device_id INTEGER REFERENCES devices(id) ON DELETE CASCADE,
    last_updated TIMESTAMP,
    temperature INTEGER,
    humidity INTEGER
);

-- Create Security Cameras Table
CREATE TABLE security_cameras (
    id SERIAL PRIMARY KEY,
    device_id INTEGER REFERENCES devices(id) ON DELETE CASCADE,
    last_updated TIMESTAMP,
    status security_camera_status_enum
);
