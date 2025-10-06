import firebase_admin
from firebase_admin import credentials, db
import os
import json
from dotenv import load_dotenv

# Load local .env variables (only used in local dev)
load_dotenv()

# Read the Firebase credentials JSON string from environment variable
firebase_creds_json = os.getenv("FIREBASE_CREDENTIALS")

if not firebase_creds_json:
    raise ValueError("Missing FIREBASE_CREDENTIALS environment variable.")

# Parse JSON string to dict
firebase_creds_dict = json.loads(firebase_creds_json)

# Initialize Firebase app only once
if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_creds_dict)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://bppv-13cd9-default-rtdb.firebaseio.com/'
    })

# Reference to 'patients' node
patients_ref = db.reference('patients')
