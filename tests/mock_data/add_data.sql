-- Insert Fake Data into Devices Table
INSERT INTO devices (id, device_type, ip_address, registration_date) VALUES
    ('550e8400-e29b-41d4-a716-446655440000', 'smart_lights', '192.168.1.10', NOW()),
    ('550e8400-e29b-41d4-a716-446655440001', 'thermostat', '192.168.1.11', NOW()),
    ('550e8400-e29b-41d4-a716-446655440002', 'security_camera', '192.168.1.12', NOW());

-- Insert Fake Data into Smart Lights Table
INSERT INTO smart_lights (id, device_id, is_online, last_updated, status) VALUES
    (gen_random_uuid(), '550e8400-e29b-41d4-a716-446655440000', TRUE, NOW(), 'on'),
    (gen_random_uuid(), '550e8400-e29b-41d4-a716-446655440000', FALSE, NOW(), 'off');

-- Insert Fake Data into Thermostats Table
INSERT INTO thermostats (id, device_id, is_online, last_updated, temperature, humidity) VALUES
    (gen_random_uuid(), '550e8400-e29b-41d4-a716-446655440001', TRUE, NOW(), 72, 40),
    (gen_random_uuid(), '550e8400-e29b-41d4-a716-446655440001', FALSE, NOW(), 65, 50);

-- Insert Fake Data into Security Cameras Table
INSERT INTO security_cameras (id, device_id, is_online, last_updated, status) VALUES
    (gen_random_uuid(), '550e8400-e29b-41d4-a716-446655440002', TRUE, NOW(), 'armed'),
    (gen_random_uuid(), '550e8400-e29b-41d4-a716-446655440002', FALSE, NOW(), 'disarmed');
