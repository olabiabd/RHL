import json
import time
import tempfile
import pandas as pd
from datetime import datetime

from .config import *
from .api_handler import APIHandler
from .processor import process_vehicle_availability
from .s3_uploader import upload_to_s3
from .utils import clean_dataframe_for_redshift

def lambda_handler(event, context):
    api = APIHandler(BASE_URL, API_KEY, SUBSCRIPTION_KEY)

    endpoints = [
        {
            "endpoint": "vehicles/v1/api/vehicle-availability",
            "method": "POST",
            "body": {},
            "group": "vehicle-availability",
        }
    ]

    results = []
    report_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")

    for e in endpoints:
        response = api.request(e["endpoint"], e["method"], e["body"])

        df = pd.DataFrame(process_vehicle_availability(response))
        df["report_time"] = report_time
        df = clean_dataframe_for_redshift(df)

        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
            df.to_csv(tmp.name, index=False)
            s3_key = upload_to_s3(
                tmp.name, S3_BUCKET_NAME, e["endpoint"], API_GROUPS, e["group"]
            )

        results.append({"endpoint": e["endpoint"], "s3_key": s3_key})
        time.sleep(1)

    return {"statusCode": 200, "body": json.dumps(results)}
