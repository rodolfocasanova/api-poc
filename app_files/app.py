from prometheus_client import start_http_server, Counter, Summary
from fastapi import FastAPI
import time
import random
import json

app = FastAPI()

# Initialize metrics
REQUEST_COUNT = Counter('myapp_request_count', 'Total number of requests', ['service', 'endpoint'])
REQUEST_TIME = Summary('myapp_request_processing_seconds', 'Request processing time in seconds', ['service', 'endpoint'])

data = {
    "name": "John Doe",
    "email": "johndoe@example.com"
    }

@app.get('/')
def hello():
    # Increment the request count metric with service and endpoint tags
    REQUEST_COUNT.labels(service='myapp', endpoint='/').inc()

    # Generate a random integer between a range
    random_number = random.randint(1, 5)
    print(random_number)

    # Convert the dictionary to JSON string
    json_data = data
    # Print the JSON data
    print(json_data)

    # Simulate some processing time
    with REQUEST_TIME.labels(service='myapp', endpoint='/').time():
        # Perform some work here
        time.sleep(random_number)  # Simulate 2 seconds of processing time
        return json_data

if __name__ == '__main__':
    # Start the HTTP server to expose metrics
    start_http_server(8000)

    # Run the FastAPI application using Uvicorn server
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
