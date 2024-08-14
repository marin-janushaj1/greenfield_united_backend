from fastapi import FastAPI
from routes import GET_endpoints, POST_endpoints
from fastapi.middleware.cors import CORSMiddleware
import schemas, database

app = FastAPI()

# Define allowed origins
origins = [
    "http://localhost:7777",  # Adjust this to match your frontend's origin
    "http://localhost:5500",  # Example for another local origin
]

# Add CORS middleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(GET_endpoints.router)
app.include_router(POST_endpoints.router)