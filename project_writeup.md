

# ASSUMPTIONS

- We currently have three device types smart lights, thermostats, security cameras
- 

# Architecture Decisions

## Database

## User of ORMs







device_type: smart lights to thermostats or security cameras.
address: mac/ip 
status: online/offline
battery: 
(sending out ping)
heartbeat: timestamp
port: 
protocol: ?


- Post
--------
The response should return the details of the registered device, including a unique identifier.
------


# Future improvements

Keep only immutable properties in SQL (id, device_type, registration timestamp).
Store mutable data (status, IP, last_updated, settings) in Redis or a document DB.

Look at using `alembic` to manage migrations

- assumed we have a defined list of device types we want to registar (thermostats, )

table per type of device 


The final design of the database choice and table configuration really depends on our access patterns. To make the correct final choice I would ask questions such as:
1. Will we often be wanting the status/ mutable configuration for our devices? (This would lend itself to)
2. 

Devices

 handling real-time data in an IoT context.

uuid, device_type, 

- smart lights to thermostats or security cameras.

-  users to manage these devices, monitor their status, and control them remotely.

- manage Strate



TODO:

swagger
