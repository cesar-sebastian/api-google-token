from fastapi import FastAPI
from google.oauth2.service_account import Credentials
from google.auth.transport.requests import Request
from fastapi.middleware.cors import CORSMiddleware
from models.Client import Client
from fastapi import HTTPException
import os
from dotenv import load_dotenv, find_dotenv

app = FastAPI()

load_dotenv(find_dotenv())

origins = [    
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SCOPES = ['https://www.googleapis.com/auth/devstorage.read_write']

@app.post("/google-token/")
def read_root(client: Client):

    if os.getenv(client.name) is None:
        raise HTTPException(status_code=404, detail=f"Not found credentials for {client.name}")
    
    pathFileCredentials = os.getenv(client.name)
    credentials = Credentials.from_service_account_file(pathFileCredentials, scopes=SCOPES)
    credentials.refresh(Request())
    
    return {'access_token': credentials.token}