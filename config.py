import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY")

S3_BUCKET_NAME = os.getenv("S3_BUCKET_NAME")

API_GROUPS = {
    "vehicle-availability": "availability/"
}
