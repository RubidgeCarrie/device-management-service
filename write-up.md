# Architecture Decision Record

# Assumptions

1. Device details do not include their status

## Database choice
Given the nature of the endpoints they could have been implemented on a NoSQL database, such as MongoDB.



## API server

I have previosuly made the decision to avoid ORM's and use "raw" SQL and our own 

FastAPI: Web framework for building APIs with Python
SQLAlchemy: ORM for python 
Pydantic: Model Validation, integrates well with FastAPi for swagger documentation



## Path to Production

The API Server is running in a container making it easy to host on an EC2 using a 

However, were this meant for production, being AWS based I would have preferenced a cloud native solution for the API's, such as API Gateway with lambda integration to handle the requests. This would allow us to more scale with options such as caching on API Gateway, 




## Challenges

It was great getting a chance to work with FastAPI but it definitely had some limitations and difficulties. 

- UUIDS don't work natively with FastAPI and pydantic model validation
- 


## Future updates

If I was continuing to use this

- Alembic db migrations
- Asynchornous requests rather than synchronous requests


# TODO:

- authentication
- testing
##

