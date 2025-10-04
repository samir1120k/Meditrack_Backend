import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get path to service account JSON
cred_path = os.getenv("FIREBASE_CREDENTIALS_PATH")

# Initialize Firebase app only once
if not firebase_admin._apps:
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://bppv-13cd9-default-rtdb.firebaseio.com/'  
    })

# Reference to the 'patients' node (like a table)
patients_ref = db.reference('patients')
