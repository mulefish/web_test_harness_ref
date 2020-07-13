# web_test_harness_ref
Ref arch to test FastAPI restful microservice. Front-end: vanilla JS. Back-end: python. Framework: FastAPI. Transport: Restful. Goal: Ene-to-end 'integration test' of a faux-microservice. 


# NOTES:
This version has removed any DB connection for a pure-play tech-demo. Please see the Master branch for example w/ postgres. 

# How to run: 
uvicorn main:app --reload 

# URL template: 
http://127.0.0.1:8000/items/26 
http://127.0.0.1:8000/test_page 


# Swagger: 
http://127.0.0.1:8000/events_docs/ 



